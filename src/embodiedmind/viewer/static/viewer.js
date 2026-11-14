"use strict";

const $ = (id) => document.getElementById(id);
const variants = {B0:"Reactive", B1:"Text history", B2:"Structured", B3:"Hybrid"};
const actions = ["Turn left","Turn right","Forward","Pick up","Drop","Toggle door","Done"];
const headings = ["east","south","west","north"];
const colors = {red:"#e06652",green:"#65ba83",blue:"#70a7df",purple:"#b690da",yellow:"#e3c971",grey:"#a1aaa5"};
const front = [[1,0],[0,1],[-1,0],[0,-1]];
const worlds = {"MiniGrid-DoorKey-8x8-v0":"DoorKey","BabyAI-GoToObjMazeS7-v0":"GoToObjMaze",
  "BabyAI-GoToObjS6-v1":"GoToObj","EmbodiedMind-GoToShift-v0":"GoToShift"};
const defaultRun = "embodiedmind-20261114-0428-ist/static";
const model = {mode:"replay", runs:[], jobs:[], episodes:[], position:7, request:0, play:null,
  liveTimer:null, sandbox:null, sandboxTimer:null, sandboxBusy:false};

function node(tag, text, className) {
  const element = document.createElement(tag);
  if (text !== undefined) element.textContent = text;
  if (className) element.className = className;
  return element;
}
function labelRun(run) {
  return run.id.replace("embodiedmind-20261114-0428-ist/", "Study / ");
}
function options(select, entries, previous = select.value) {
  select.replaceChildren(...entries.map(([value, label]) => new Option(label, value)));
  if (entries.some(([value]) => value === previous)) select.value = previous;
}
function error(message) { $("error").textContent = message; $("error").hidden = !message; }
function outcome(value) { return String(value).replaceAll("_", " "); }

async function api(path, params, body) {
  const url = "/api/" + path + (params ? "?" + new URLSearchParams(params) : "");
  const result = await fetch(url, body ? {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(body)} : {});
  const value = await result.json();
  if (!result.ok) throw new Error(value.error);
  return value;
}

function draw(canvas, board, obs, highlight) {
  const raw = canvas.getContext("2d");
  const size = 30;
  const width = board ? board.width : 7, height = board ? board.height : 7;
  canvas.width = width * size;
  canvas.height = height * size;
  canvas.setAttribute("role","img");
  canvas.setAttribute("aria-label", board ? "Full evaluator board" : "Agent view, facing " + headings[obs.direction]);
  raw.fillStyle = board ? "#273633" : "#16221f";
  raw.fillRect(0,0,canvas.width,canvas.height);
  const tiles = board ? board.objects : obs.cells.map(c => ({...c,x:c.right+3,y:6-c.forward}));
  const player = board ? board.agent : {x:3,y:6,direction:3};
  for (const tile of tiles) {
    const {x,y,state} = tile, px = x*size, py = y*size, cx = px+15, cy = py+15;
    const color = colors[tile.color] || "#a1aaa5";
    if (!board) {
      raw.fillStyle = "#30413b";
      raw.fillRect(px,py,size,size);
    }
    if (tile.object === "wall") {
      raw.fillStyle = "#74837b"; raw.fillRect(px+1,py+1,28,28);
      raw.fillStyle = "#87948c"; raw.fillRect(px+4,py+4,22,2);
    } else if (tile.object === "goal" || tile.object === "lava") {
      raw.fillStyle = tile.object === "goal" ? "#64b979" : "#d45a49";
      raw.fillRect(px+3,py+3,24,24);
      raw.strokeStyle = "#e1f6df"; raw.strokeRect(px+7,py+7,16,16);
    } else if (tile.object === "door") {
      raw.strokeStyle = color; raw.lineWidth = 3;
      raw.strokeRect(px+4,py+3,22,24);
      if (state !== "open") {
        raw.fillStyle = color; raw.fillRect(px+8,py+6,14,18);
        raw.fillStyle = "#24302c"; raw.fillRect(px+17,py+14,3,3);
      }
    } else if (tile.object === "key") {
      raw.strokeStyle = color; raw.lineWidth = 3; raw.beginPath();
      raw.arc(cx-5,cy,4,0,Math.PI*2); raw.moveTo(cx-1,cy); raw.lineTo(cx+10,cy);
      raw.lineTo(cx+10,cy+4); raw.stroke();
    } else if (tile.object === "ball" || tile.object === "box") {
      raw.fillStyle = color;
      if (tile.object === "box") raw.fillRect(px+7,py+7,16,16);
      else {raw.beginPath(); raw.arc(cx,cy,9,0,Math.PI*2); raw.fill();}
    }
  }
  raw.strokeStyle = "#92a69738"; raw.lineWidth=1; raw.beginPath();
  for(let x=0;x<=width;x++){raw.moveTo(x*size,0);raw.lineTo(x*size,canvas.height);}
  for(let y=0;y<=height;y++){raw.moveTo(0,y*size);raw.lineTo(canvas.width,y*size);}
  raw.stroke();
  raw.save(); raw.translate(player.x*size+15,player.y*size+15); raw.rotate(player.direction*Math.PI/2);
  raw.fillStyle = "#fc7c64"; raw.beginPath(); raw.moveTo(11,0); raw.lineTo(-8,-8); raw.lineTo(-8,8);
  raw.closePath(); raw.fill(); raw.strokeStyle="#401b14"; raw.stroke(); raw.restore();
  if (board && highlight) {
    raw.strokeStyle="#fff1ae"; raw.lineWidth=3;
    raw.strokeRect(highlight[0]*size+3,highlight[1]*size+3,24,24);
  }
}
function field(list, key, value, className) {
  list.append(node("dt",key),node("dd",value,className));
}
function boardCard({title, status, failed, frame, replay, action, intervention}) {
  const card = node("article",undefined,"agent-card");
  const head = node("div",undefined,"card-head");
  head.append(node("h2",title),node("span",status,"badge"+(failed?" bad":"")));
  card.append(head);
  if (!frame?.board || !frame.observation) return card;
  const charts = node("div",undefined,"boards");
  const world = node("canvas"), pov = node("canvas");
  for (const [label, canvas] of [["Full board · evaluator",world],["7 × 7 · agent view",pov]]) {
    const figure = node("figure");
    figure.append(node("figcaption",label),canvas);
    charts.append(figure);
  }
  const {board,observation,event} = frame;
  draw(world,board,observation); draw(pov,null,observation);
  card.append(charts);
  const stats = node("dl");
  field(stats,"Facing",headings[observation.direction]);
  field(stats,"Carrying",observation.carrying ? [observation.carrying.color, observation.carrying.object].join(" ") : "Nothing");
  if (intervention) {
    const description = intervention.applied && intervention.new_position
      ? "Target moved " + intervention.old_position.join(", ") + " → " + intervention.new_position.join(", ")
      : intervention.applied ? intervention.masked_cells + " visible tiles masked" : outcome(intervention.reason);
    field(stats,"World event",description);
  }
  if (event) {
    const hint = event.hint?.replace(/next suggested action: (\d)\./,
      (_, id) => "next suggested action: "+actions[id]+".").replace(/\(([01])\)\.$/,
      (_, id) => " ("+actions[id].toLowerCase()+").");
    field(stats,"Hint",hint || (event.scripted?"Scripted turn":"—"));
    field(stats,"Action",actions[event.action] || "—");
    field(stats,"Outcome",event.moved === false ? "Blocked · stayed in place" : event.reward > 0 ?
      "Mission completed" : event.moved === true ? "Moved one tile" : "Action applied",event.moved === false?"blocked":"");
    const evidence=event.decision?.evidence;
    if(evidence) {
      field(stats,"Evidence",evidence);
      const cited=event.facts?.find(fact=>fact.relative && (evidence===fact.id || evidence.startsWith(fact.id+" ")));
      if(cited) {
        const button=node("button","Highlight "+cited.id,"evidence-link");
        button.type="button";
        button.setAttribute("aria-pressed","false");
        button.onclick=()=> {
          const pressed=button.getAttribute("aria-pressed")==="true";
          const {x,y,direction}=board.agent, [dx,dy]=front[direction], [f,r]=cited.relative;
          button.setAttribute("aria-pressed",String(!pressed));
          draw(world,board,observation,pressed?null:[x+f*dx-r*dy,y+f*dy+r*dx]);
        };
        stats.lastElementChild.append(document.createTextNode(" "),button);
      }
    }
  }
  card.append(stats);
  if (event?.prompt) {
    const details = node("details");
    details.append(node("summary","Model input and memory"),node("pre",event.prompt));
    for (const fact of event.facts || []) {
      const button = node("button", [fact.id,fact.color,fact.object].filter(Boolean).join(" "), "fact");
      const coordinates = fact.relative;
      button.disabled = !coordinates;
      if (coordinates) {
        button.type="button";
        button.setAttribute("aria-pressed","false");
        button.addEventListener("click",() => {
          const pressed=button.getAttribute("aria-pressed")==="true";
          details.querySelectorAll("button").forEach(b=>b.setAttribute("aria-pressed","false"));
          button.setAttribute("aria-pressed",String(!pressed));
          const here=board.agent, [dx,dy]=front[here.direction], [f,r]=coordinates;
          draw(world,board,observation,pressed?null:[here.x+f*dx-r*dy, here.y+f*dy+r*dx]);
        });
      }
      details.append(button);
    }
    card.append(details);
  }
  if (replay && event) {
    const button = node("button","Take over before action "+action,"jump");
    button.type="button"; button.addEventListener("click",replay); card.append(button);
  }
  return card;
}
function stopReplay() {
  clearInterval(model.play); model.play=null; $("play").textContent="Play";
}
function setMode(mode) {
  model.mode=mode; error("");
  stopReplay(); stopAgent();
  for (const key of ["replay","live","sandbox"]) $(key).hidden = key !== mode;
  document.querySelectorAll("[data-mode]").forEach(button=>button.setAttribute("aria-pressed",button.dataset.mode===mode));
  clearTimeout(model.liveTimer);
  if (mode==="replay") renderReplay();
  if (mode==="live") {
    setHeading("Live monitor","Experiment progress","Select a run to follow its current episode.");
    updateLive();
  }
  if(mode==="sandbox") {
    setHeading("Exploratory simulation","MiniGrid sandbox","Manual control and local agent moves");
    if (!model.sandbox) startSandbox();
  }
}
function setHeading(label,title,subtitle) {
  $("mode-label").textContent=label; $("title").textContent=title; $("subtitle").textContent=subtitle;
}
const scenario = (job) => [job.environment,job.intervention,job.replicate].join("|");
function updateSeeds(seed) {
  const jobs=model.jobs.filter(j=>scenario(j)===$("scenario").value);
  options($("seed"),[...new Set(jobs.map(j=>j.seed))].sort((a,b)=>a-b).map(n=>[String(n),n]),seed);
}
async function openRun(initial=false) {
  const token=++model.request;
  stopReplay(); error("");
  model.episodes=[]; renderReplay();
  const run=$("replay-run").value;
  const jobs=run ? await api("jobs",{run}) : [];
  if (token!==model.request) return;
  model.jobs=jobs;
  const unique=new Map(model.jobs.map(j=>[scenario(j),worlds[j.environment]+" · "+j.intervention.replaceAll("_"," ")
    +(j.replicate ? " · repeat "+(j.replicate+1):"")]));
  options($("scenario"),[...unique],initial?"MiniGrid-DoorKey-8x8-v0|none|0":"");
  updateSeeds(initial?"1015":"");
  await loadPair(initial ? 7 : 0, initial);
}
async function loadPair(position, initial=false) {
  const token=++model.request;
  stopReplay(); error("");
  const match = model.jobs.filter(j=>scenario(j)===$("scenario").value && j.seed===Number($("seed").value));
  const entries=match.map(j=>[j.variant,j.variant+" · "+variants[j.variant]]).sort();
  options($("left"),entries,initial?"B0":$("left").value);
  const right=$("right").value;
  options($("right"),entries,initial?"B2":right);
  if (!initial && !right && entries.length>1) $("right").selectedIndex=1;
  model.episodes=[];
  $("comparison").textContent=match.length?"Loading saved episodes…":"No completed episodes in this run.";
  if (!match.length) {renderReplay();return;}
  const run=$("replay-run").value;
  const pair=await Promise.all(["left","right"].map(key=>api("replay",{run,job:match.find(j=>j.variant===$(key).value).id})));
  if (token!==model.request) return;
  model.episodes=pair; model.position=position; renderReplay();
}
function isBlocked(event) { return event?.action===2 && event?.moved===false; }
const milestones = {
  blocked: f => isBlocked(f.event),
  pickup: (f,next) => f.event?.action===3 && next?.observation.carrying?.object==="key",
  door: (f,next) => f.event?.action===5 && next?.board.objects.some(tile=>
    tile.object==="door" && tile.state==="open" && f.board.objects.some(previous=>
      previous.x===tile.x && previous.y===tile.y && previous.object==="door" && previous.state!=="open")),
};
function milestone(key) {
  const indexes=model.episodes.map(({frames})=>frames.findIndex((frame,index)=>milestones[key](frame,frames[index+1])))
    .filter(index=>index>=0);
  return key==="blocked" ? model.episodes[1]?.frames.findIndex(f=>isBlocked(f.event)) ?? -1 :
    indexes.length ? Math.min(...indexes) : -1;
}
function renderReplay() {
  if(model.mode!=="replay") return;
  const [first,second]=model.episodes;
  const end=first?Math.max(first.summary.steps,second.summary.steps):0;
  model.position=Math.min(end,Math.max(0,model.position));
  $("step").max=end; $("step").value=model.position;
  $("step-label").textContent=first && model.position===end?"Final state":"Action "+(model.position+1);
  for(const key of ["step","play","prev","next"]) $(key).disabled=!first;
  for(const key of Object.keys(milestones)) $(key).disabled=milestone(key)<0;
  $("prev").disabled=!first||model.position===0; $("next").disabled=!first||model.position===end;
  if(!first){
    setHeading("Recorded episodes","Replay comparison","Choose a saved run to compare episodes.");
    $("comparison").textContent="No episodes loaded.";
    return;
  }
  setHeading("Recorded episodes",worlds[first.summary.environment]+" comparison",
    "Seed "+first.summary.seed+" · "+first.summary.mission);
  $("comparison").replaceChildren(...model.episodes.map(episode=>{
    const {summary,frames}=episode;
    const at=Math.min(model.position,frames.length-1);
    return boardCard({
      title:summary.variant+" · "+variants[summary.variant],
      status:summary.success?"Success · "+summary.steps+" actions":outcome(summary.outcome)+" · "+summary.steps+" actions",
      failed:!summary.success, frame:frames[at], action:at+1,
      intervention:episode.interventions.find(event=>event.step===at),
      replay:()=>takeOver(summary,at),
    });
  }));
}
async function refreshCatalog() {
  const catalog=await api("catalog");
  model.runs=catalog.runs;
  const list=model.runs.map(r=>[r.id,labelRun(r)]);
  options($("replay-run"),list,$("replay-run").value||defaultRun);
  options($("live-run"),list,$("live-run").value||defaultRun);
  options($("sandbox-env"),catalog.environments.map(v=>[v,worlds[v]]), "MiniGrid-DoorKey-8x8-v0");
  options($("sandbox-intervention"),catalog.interventions.map(v=>[v,v.replaceAll("_"," ")]));
}
async function updateLive() {
  clearTimeout(model.liveTimer);
  if(model.mode!=="live") return;
  const run=$("live-run").value;
  if (!run) { $("live-status").textContent="No runs found. Refresh runs after launching a monitored run."; return; }
  try {
    const {heartbeat,snapshots}=await api("live",{run});
    if(model.mode!=="live"||run!==$("live-run").value) return;
    const h=$("progress"); h.max=heartbeat.planned||1; h.value=heartbeat.completed||0;
    $("live-status").textContent=(heartbeat.status ?
      outcome(heartbeat.status)+" · "+(heartbeat.completed||0)+"/"+(heartbeat.planned||0)+" episodes · "+(heartbeat.errors||0)+" errors" :
      "Waiting for the run to start") + (heartbeat.at ? " · "+new Date(heartbeat.at).toLocaleTimeString():"");
    error("");
    $("live-boards").replaceChildren(...snapshots.map(s=>boardCard({
      title:s.job.variant+" · Seed "+s.job.seed,
      status:s.error ? outcome(s.phase)+": "+s.error : outcome(s.phase)+" · "+s.step+" actions",
      failed:!!s.error,frame:{board:s.board,observation:s.observation,
        event:s.decision?.action !== undefined ? {...s.decision, decision:s.decision}:null},
    })));
    if(!snapshots.length) $("live-boards").textContent="No live board snapshots. Start a run with --monitor.";
  } catch(e){ error(e.message); }
  if(model.mode==="live" && run===$("live-run").value) model.liveTimer=setTimeout(updateLive,650);
}
function stopAgent() {
  clearTimeout(model.sandboxTimer); model.sandboxTimer=null; $("agent-run").textContent="Auto-play";
}
function takeOver(summary, step) {
  model.sandbox={branch:{run:$("replay-run").value,job:summary.id,step}, actions:[]};
  $("sandbox-variant").value=summary.variant;
  setMode("sandbox");
  sandboxRequest();
}
function startSandbox() {
  stopAgent();
  model.sandbox={environment:$("sandbox-env").value, seed:Number($("sandbox-seed").value),
    intervention:$("sandbox-intervention").value,actions:[]};
  return sandboxRequest();
}
async function sandboxRequest({action,agent=false,save=false}={}) {
  if(!model.sandbox || model.sandboxBusy) return;
  model.sandboxBusy=true; error("");
  const session=model.sandbox;
  const body={...session, variant:$("sandbox-variant").value,agent_step:agent,save};
  if(action!==undefined) body.actions=[...session.actions,action];
  const buttons=[...$("sandbox").querySelectorAll("button")].filter(b=>b.id!=="agent-run");
  buttons.forEach(b=>b.disabled=true);
  $("sandbox-status").textContent=agent?"Waiting for Ollama…":"Updating sandbox…";
  let state;
  try {
    state=await api("sandbox",null,body);
    if(model.sandbox!==session) return;
    session.actions=state.actions; session.done=state.done;
    $("branch").textContent=session.branch?"Forked before action "+(session.branch.step+1)+" · "+session.branch.job:
      worlds[session.environment]+" · Seed "+session.seed;
    $("sandbox-board").replaceChildren(boardCard({title:state.observation.mission,
      status:state.done?(state.reward>0?"Success":"Ended"):state.step+" actions applied", frame:state}));
    $("sandbox-status").textContent=state.saved?"Saved in sandbox output as "+state.saved:
      state.decision ? "Agent chose "+actions[state.decision.action]+(state.moved===false?" · blocked":""):
      action!==undefined ? actions[action]+(state.moved===false?" · blocked":"") : "Ready";
  } catch(e) { if(model.mode==="sandbox") error(e.message); stopAgent(); }
  finally {
    model.sandboxBusy=false;
    buttons.forEach(b=>b.disabled=false);
    if (model.sandbox===session && session.done) {
      $("manual").disabled=true; $("agent-step").disabled=true; stopAgent();
    } else $("manual").disabled=false;
  }
  return state;
}
async function autoAgent() {
  if (model.sandboxTimer===null || model.mode!=="sandbox") return;
  const state=await sandboxRequest({agent:true});
  if (state && !state.done && model.sandboxTimer!==null) model.sandboxTimer=setTimeout(autoAgent,330);
  else stopAgent();
}
function safe(fn) { return (...args)=>Promise.resolve().then(()=>fn(...args)).catch(e=>error(e.message)); }

document.querySelectorAll("[data-mode]").forEach(b=>b.onclick=()=>setMode(b.dataset.mode));
$("replay-run").onchange=safe(()=>openRun());
$("scenario").onchange=safe(()=>{updateSeeds("");return loadPair(0);});
for(const key of ["seed","left","right"]) $(key).onchange=safe(()=>loadPair(model.position));
$("step").oninput=()=>{model.position=Number($("step").value);renderReplay();};
$("prev").onclick=()=>{model.position--;renderReplay();}; $("next").onclick=()=>{model.position++;renderReplay();};
for(const key of Object.keys(milestones)) $(key).onclick=()=>{model.position=milestone(key);renderReplay();};
$("play").onclick=()=>{
  if(model.play!==null) return stopReplay();
  if(model.position>=Number($("step").max)) model.position=0;
  renderReplay();
  $("play").textContent="Pause";
  model.play=setInterval(()=>{
    model.position++; renderReplay();
    if(model.position>=Number($("step").max)) stopReplay();
  },420);
};
$("live-run").onchange=updateLive;
$("refresh-live").onclick=safe(async()=>{await refreshCatalog();await updateLive();});
$("sandbox-form").onsubmit=(event)=>{event.preventDefault();startSandbox();};
$("sandbox-env").onchange=()=>{$("intervention-field").hidden=$("sandbox-env").value!=="EmbodiedMind-GoToShift-v0";};
for(const [action,name] of actions.entries()){
  const button=node("button",name);button.type="button";button.onclick=()=>sandboxRequest({action});$("actions").append(button);
}
$("agent-step").onclick=()=>sandboxRequest({agent:true});
$("agent-run").onclick=()=>{
  if(model.sandboxTimer!==null) return stopAgent();
  if(model.sandboxBusy||model.sandbox?.done) return;
  $("agent-run").textContent="Pause agent";
  model.sandboxTimer=setTimeout(autoAgent,0);
};
$("save").onclick=()=>sandboxRequest({save:true});
document.addEventListener("keydown",event=>{
  if(model.mode!=="sandbox" || model.sandboxBusy || model.sandbox?.done ||
    event.altKey || event.ctrlKey || event.metaKey || /INPUT|SELECT|TEXTAREA|BUTTON/.test(event.target.tagName)) return;
  const keyActions={ArrowLeft:0,ArrowRight:1,ArrowUp:2,p:3,d:4,t:5};
  if(keyActions[event.key]!==undefined){event.preventDefault();sandboxRequest({action:keyActions[event.key]});}
});
safe(async()=>{await refreshCatalog();await openRun(true);})();
