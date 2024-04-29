const btn = document.getElementById("translate");
btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "translating.....";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/translate?url=" + url, true);
        xhr.onload = function() {
            var text = xhr.responseText;
            const p = document.getElementById("output1");
            p.innerHTML = text;
            btn.disabled = false;
            btn.innerHTML = "translate in hindi";
        }
        xhr.send();
    });
});