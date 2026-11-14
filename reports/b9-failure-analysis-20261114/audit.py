import csv, hashlib, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import fmean

roots = [Path("outputs") / name for name in (
 "memory-large-stock-20261114-173852", "memory-large-shift-20261114-173852",
 "memory-b9-comparison-20261114-172249", "memory-b9-feasibility-20261114-172249")]
labels = ("large stock", "large shift", "development inference", "fixed-explore feasibility")
dirs = ((1,0),(0,1),(-1,0),(0,-1))
def count(r,k): return r.get(k,0)
def load(path): return json.loads(path.read_text())
def stream(path): return [json.loads(x) for x in path.read_text().splitlines()]
def pose(b): return tuple(b["agent"][k] for k in ("x","y","direction"))
def objects(b,k,state=None): return {(i["x"],i["y"]) for i in b["objects"] if i["object"]==k and (state is None or i["state"]==state)}
def label(phase,env,inter):
 return inter if env.startswith("EmbodiedMind") else env.removeprefix("MiniGrid-").removeprefix("BabyAI-").split("-v")[0]
def matcher(mission,env):
 if "KeyCorridor" in env: return lambda c:c["object"]=="ball"
 if "BlockedUnlock" in env: return lambda c:c["object"]=="box"
 if "DoorKey" in env or "MultiRoom" in env or "Dynamic-Obstacles" in env: return lambda c:c["object"]=="goal"
 tokens = re.findall(r"\b(blue|green|grey|purple|red|yellow) (key|ball|box|door)\b",mission)
 return lambda c:bool(tokens) and (c["color"],c["object"])==tokens[0]
def unpack(path, kind):
 s=load(path/"summary.json")
 t=stream(path/"trajectory.jsonl")
 e=stream(path/"evaluator-steps.jsonl")
 assert len(t)==s["steps"] and len(e)==len(t)+1, path
 assert [x["step"] for x in e]==list(range(len(e))) and [x["step"] for x in t]==list(range(len(t))),path
 assert all(a["next_observation"]==b["observation"] for a,b in zip(t,t[1:])),path
 assert abs(sum(x["reward"] for x in t)-s["reward"])<1e-9, path
 p=[pose(y["board"]) for y in e]
 xy=[x[:2] for x in p]
 ac=Counter(x["executed_action"] for x in t)
 rs=Counter(x["planning"]["reason"] or "unspecified" for x in t)
 goals=Counter(x["planning"]["goal"] for x in t)
 b0=e[0]["board"]; bz=e[-1]["board"]
 selected=matcher(s["mission"],s["environment"])
 open_count=len(objects(bz,"door","open")-objects(b0,"door","open"))
 closed_or_locked=objects(b0,"door","closed")|objects(b0,"door","locked")
 crossing=sum((x!=y and y in closed_or_locked) for x,y in zip(xy,xy[1:]))
 failed_toggles=sum(a["executed_action"]==5 and objects(x["board"],"door","open")==objects(y["board"],"door","open")
                    for a,x,y in zip(t,e,e[1:]))
 st=next((i for i,a in enumerate(t) if any(selected(c) for c in a["observation"]["cells"])),None)
 key_seen=next((i for i,a in enumerate(t) if any(c["object"]=="key" for c in a["observation"]["cells"])),None)
 locked_seen=next((i for i,a in enumerate(t) if any(c["object"]=="door" and c["state"]=="locked" for c in a["observation"]["cells"])),None)
 inv=[(a["next_observation"]["carrying"] or {}).get("object") for a in t]
 picked=sum(x["executed_action"]==3 and bool(x["next_observation"]["carrying"]) and not x["observation"]["carrying"] for x in t)
 blocked=0; wait=longwait=0
 diagnostics=Counter()
 segments={a["memory"].get("event",{}).get("segment") for a in t}
 for i,(a,x,y) in enumerate(zip(t,xy,xy[1:])):
    wait=wait+1 if x==y else 0
    longwait=max(wait,longwait)
    blocked+=a["executed_action"]==2 and x==y
    obs=a["observation"]
    front=next((c for c in obs["cells"] if (c["forward"],c["right"])==(1,0)),None)
    if a["planning"]["reason"]=="progress_aware_explore" and a["executed_action"] in (0,1):
        diagnostics["progress_turns"]+=1
        diagnostics["one_action_progress_turns"]+=len(a["planning"]["route"])==1
        diagnostics["progress_turns_with_empty_front"]+=bool(front and front["object"]=="empty")
    carried=obs["carrying"]
    if (carried and carried["object"]=="key" and front and front["object"]=="door" and front["state"]=="locked"):
        diagnostics["facing_locked_with_key"]+=1
        diagnostics["verify_facing_locked_with_key"]+=a["planning"]["goal"]=="verify"
        diagnostics["toggle_facing_locked_with_key"]+=a["executed_action"]==5
 cue=next((a["memory"]["hallway_cue"] for a in t if a["memory"].get("hallway_cue")),None)
 return dict(run=kind, path=path.as_posix(), game=label(kind,s["environment"],s["intervention"]), seed=s["seed"],
     variant=s["variant"],mission=s["mission"],outcome=s["outcome"],steps=s["steps"],success=s["success"],
     moves=sum(x!=y for x,y in zip(xy,xy[1:])), unique_tiles=len(set(xy)), unique_poses=len(set(p)),
     max_no_move=longwait, turn=ac[0]+ac[1], forward=ac[2], pickup=ac[3], drop=ac[4], toggle=ac[5],
     done=ac[6], effective_pickups=picked, held_key="key" in inv, held_ball="ball" in inv,
     doors_open_at_end=open_count, door_crossings=crossing, unchanged_open_set_toggles=failed_toggles,
     first_target_seen=st, first_key_seen=key_seen, first_locked_door_seen=locked_seen,
     actual_blocked_forward=blocked, **{k:diagnostics[k] for k in (
       "progress_turns","one_action_progress_turns","progress_turns_with_empty_front",
       "facing_locked_with_key","verify_facing_locked_with_key","toggle_facing_locked_with_key")},
     segments=len(segments-{None}),
     explore=goals["explore"], approach=goals["approach"], verify=goals["verify"],
     progress=rs["progress_aware_explore"], burst=rs["forward_burst"],
     task_steps=sum(n for key,n in rs.items() if key in {
        "route_to_subgoal","explore_for_subgoal","attempt_subgoal_interaction","find_key_drop_tile","release_key_after_unlock",
        "route_to_placement","attempt_verified_placement","inspect_toward_start_room","return_toward_start_room","search_hallway","approach_matching_branch"}),
     cue=cue["object"] if cue else "", controller_reasons=dict(rs), proposals=dict(goals),
     exhibit_path=p[0:1]+p[-1:], reward=s["reward"], tokens=s["prompt_tokens"]+s["completion_tokens"])

results=[]; anchors=[]
for root, kind in zip(roots,labels):
 m=load(root/"manifest.json")
 for j in m["jobs"]:
    v=j["variant"]
    if v=="B9": results.append(unpack(root/"episodes"/j["id"],kind))
    elif kind=="large stock" and ((v=="B7" and j["id"].startswith("e01-")) or (v=="B8" and j["id"].startswith("e09-"))):
        anchors.append(unpack(root/"episodes"/j["id"],kind))
assert len(results)==170 and sum(x["run"].startswith("large") for x in results)==140
def agg(xs):
 sums=("turn","forward","pickup","drop","toggle","done","effective_pickups","verify","explore","progress","burst","task_steps",
       "moves","actual_blocked_forward","door_crossings","unchanged_open_set_toggles",
       "progress_turns","one_action_progress_turns","progress_turns_with_empty_front",
       "facing_locked_with_key","verify_facing_locked_with_key","toggle_facing_locked_with_key")
 means=("steps","tokens","unique_tiles","max_no_move","segments")
 boolkeys=("held_key","held_ball","doors_open_at_end","first_target_seen","first_key_seen","first_locked_door_seen","toggle","pickup","drop")
 return dict(n=len(xs),wins=sum(x["success"] for x in xs),
    totals={k:sum(x[k] for x in xs) for k in sums},
    means={k:round(fmean(x[k] for x in xs),1) for k in means},
    episodes={k:sum((x[k] is not None if k.startswith("first_") else bool(x[k])) for x in xs) for k in boolkeys},
    outcomes=dict(Counter(x["outcome"] for x in xs)),
    win_seeds=sorted(x["seed"] for x in xs if x["success"]),
    reasons=dict(sum((Counter(x["controller_reasons"]) for x in xs),Counter())))
game_groups=defaultdict(list)
for x in results+anchors: game_groups[x["run"],x["game"],x["variant"]].append(x)
summary={" / ".join(k):agg(v) for k,v in sorted(game_groups.items())}
path=Path(sys.argv[1])
path.mkdir(exist_ok=True,parents=True)
with (path/"episode-audit.csv").open("w",newline="",encoding="utf-8") as f:
 writer=csv.DictWriter(f,fieldnames=list(results[0]))
 writer.writeheader()
 for row in sorted(results+anchors,key=lambda r:(r["run"],r["game"],r["variant"],r["seed"])):
    writer.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()})
(path/"trace-summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("Run counts",dict(Counter((x["run"],x["success"]) for x in results)))
