
import { LineChart,Line,XAxis,YAxis,Tooltip } from 'recharts'

const data=[
{name:'1',value:10},
{name:'2',value:12},
{name:'3',value:9},
{name:'4',value:15},
{name:'5',value:11}
]

export default function Pipeline(){

return(

<section className="section">

<h2>Pipeline Health</h2>

<LineChart width={600} height={300} data={data}>
<XAxis dataKey="name"/>
<YAxis/>
<Tooltip/>
<Line type="monotone" dataKey="value"/>
</LineChart>

</section>

)
}
