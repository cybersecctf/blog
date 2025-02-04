var currenturl="";
var currentflag="";
function getQueryParamOrDefault(name, defaultValue) {
    const urlParams = new URLSearchParams(window.location.search);
    const value = urlParams.get(name);
    return value !== null ? value : defaultValue;
  }
  function hasQueryParam(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.has(name);
  }
  function endsWith(str, suffix) {
    return str.indexOf(suffix, str.length - suffix.length) !== -1;
  }
   function find(event) {
        console.log("Enter key is pressed"+event.keyCode);
                  if (event.keyCode == 13) {
             var userInput = document.getElementById('search-box').value;
   if (userInput.includes('{') && userInput.includes('}'))
{
 checkflag();
return;
}
else
        window.location.href=  "https://cybersecctf.github.io/blog/?q="+userInput ;
              }
}
function addcomment(writeupList)
{
                      // Add the link to the headings
                      var writeupItem = document.createElement('li');
                      var link = document.createElement('a');
                      link.href = "https://github.com/cybersecctf/blog/issues/1";
                      link.textContent ="comments";
                      link.title = "comments";
                      link.classList.add('writeup-link'); // Add the 'writeup-link' class
                      link.dataset.content = ''; // Placeholder for content, update this dynamically if needed
                      writeupItem.appendChild(link);
                      writeupList.appendChild(writeupItem);
                      return writeupList;
}
  function filterWriteups() {
            var query = document.getElementById('search-box').value.toLowerCase();
            query= getQueryParamOrDefault('q', query);




            var links = document.getElementsByClassName('writeup-link');
           links=addcomment(links);
            var resultsCount = 0;
            var linksvalue=links.length
            if (linksvalue>3)
                       linksvalue=3
            for (var i = 0; i < linksvalue; i++) {
                var title = links[i].textContent.toLowerCase();
                var truncatedTitle = links[i].title.toLowerCase();
                var link = links[i].href;
               
                var content = links[i].dataset.content.toLowerCase();
                 var writeup="";
               if(endsWith( link,".md"))
                   writeup= renderMarkdown(link);
            
                if (title.includes(query) || truncatedTitle.includes(query) || link.includes(query) || content.includes(query)) {
                    links[i].parentElement.style.display = '';
                   if(resultsCount==0)
                          {
                            console.log("visible"+links[i].href);    
                             loadWriteupContent(links[i].href);
                            }
                       if(resultsCount>2)
                             break;
                    resultsCount++;
                  
                } else {
                    links[i].parentElement.style.display = 'none';
                }
            }
  
  
             if (links.length > 0) {
     
 
            currentWriteupUrl = links[0].href;
          

        }
     


   return links;
        }
        function loadWriteupContent(writeupUrl) {
            fetch(writeupUrl)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`Failed to fetch ${writeupUrl}. Status: ${response.status}`);
                    }
                    return response.text();
                })
                .then(data => {
                    // Create a temporary element to parse the HTML content
  
                    var tempElement = document.createElement('div');
                    tempElement.innerHTML = data;
                     content=data
                    // Extract the flag element
                    var flagElement = tempElement.querySelector('.flag');
  
                    // Extract the flag text
                    var flag = flagElement ? flagElement.textContent.trim() : null;
  
                    // Display the flag in the console (for testing)
                    console.log('Flag0:', flag);
            var userInput = document.getElementById('search-box').value;
     
                    // Render the writeup content
                    document.getElementById('writeup-content').innerHTML = renderMarkdown(data);
  
                   
                })
                .catch(error => {
                    console.error('Error fetching or parsing content:', error);
                });

        }
        function loadLinksFromTextFile(file) {
            fetch(file)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`Failed to fetch ${file}. Status: ${response.status}`);
                    }
                    return response.text();
                })
                .then(data => {
                    var links = parseLinksFromText(data);
                 updateSidebar(links);
                })
                .catch(error => {
                    console.error('Error loading links:', error);
                });
        }
  function parseLinksFromText(text) {
            var links = [];
            var lines = text.split('\n');
            for (var i = 0; i < lines.length; i++) {
                var parts = lines[i].split(',');
                if (parts.length === 2) {
                    links.push({ title: parts[0].trim(), url: parts[1].trim() });
                }
            }
            return links;
        }
          function updateSidebar(links) {
            var archiveList = document.getElementById('archive-list');
            var writeupList = document.getElementById('writeup-list');
            
            archiveList.innerHTML = ''; // Clear existing content
            writeupList.innerHTML = ''; // Clear existing content
  
            for (var i = 0; i < links.length; i++) {
                // Add the link to the archive
                var archiveItem = document.createElement('li');
                archiveItem.textContent = links[i].title;
                archiveList.appendChild(archiveItem);
  
                // Add the link to the headings
                var writeupItem = document.createElement('li');
                var link = document.createElement('a');
                link.href = links[i].url;
                if(i==0)  
                   if(endsWith(   link.href ,".md"))
                        link.dataset.content = renderMarkdown(link.herf); 
                       else
                       window.location.href=  link.href ;
                words= links[i].title.split(' ');
                link.textContent =words[0]+" "+words[1] 
                link.title = links[i].title; // Store the full title as a title attribute
                link.classList.add('writeup-link'); // Add the 'writeup-link' class
            
                writeupItem.appendChild(link);
                writeupList.appendChild(writeupItem);
  
                // Load writeup content on click
                link.addEventListener('click', function(event) {
                    event.preventDefault();
                     currentWriteupUrl=this.href;
  
                    if(endsWith( currentWriteupUrl,".md"))
                    loadWriteupContent(this.href); // Pass the full title to loadWriteupContent
                       else
                       window.location.href=this.href;
  var ulElement = document.getElementById("writeup-list");
  
  // Check if the element exists before trying to hide it
  if (ulElement) {
    // Set the display property to "none"
    ulElement.style.display = "none";
  }
                });
            }
  
            // After updating the sidebar, trigger the filterWriteups function
            filterWriteups2();
        }
        function checkFlag() {
  var tempElement = document.createElement('div');
                    tempElement.innerHTML = content;

             var flagElement = tempElement.querySelector('.flag');
  
                    // Extract the flag text
                    var flag = flagElement ? flagElement.textContent.trim() : "fakeflag";
  
            var userInput = document.getElementById('search-box').value;
                                console.log('Flag:'+flag+":"+userInput+":");
  
             if (flag.localeCompare(userInput)==0) {
                       document.getElementById('writeup-content').innerHTML ="flag is correct";
                    } else {
                        document.getElementById('writeup-content').innerHTML ="flag is wrong";
                    }
                    return false;
        }
  
        function renderMarkdown(content) {
            return content
                .replace(/\n/g, '<br>')
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        }
  
        // Attach click event listeners to each writeup link
        function getQueryParamOrDefault(name, defaultValue) {
          const urlParams = new URLSearchParams(window.location.search);
          const value = urlParams.get(name);
          return value !== null ? value : defaultValue;
        }
      function hasQueryParam(name) {
          const urlParams = new URLSearchParams(window.location.search);
          return urlParams.has(name);
        }
      function endsWith(str, suffix) {
          return str.indexOf(suffix, str.length - suffix.length) !== -1;
      }
       function find(event) {
        console.log("Enter key is pressed"+event.keyCode);
      
                  if (event.keyCode == 13) {

             var userInput = document.getElementById('search-box').value;
 if (userInput.includes('{') && userInput.includes('}'))
                  {
var tempElement = document.createElement('div');
data=renderMarkdown(currenturl);
                
                          tempElement.innerHTML = data;
                           content=data
                          // Extract the flag element
                          var flagElement = tempElement.querySelector('.flag');
      
                          // Extract the flag text
                                       var flag = flagElement ? flagElement.textContent.trim() : "fakeflag";
                          console.log('Flag02:', flag,currentflag);
      
                 if (currentflag.localeCompare(userInput)==0) {
document.getElementById('search-box').value="flag is correct"; 
}
else
{
document.getElementById('search-box').value="flag is not correct"; 

}
}
else
{
        window.location.href=  "https://cybersecctf.github.io/blog/?q="+userInput ;
 var links2 = document.getElementsByClassName('writeup-link');

currentWriteupUrl = links2[0].href;
            console.log("current"+currentWriteupUrl);
}

              }
}
function filterWriteups2() {
    var query = document.getElementById('search-box').value.toLowerCase();
    query = getQueryParamOrDefault('q', query);
    var links = document.getElementsByClassName('writeup-link');
    var resultsCount = 0;
    var randomLinks = [];

    // Shuffle the array of links
    var shuffledLinks = Array.from(links).sort(() => 0.5 - Math.random());
       
    for (var i = 0; i < shuffledLinks.length; i++) {
        var title = shuffledLinks[i].textContent.toLowerCase();
        var truncatedTitle = shuffledLinks[i].title.toLowerCase();
        var link = shuffledLinks[i].href;
        var content = shuffledLinks[i].dataset.content.toLowerCase();
        var writeup = "";
        if (endsWith(link, ".md"))
            writeup = renderMarkdown(link);
        if (title.includes(query) || truncatedTitle.includes(query) || link.includes(query) || content.includes(query)) {
            if (resultsCount < 3) {
                console.log("visible" + shuffledLinks[i].href);
                currenturl = shuffledLinks[i].href;
                loadWriteupContent(shuffledLinks[i].href);
                randomLinks.push(shuffledLinks[i]);
                resultsCount++;
            }
            shuffledLinks[i].parentElement.style.display = 'none';
        } else {
            shuffledLinks[i].parentElement.style.display = 'none';
        }
    }

    // Add comment link as the fourth writeup
    var commentLink = document.createElement('a');
    commentLink.href = "https://github.com/cybersecctf/blog/issues/1";
    commentLink.textContent = "Comment here";
    commentLink.className = "writeup-link";
 
    randomLinks.push(commentLink);

    return randomLinks;
}
      function filterWriteups3() {
                  var query = document.getElementById('search-box').value.toLowerCase();
                  query= getQueryParamOrDefault('q', query);
                  var links = document.getElementsByClassName('writeup-link');
             
                  var resultsCount = 0;
     
                  for (var i = 0; i < links.length; i++) {
                      var title = links[i].textContent.toLowerCase();
                      var truncatedTitle = links[i].title.toLowerCase();
                      var link = links[i].href;
                      var content = links[i].dataset.content.toLowerCase();
                     var writeup="";
                   if(endsWith( link,".md"))
                     
                       writeup=renderMarkdown(link);
                      if (title.includes(query) || truncatedTitle.includes(query) || link.includes(query) || content.includes(query)) {
                          links[i].parentElement.style.display = '';
 if(resultsCount==0)
                          {
                            console.log("visible"+links[i].href);    
                               currenturl=links[i].href;
                             loadWriteupContent(links[i].href);

                            }
                          resultsCount++;
                        
                      } else {
                          links[i].parentElement.style.display = 'none';
                      }
                  }
      
      
                   if (links.length > 0) {

                  currentWriteupUrl = links[0].href;
            console.log("current"+currentWriteupUrl);

                 var links2 = document.getElementsByClassName('writeup-link');

currentWriteupUrl = links2[0].href;
            console.log("current"+currentWriteupUrl);
              }
         return links;
              }
              function loadWriteupContent(writeupUrl) {
                  fetch(writeupUrl)
                      .then(response => {
                          if (!response.ok) {
                              throw new Error(`Failed to fetch ${writeupUrl}. Status: ${response.status}`);
                          }
                          return response.text();
                      })
                      .then(data => {
                          // Create a temporary element to parse the HTML content
      
                          var tempElement = document.createElement('div');
                          tempElement.innerHTML = data;
                           content=data
                          // Extract the flag element
                          var flagElement = tempElement.querySelector('.flag');
      
                          // Extract the flag text
                                       var flag = flagElement ? flagElement.textContent.trim() : "fakeflag";
                           currentflag=flag;
                          console.log('Flag01:', flag);
      
                          // Render the writeup content
                          document.getElementById('writeup-content').innerHTML = renderMarkdown(data);
                      
                         
                      })
                      .catch(error => {
                          console.error('Error fetching or parsing content:', error);
                      });
   console.log( document.getElementsByClassName('writeup-link').innerHTML);

              }
              function loadLinksFromTextFile(file) {
                  fetch(file)
                      .then(response => {
                          if (!response.ok) {
                              throw new Error(`Failed to fetch ${file}. Status: ${response.status}`);
                          }
                          return response.text();
                      })
                      .then(data => {
                          var links = parseLinksFromText(data);
                       updateSidebar(links);
                       return links;
                      })
                      .catch(error => {
                          console.error('Error loading links:', error);
                      });
              }
      function parseLinksFromText(text) {
                  var links = [];
                  var lines = text.split('\n');
                  for (var i = 0; i < lines.length; i++) {
                      var parts = lines[i].split(',');
                      if (parts.length === 2) {
                          links.push({ title: parts[0].trim(), url: parts[1].trim() });
                      }
                  }
                  return links;
              }
                function updateSidebar(links) {
                  var archiveList = document.getElementById('archive-list');
                  var writeupList = document.getElementById('writeup-list');
                  
                  archiveList.innerHTML = ''; // Clear existing content
                  writeupList.innerHTML = ''; // Clear existing content
      
                  for (var i = 0; i < links.length; i++) {
                      // Add the link to the archive
                      var archiveItem = document.createElement('li');
                      archiveItem.textContent = links[i].title;
                      archiveList.appendChild(archiveItem);
      
                      // Add the link to the headings
                      var writeupItem = document.createElement('li');
                      var link = document.createElement('a');
   
                      link.href = links[i].url;
                      words= links[i].title.split(' ');
                      link.textContent =words[0]+" "+words[1] 
                      link.title = links[i].title; // Store the full title as a title attribute
                      link.classList.add('writeup-link'); // Add the 'writeup-link' class
                      link.dataset.content = renderMarkdown( link.href); // Placeholder for content, update this dynamically if needed
     
                      writeupItem.appendChild(link);
                      writeupList.appendChild(writeupItem);

      
                      // Load writeup content on click
                      link.addEventListener('click', function(event) {
                          event.preventDefault();
                           currentWriteupUrl=this.href;
      
                          if(endsWith( currentWriteupUrl,".md"))
                          loadWriteupContent(this.href); // Pass the full title to loadWriteupContent
                             else
                             window.location.href=this.href;
        var ulElement = document.getElementById("writeup-list");
      
        // Check if the element exists before trying to hide it
        if (ulElement) {
          // Set the display property to "none"
          ulElement.style.display = "none";
        }
                      });
                  }
       
                  // After updating the sidebar, trigger the filterWriteups function
                  filterWriteups3();
              }
              function checkFlag() {
      var tempElement = document.createElement('div');
                          tempElement.innerHTML = "";
      
                   var flagElement = tempElement.querySelector('.flag');
      
                          // Extract the flag text
                          var flag = flagElement ? flagElement.textContent.trim() : "fakeflag";
      
                  var userInput = document.getElementById('search-box').value;
                             
       
                   if (flag.localeCompare(userInput)==0) {
                              document.getElementById('checkflag').style.display = 'block';return true;
                          } else {
                              document.getElementById('checkflag').style.display = 'none';return false;
                          }
                          return false;
              }
      
              function renderMarkdown(content) {
                  return content
                      .replace(/\n/g, '<br>')
                      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
              }
      
        
 

        
               
 
 
