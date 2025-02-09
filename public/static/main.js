


var sendButton = document.getElementById("input_button");
var text_input = document.getElementById("text_input");

function CreatePopupbox(txt, duration){
    const popup_box = document.getElementById("popup-box");
    popup_box.classList.add("visible");
    popup_box.textContent = txt;
    setTimeout(() => {
        popup_box.classList.remove("visible");
    }, duration);
}

sendButton.addEventListener('click', function() {
    if(text_input.value === ""){
        CreatePopupbox("输入文本不能为空", 1500);
        return;
    }

    this.style.backgroundImage = 'url("static/img/stop.png")';

    text_input.value = "";
    text_input.disabled = true;
    text_input.style.cursor = "not-allowed";
});