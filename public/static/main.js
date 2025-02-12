var sendButton = document.getElementById("input_button");
var text_input = document.getElementById("text_input");

class INFO{
    constructor(key = "", nam = "", url = "", tool = "", sys = "", func = "", par = ""){
        this.api_key = key;
        this.model_name = nam;
        this.model_url = url;
        this.tool_choice = tool;
        this.sys_prompt = sys;
        this.func_desp = func;
        this.func_para_desp = par;
    }
};

const UserInfo = new INFO()

function CreatePopupbox(txt, duration) {
    const popup_box = document.getElementById("popup-box");
    popup_box.classList.add("visible");
    popup_box.textContent = txt;
    setTimeout(() => {
        popup_box.classList.remove("visible");
    }, duration);
}

function ListaddMessage(IsUser, txt) {
    const msg_container = document.getElementById("message_list");
    if(IsUser === true) {
        const msg_ele = `
        <div class="user_msg">
            <p class="user_msg_content">${txt}</p>
            <img src="static/img/person.png" alt="User Avatar" class="avatar">
        </div>
        `
        msg_container.innerHTML += msg_ele;
    }
    else {
        const msg_ele = `
        <div class="ai_msg">
            <img src="static/img/search.png" alt="AI Avatar" class="ai_avatar">
            <p class="ai_msg_content">${txt}</p>
        </div>
        `
        msg_container.innerHTML += msg_ele;
    }
}

function SendMessage(txt) {
    fetch("/chat", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"msg": txt})
    })
    .then(response => response.json())
    .then(data => {
        ListaddMessage(false, data.msg)

        var MsgListDiv = document.getElementById("message_list");
        MsgListDiv.scrollTop = MsgListDiv.scrollHeight - MsgListDiv.clientHeight;

        sendButton.style.backgroundImage = 'url("static/img/send-message.png")';
        text_input.disabled = false;
        sendButton.disabled = false;
    })
    .catch((error) => {
        ListaddMessage(false, `Error: ${error}. Please check if the backend is enabled`)

        var MsgListDiv = document.getElementById("message_list");
        MsgListDiv.scrollTop = MsgListDiv.scrollHeight - MsgListDiv.clientHeight;

        sendButton.style.backgroundImage = 'url("static/img/send-message.png")';
        text_input.disabled = false;
        sendButton.disabled = false;
        console.log(error);
    })
}

window.onload = function() {

    fetch("/init",{
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        UserInfo.api_key = data.key;
        UserInfo.model_name = data.nam;
        UserInfo.model_url = data.url;
        UserInfo.tool_choice = data.tool;
        UserInfo.sys_prompt = data.sys;
        UserInfo.func_desp = data.func;
        UserInfo.func_para_desp = data.par;

        var console_table = document.getElementById("console_table");
        console_table.innerHTML += `
        <table class="info_table">
            <thead>
                <tr>
                    <th>定义</th>
                    <th>说明</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>API key</td>
                    <td>${UserInfo.api_key}</td>
                </tr>
                <tr>
                    <td>模型名称</td>
                    <td>${UserInfo.model_name}</td>
                </tr>
                <tr>
                    <td>地址</td>
                    <td>${UserInfo.model_url}</td>
                </tr>
                <tr>
                    <td>函数调用</td>
                    <td>${UserInfo.tool_choice}</td>
                </tr>
                <tr>
                    <td>系统prompt</td>
                    <td>${UserInfo.sys_prompt}</td>
                </tr>
                <tr>
                    <td>函数描述</td>
                    <td>${UserInfo.func_desp}</td>
                </tr>
                <tr>
                    <td>URL</td>
                    <td>${UserInfo.func_para_desp}</td>
                </tr>
            </tbody>
        </table>
        `
    })
    .catch((error) => {
        console.log(error)
        console_table.innerHTML += `
        <div style = "word-wrap: break-word; overflow-wrap: break-word; ">
        ERROR: ${error}
        </div>
        `
    })


    sendButton.addEventListener('click', function() {
        if(text_input.value === "") {
            CreatePopupbox("输入文本不能为空", 1500);
            return;
        }
    
        ListaddMessage(true, text_input.value);
    
        var MsgListDiv = document.getElementById("message_list");
        MsgListDiv.scrollTop = MsgListDiv.scrollHeight - MsgListDiv.clientHeight;
    
    
        SendMessage(text_input.value);
        
        this.style.backgroundImage = 'url("static/img/stop.png")';
        this.disabled = true;
    
        text_input.value = "";
        text_input.disabled = true;
    });
}
