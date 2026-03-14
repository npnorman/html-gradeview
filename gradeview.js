// Nicholas Norman March 2026

// load contents from JS file into HTML

jsCodeWindow = document.getElementById("js-code");
htmlCodeWindow = document.getElementById("html-code");
htmlIframe = document.getElementById("html-iframe");
filename = document.getElementById("filename");
htmlTitle = document.getElementById("html-title");

function getIframeTitle() {
    htmlTitle.textContent = htmlIframe.contentDocument.title;
    htmlTitle.title = htmlIframe.contentDocument.title;
    htmlIframe.removeEventListener('load', getIframeTitle);
}

function loadHTML(URL) {
    filename.textContent = URL;
    filename.title = URL;
    
    htmlIframe.addEventListener('load', getIframeTitle);
}

async function loadFile(codeWindow, URL) {

    let response = await fetch(URL);
    let codeText = "";

    if (response.ok) {
        codeText = await response.text();
    } else {
        console.log("Error reading file");
    }

    codeWindow.textContent = codeText;
}

loadFile(jsCodeWindow, "./example_html/js1.js");
loadFile(htmlCodeWindow, "./example_html/html1.html");
loadHTML("./example_html/html1.html");

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
    }
});