# My Interactive Web Page

Welcome to my simple yet interactive web page created using Markdown, HTML, CSS, and JavaScript!

<div class="container">
    <div class="content">
        <h2>About This Page</h2>
        <p>This page demonstrates how you can combine Markdown with HTML, CSS, and JavaScript to create an interactive web experience.</p>
        <button id="infoButton">Click Me for Info</button>
        <div id="infoText" style="display:none; margin-top: 10px;">
            <p>Here's some additional information that appears when you click the button!</p>
        </div>
    </div>
</div>

## More Features

Here's another section with more features:

<div class="content">
    <h3>Subscribe to Our Newsletter</h3>
    <form action="https://example.com/subscribe" method="POST">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <button type="submit">Subscribe</button>
    </form>
</div>

## JavaScript and Internet Connection

<div class="content">
    <h3>Check Internet Connection</h3>
    <button id="checkConnectionButton">Check Connection</button>
    <p id="connectionStatus"></p>
</div>

<style>
.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
}

.content {
    background-color: #f0f0f0;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
}

button {
    padding: 10px 20px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

input[type="email"] {
    padding: 8px;
    margin-right: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
</style>

<script>
document.getElementById("infoButton").addEventListener("click", function() {
    var infoText = document.getElementById("infoText");
    if (infoText.style.display === "none") {
        infoText.style.display = "block";
    } else {
        infoText.style.display = "none";
    }
});

document.getElementById("checkConnectionButton").addEventListener("click", function() {
    var connectionStatus = document.getElementById("connectionStatus");
    if (navigator.onLine) {
        connectionStatus.innerHTML = "You are connected to the internet!";
        connectionStatus.style.color = "green";
    } else {
        connectionStatus.innerHTML = "You are offline. Please check your connection.";
        connectionStatus.style.color = "red";
    }
});
</script>
