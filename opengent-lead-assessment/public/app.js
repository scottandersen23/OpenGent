
const form = document.getElementById("assessmentForm");

form.addEventListener("submit", async (e) => {

e.preventDefault();

const data = new FormData(form);

const payload = {
name: data.get("name"),
email: data.get("email"),
role: data.get("role"),
data_stack: data.get("data_stack"),
data_challenge: data.get("data_challenge"),
answers: {
q1: data.get("q1"),
q2: data.get("q2"),
q3: data.get("q3"),
q4: data.get("q4"),
q5: data.get("q5")
},
referrer: data.get("referrer")
};

const res = await fetch("/api/submit", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(payload)
});

const result = await res.json();

document.getElementById("response").innerText =
"Assessment submitted successfully.";

});
