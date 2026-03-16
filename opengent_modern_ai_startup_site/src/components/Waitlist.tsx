
import axios from 'axios'

export default function Waitlist(){

async function join(){

await axios.post('/api/waitlist',{email:"demo@email.com"})

alert("Added to waitlist")

}

return(

<section className="section">

<h2>Join the Waitlist</h2>

<p>Get early access to OpenGent.</p>

<button onClick={join}>Join Waitlist</button>

</section>

)
}
