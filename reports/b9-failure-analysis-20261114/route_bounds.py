"""Evaluator-only action-length analysis using saved spawn boards."""
import csv
import json
import re
import sys
from collections import deque
from pathlib import Path

DIRECTIONS = ((1,0),(0,1),(-1,0),(0,-1))
SOURCE = Path("outputs/memory-large-stock-20261114-173852/episodes")

def shortest(board, mission, game, *, relax=False):
    walls = {(o["x"],o["y"]) for o in board["objects"] if o["object"] in {"wall","lava"}}
    gates = [((o["x"],o["y"]),o["color"],o["state"]=="locked")
             for o in board["objects"] if o["object"]=="door"]
    gate_at = {gate[0]:i for i,gate in enumerate(gates)}
    goals = {(o["x"],o["y"]) for o in board["objects"] if o["object"]=="goal"}
    items = [((o["x"],o["y"]),o["object"],o["color"]) for o in board["objects"]
             if o["object"] in {"key","ball","box"}]
    open_mask = sum(1<<i for i,gate in enumerate(gates) if any(
        (o["x"],o["y"])==gate[0] and o["state"]=="open" for o in board["objects"]))
    start = ((board["agent"]["x"],board["agent"]["y"]), board["agent"]["direction"],
             open_mask, -1, tuple(o[0] for o in items))
    obj = re.fullmatch(r"go to the (\w+) (\w+)",mission)
    go_to = {(i,j) for (i,j),k,c in items if obj and obj.groups()==(c,k)}
    queue=deque([(start,())])
    seen={start}
    while queue:
        (p,heading,opened,held,locations),path=queue.popleft()
        dx,dy=DIRECTIONS[heading]
        ahead=p[0]+dx,p[1]+dy
        door=gate_at.get(ahead)
        if p in goals or (game==2 and path and ahead in go_to):
            return path
        # Closing doors is unnecessary here. Opening consumes one action.
        door_open=relax or door is None or opened & (1<<door)
        free=(0<=ahead[0]<board["width"] and 0<=ahead[1]<board["height"]
              and ahead not in walls and (relax or ahead not in locations) and door_open)
        successors=[
            (0,(p,(heading-1)%4,opened,held,locations)),
            (1,(p,(heading+1)%4,opened,held,locations)),
        ]
        if free:
            successors.append((2,(ahead,heading,opened,held,locations)))
        if door is not None and not door_open:
            _,color,locked=gates[door]
            if not locked or (held>=0 and items[held][1:]==("key",color)):
                successors.append((5,(p,heading,opened|(1<<door),held,locations)))
        if game in (1,7):
            if held<0 and ahead in locations:
                index=locations.index(ahead)
                if game==7 and items[index][1]=="box":
                    return (*path,3)
                updated=(*locations[:index],None,*locations[index+1:])
                successors.append((3,(p,heading,opened,index,updated)))
            if game==7 and held>=0 and free and door is None and ahead not in goals:
                updated=(*locations[:held],ahead,*locations[held+1:])
                successors.append((4,(p,heading,opened,-1,updated)))
        for action,state in successors:
            if state not in seen:
                seen.add(state)
                queue.append((state,(*path,action)))
    return None

results=[]
for game,title in ((1,"DoorKey"),(2,"GoToObj Maze"),(5,"MultiRoom"),(7,"Blocked Unlock Pickup")):
    for folder in sorted(SOURCE.glob(f"e{game:02}-*-B9-r0")):
        summary=json.loads((folder/"summary.json").read_text())
        with (folder/"evaluator-steps.jsonl").open() as source:
            board=json.loads(next(source))["board"]
        route=shortest(board,summary["mission"],game)
        relaxed=shortest(board,summary["mission"],game,relax=True) if game==2 else None
        results.append({"game":title,"seed":summary["seed"],"modeled_actions":len(route) if route is not None else None,
                        "within_48": route is not None and len(route)<=48,
                        "relaxed_wall_only_actions":len(relaxed) if relaxed is not None else None,
                        "modeled_route":" ".join(map(str,route)) if route is not None else "",
                        "source":folder.as_posix()})
    rows=[r for r in results if r["game"]==title]
    print(title,[(r["seed"],r["modeled_actions"]) for r in rows])
target=Path(sys.argv[1])
with (target/"evaluator-route-lengths.csv").open("w",encoding="utf-8",newline="") as out:
    writer=csv.DictWriter(out,fieldnames=list(results[0]))
    writer.writeheader()
    writer.writerows(results)
