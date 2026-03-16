
curl -X POST http://localhost:3000/api/submit \
-H "Content-Type: application/json" \
-d '{
"name":"Test User",
"email":"test@test.com",
"role":"Data Engineer",
"data_stack":"Snowflake + dbt",
"data_challenge":"Pipeline failures",
"answers":{
"q1":"Airflow",
"q2":"Transform stage",
"q3":"Dashboards",
"q4":"Yes",
"q5":"Reliable pipelines"
},
"referrer":"test"
}'
