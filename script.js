 // Fetch the content of ai.txt
fetch('https://cybersecctf.github.io/blog/ai.txt')
    .then(response => response.text())
    .then(data => {
        // Split the content into lines
        var lines = data.split('\n');

        // Loop over the lines
        for (var i = 0; i < lines.length; i++) {
            // If the line includes the keyword
             var input = event.target.value; 
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
