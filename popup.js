const btn = document.getElementById("summarise");
const btn1 = document.getElementById("translate");
const btn2 = document.getElementById("select").value;
btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "Summarising...";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/summary?url=" + url, true);
        xhr.onload = function() {
            var text = xhr.responseText;
            const p = document.getElementById("output");
            p.innerHTML = text;
            btn.disabled = false;
            btn.innerHTML = "Summarise";
        }
        xhr.send();
    });
});

// const btn1 = document.getElementById("translate");
if (btn2 == 'Hindi'){
btn1.addEventListener("click", function() {
    btn1.disabled = true;
    btn1.innerHTML = "translating.....";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/translate?url=" + url, true);
        xhr.onload = function() {
            var text = xhr.responseText;
            const p = document.getElementById("output1");
            p.innerHTML = text;
            btn1.disabled = false;
            btn1.innerHTML = "translate";
        }
        xhr.send();
    });
  
});
} 
else if(btn2 == 'Gujarati'){
    btn1.addEventListener("click", function() {
        btn1.disabled = true;
        btn1.innerHTML = "translating.....";
        chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
            var url = tabs[0].url;
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "http://127.0.0.1:5000/translate1?url=" + url, true);
            xhr.onload = function() {
                var text = xhr.responseText;
                const p = document.getElementById("output1");
                p.innerHTML = text;
                btn1.disabled = false;
                btn1.innerHTML = "translate";
            }
            xhr.send();
        });
      
    });
}
else if(btn2 == 'Tamil'){
    btn1.addEventListener("click", function() {
        btn1.disabled = true;
        btn1.innerHTML = "translating.....";
        chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
            var url = tabs[0].url;
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "http://127.0.0.1:5000/translate2?url=" + url, true);
            xhr.onload = function() {
                var text = xhr.responseText;
                const p = document.getElementById("output1");
                p.innerHTML = text;
                btn1.disabled = false;
                btn1.innerHTML = "translate";
            }
            xhr.send();
        });
      
    });
}
else if(btn2 == 'Telgu'){
    btn1.addEventListener("click", function() {
        btn1.disabled = true;
        btn1.innerHTML = "translating.....";
        chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
            var url = tabs[0].url;
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "http://127.0.0.1:5000/translate3?url=" + url, true);
            xhr.onload = function() {
                var text = xhr.responseText;
                const p = document.getElementById("output1");
                p.innerHTML = text;
                btn1.disabled = false;
                btn1.innerHTML = "translate";
            }
            xhr.send();
        });
      
    });
}
else{
    btn1.addEventListener("click", function() {
        btn1.disabled = true;
        btn1.innerHTML = "translating.....";
        chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
            var url = tabs[0].url;
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "http://127.0.0.1:5000/translate4?url=" + url, true);
            xhr.onload = function() {
                var text = xhr.responseText;
                const p = document.getElementById("output1");
                p.innerHTML = text;
                btn1.disabled = false;
                btn1.innerHTML = "translate";
            }
            xhr.send();
        });
      
    });
}