function showHeadLines(){
    var headlinesURL = "https://newsapi.org/v2/top-headlines" +
        "?" +
        "country=us" +
        "&" +
        "category=entertainment" +
        "&" +
        "apiKey=7efd25e409934d40a079a045704b0b94";

    var req = new XMLHttpRequest();
    req.open("GET", headlinesURL, true);

    req.send();
    document.getElementById('ajax-wait').style.display = 'block';
}

window.addEventListener('load', showHeadLines);