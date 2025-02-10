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

function addMessage(IsUser, txt){
    const msg_container = document.getElementById("message_list");
    if(IsUser === true) {
        const msg_ele = `
        <div class="user_msg">
            <p class="user_msg_content">${txt}</p>
            <img src="static/img/stop.png" alt="User Avatar" class="avatar">
        </div>
        `
        msg_container.innerHTML += msg_ele;
    }
    else {
        const msg_ele =`
        <div class="ai_msg">
            <img src="static/img/send-message.png" alt="AI Avatar" class="avatar">
            <p class="ai_msg_content">${txt}</p>
        </div>
        `
        msg_container.innerHTML += msg_ele;
    }
}

sendButton.addEventListener('click', function() {
    if(text_input.value === "") {
        CreatePopupbox("输入文本不能为空", 1500);
        return;
    }

    addMessage(true, text_input.value)
    
    addMessage(false, "请稍后再试")
    
    text_input.value = "";

    this.style.backgroundImage = 'url("static/img/stop.png")';
    text_input.disabled = true;
    text_input.style.cursor = "not-allowed";
});