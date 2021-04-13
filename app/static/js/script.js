function ajaxGet(url, callback) {
    var req = new XMLHttpRequest();
    req.open("GET", url);
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            callback(req.responseText);
        } else {
            const message = "Adresse introuvable, reessayer une nouvelle adresse"
            alert(message);
        }
    });
    req.addEventListener("error", function () {
        const message = "Adresse introuvable, reessayer une nouvelle adresse"
        alert(message);
    });
    req.send(null);
}

function ajaxPost(url, data, callback, isJson){
    var req = new XMLHttpRequest();
    req.open("POST", url);
    req.addEventListener("load", function (){
        if (req.status >= 200 && req.status < 400) {
            callback(req.responseText);
        } else {
            const message = "Adresse introuvable, reessayer une nouvelle adresse"
            alert(message);
        }
    });
    req.addEventListener("error", function () {
        const message = "Adresse introuvable, reessayer une nouvelle adresse"
        alert(message);
    });
    if (isJson) {
        req.setRequestHeader("Content-Type", "application/json");
        data = JSON.stringify(data);
    }
    req.send(data);
}

