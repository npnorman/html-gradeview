# Nicholas Norman March 2026
# Use python to host the app and allows JS to fetch

import http.server
import socketserver
import webbrowser
import os

# open TKinter

# ask for root directory (for input files)
# generate gradeview button

# Generate files
def generate_files(inputURL):
    # overwrite current gradeview.html file
    gradeviewFile = open("gradeview.html", "w")
    
    # basic setup
    currentHTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gradeview</title>
    <link rel="stylesheet" href="gradeview.css">
</head>
<body>
    <div>

    </div>
    <div class="columns">
        <div class="folders">
            <!-- Folders -->
            <div>
                <h1>Student Folders</h1>
            </div>
            <div id="folders" class="folders">
"""

    folders = os.listdir(inputURL)

    # for each subfolder (student names)
    for folder in folders:
        # add folder name to student folders list
        # add folder title
        # add folder id
        currentHTML += f"""
                <div id="{folder}" title="{folder}" class="subfolder">
                    <img class="folder-icon" src="open-folder-icon.png">
                    <span>{folder}/</span>
                </div> 
        """


    currentHTML += """
            </div>
        </div>
        <div class="html">
            <!-- HTML -->
            <div class="html-metadata">
                <span title="title" id="html-title">Select a folder to load</span>
            </div>
            <iframe id="html-iframe" src=""></iframe>
        </div>
        <div class="codeWindow">
            <!-- JS/CSS -->
            <div class="buttons">
                <select id="code-url">
                </select>
            </div>
            <div class="js">
                <pre id="js-code">Select a file to load</pre>
            </div>
        </div>
    </div>

    <script src="gradeview.js"></script>
</body>
</html>
"""

    gradeviewFile.write(currentHTML)
    
    gradeviewFile.close()
    
    jsFile = open("gradeview.js", "w")

    currentJS = """
// Nicholas Norman March 2026

// load contents from JS file into HTML

jsCodeWindow = document.getElementById("js-code");
htmlIframe = document.getElementById("html-iframe");
htmlTitle = document.getElementById("html-title");
codeSelector = document.getElementById("code-url");

function getIframeTitle() {
    htmlTitle.textContent = htmlIframe.contentDocument.title;
    htmlTitle.title = htmlIframe.contentDocument.title;
    htmlIframe.removeEventListener('load', getIframeTitle);
}

function loadHTML(URL) {
    htmlIframe.src = URL;
    htmlIframe.addEventListener('load', getIframeTitle);
}

async function loadFile(codeWindow, URL) {

    let response = await fetch(URL);
    let codeText = "";

    if (response.ok) {
        codeText = await response.text();
        codeWindow.textContent = codeText;
    } else {
        console.log("Error reading file");
        codeWindow.textContent = "Error reading file";
    }
    
}

function loadSelect(files) {
    // clear all options
    codeSelector.innerHTML = "";

    // for each file
    for (let i = 0; i < files.length; i++) {
        // make a new option
        let newOption = document.createElement("option");
        newOption.text = files[i];
        newOption.value = files[i];

        codeSelector.appendChild(newOption);
    }
    
    // set default option to file at [1]
    if (files.length >= 2) {
        codeSelector.value = files[1];
    } else {
        codeSelector.value = files[0];
    }
}

function loadAllFiles(id) {

    //load code window and iframe
    loadHTML(folderContents[id][0]);

    if (folderContents[id].length >= 2) {
        loadFile(jsCodeWindow, folderContents[id][1]);
    } else {
        loadFile(jsCodeWindow, folderContents[id][0]);
    }

    //load selector
    loadSelect(folderContents[id]);
}

// folders
folders = document.getElementById("folders");

folders.addEventListener('click', function (e) {

    //remove all selected classes
    for (let i = 0; i < folders.children.length; i++) {
        folders.children[i].classList.remove("selected");
    }

    let target = e.target;
    let cssTarget = target;
    let isCorrectElementSelected = false;

    if (target.tagName == "SPAN" || target.tagName == "IMG") {
        //get parent
        cssTarget = target.parentElement;
        isCorrectElementSelected = true;

    } else if (target.tagName == "DIV") {
        //check class
        if (target.classList.contains("subfolder")) {
            //set selected class
            isCorrectElementSelected = true;
        }
    }

    if (isCorrectElementSelected) {
        cssTarget.classList.add("selected");

        //load proper files
        loadAllFiles(cssTarget.id);
    }
});

codeSelector.addEventListener('change', function () {
    loadFile(jsCodeWindow, codeSelector.value);
});

folderContents = {};
"""
    
    # for each file
    for folder in folders:
        # get a list of all files
        folderPath = os.path.join(inputURL, folder)
        currentJS += f"folderContents['{folder}'] = [];\n"
        
        files = []
        for root, dirs, filenames in os.walk(folderPath):
            for filename in filenames:
                files.append(os.path.join(folderPath, filename))
            
        htmlFiles = ""
        otherFiles = ""
        for file in files:
            
            currentFile = file
            currentFile = currentFile.replace("\\","/")
            
            if (".html" in currentFile):
                htmlFiles += f"folderContents['{folder}'].push('{currentFile}');\n"
            else:
                otherFiles += f"folderContents['{folder}'].push('{currentFile}');\n"
            # add first html file to bottom of JS file
            # add other files below
        
        currentJS += htmlFiles + otherFiles
        
    jsFile.write(currentJS)
    jsFile.close()

def setupServer():
    # Serve the file
    PORT = 8080
    os.chdir("./")

    webbrowser.open(f"http://localhost:{PORT}/gradeview.html")

    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()