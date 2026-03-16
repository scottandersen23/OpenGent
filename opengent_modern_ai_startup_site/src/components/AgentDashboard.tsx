
import { useState } from 'react'

export default function AgentDashboard(){

const [logs,setLogs]=useState<string[]>([])

function runAgent(){

const steps=[
"Checking pipeline freshness",
"Validating schemas",
"Running anomaly detection",
"Detecting revenue drift",
"Generating executive report"
]

let i=0

const timer=setInterval(()=>{

setLogs(prev=>[...prev,steps[i]])

i++

if(i===steps.length) clearInterval(timer)

},800)

}

return(

<section className="section">

<h2>Agent Simulation</h2>

<button onClick={runAgent}>Run Agent</button>

<pre className="logs">

{logs.map((l,i)=>(<div key={i}>{l}</div>))}

</pre>

</section>

)
}
