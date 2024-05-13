document.getElementById("instance").addEventListener("click", function() {
    var contentDiv = document.getElementById("content");
    if (contentDiv.style.display === "none") {
        contentDiv.style.display = "block"; // Show the div
    } else {
        contentDiv.style.display = "none"; // Hide the div
    }
});