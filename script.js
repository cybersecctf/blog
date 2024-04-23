// Fetch the content of ai.txt
fetch('https://cybersecctf.github.io/blog/Ai')
    .then(response => response.text())
    .then(data => {
        // Split the content into lines
        var lines = data.split('\n');
 
        // Get the input line element
        var inputLine = document.getElementById('input-line');

        // Add a click event listener to the input line
        inputLine.addEventListener('click', function() {
            // Get the current input value
            var input = inputLine.value;
            
            // Loop   over the lines
            for (var i = 0; i < lines.length; i++) {
                // If the line includes the keyword
                if (lines[i].includes(input)) {
                    // Extract the URL of the markdown file from the line
                    var mdFileUrl = lines[i].split(', ')[1];

                    // Fetch the content of the markdown file
                    fetch(mdFileUrl)
                        .then(response => response.text())
                        .then(mdData => {
                            // Display the content of the markdown file
                            document.getElementById('output').innerText = mdData;
                        });

                    // Stop searching after finding the first match
                    break;
                }
            }
        });
    });

