
import React,{useState,useEffect} from "react"

export default function App(){

 const [success,setSuccess]=useState(false)
 const [showMore,setShowMore]=useState(false)
 const [referrer,setReferrer]=useState("direct")

 useEffect(()=>{
  const params = new URLSearchParams(window.location.search)
  const ref = params.get("ref")
  if(ref) setReferrer(ref)
 },[])

 async function submit(e:any){
  e.preventDefault()

  const form = new FormData(e.target)

  const body={
    name:form.get("name"),
    email:form.get("email"),
    company:form.get("company"),
    role:form.get("role"),
    challenge:form.get("challenge"),
    stack:form.get("stack"),
    referrer
  }

  await fetch("http://localhost:4000/api/lead",{
    method:"POST",
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify(body)
  })

  setSuccess(true)
 }

 if(success){
  return <div style={{padding:60}}>You're on the list. We'll notify you soon.</div>
 }

 return(
 <div style={{padding:40,maxWidth:900,margin:"auto"}}>

  <img src="/logo.png" style={{width:160}}/>

  <h1>AI agents that monitor data pipelines before issues impact business metrics.</h1>

  <button onClick={()=>document.getElementById("signup")?.scrollIntoView({behavior:"smooth"})}>
   Get Early Access
  </button>

  <section style={{marginTop:80}}>

   <h2>Modern SaaS companies rely on data pipelines to run the business.</h2>

   <ul>
   <li>Broken pipelines corrupt dashboards</li>
   <li>Revenue anomalies go unnoticed</li>
   <li>Teams spend hours debugging metrics</li>
   </ul>

  </section>

  <section id="signup" style={{marginTop:80}}>

   <h2>Get early access to OpenGent</h2>

   <form onSubmit={submit}>

    <input name="name" placeholder="Name" required/><br/>
    <input name="email" placeholder="Email" required/><br/>
    <input name="company" placeholder="Company"/><br/>

    {!showMore &&
     <button type="button" onClick={()=>setShowMore(true)}>
      Add details (optional)
     </button>
    }

    {showMore &&
    <div>
     <input name="role" placeholder="Role"/><br/>
     <input name="challenge" placeholder="Data challenge"/><br/>
     <input name="stack" placeholder="Data stack"/><br/>
    </div>
    }

    <input type="hidden" name="referrer" value={referrer}/>

    <button type="submit">Join Early Access</button>

   </form>

  </section>

 </div>
 )
}
