
import express from "express"
import cors from "cors"
import pkg from "@prisma/client"

const { PrismaClient } = pkg
const prisma = new PrismaClient()

const app = express()
app.use(cors())
app.use(express.json())

app.post("/api/lead", async (req,res)=>{

 const {name,email,company,role,challenge,stack,referrer} = req.body

 try{

  const lead = await prisma.lead.create({
    data:{
      name,
      email,
      company,
      role,
      data_challenge: challenge,
      data_stack: stack,
      referrer
    }
  })

  res.json({success:true})

 }catch(e){
  console.error(e)
  res.status(500).json({error:"failed"})
 }

})

app.listen(4000,()=>{
 console.log("API running on port 4000")
})
