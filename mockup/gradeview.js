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
// AUTO GENERATED
folderContents["johnsmith"] = [];
folderContents["janesmith"] = [];

// HTML, JS, other files
folderContents["johnsmith"].push("./john_smith/html2.html");

// HTML, JS, other files
folderContents["janesmith"].push("./jane_smith/html3.html");
folderContents["janesmith"].push("./jane_smith/js1.js");