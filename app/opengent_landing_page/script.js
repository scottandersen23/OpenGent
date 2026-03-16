
document.getElementById("leadForm").addEventListener("submit", function(e){
e.preventDefault();
document.getElementById("formMessage").innerText =
"Thanks! Your request has been received.";
});
