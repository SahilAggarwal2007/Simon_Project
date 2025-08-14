async function askSimon() {
    const prompt = document.getElementById("userInput").value;
    const responseDiv = document.getElementById("response");

    const response = await fetch("http://127.0.0.1:5000/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: prompt })
    });

    const data = await response.json();
    responseDiv.innerText = data.reply;
}
