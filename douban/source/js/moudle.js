async function PostData(api, data) {
    let url = "http://39.106.81.229:9920" + api;
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: data,
    });
    return response.json();
}
async function GetData(api,data){
    let url = "http://39.106.81.229:9920" + api;
    const response = await fetch(url, {
        method: "GET",
        mode: "cors",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: data,
    });
    return response.json();
}

async function GetDataByToken(api) {
    let token = "Bearer " + localStorage.getItem("token")
    let url = "http://39.106.81.229:9920" + api
    const response = await fetch(url, {
        method: "GET",
        headers: {
            "Authorization": token,
        }
    })
    return response.json();
}
async function PostDataByToken(api) {
    let token = "Bearer " + localStorage.getItem("token")
    let url = "http://39.106.81.229:9920" + api
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Authorization": token,
        }
    })
    return response.json();
}
async function SendDataByToken(api,data){
    let token = "Bearer " + localStorage.getItem("token")
    let url = "http://39.106.81.229:9920" + api
    const response = await fetch(url, {
        method: "PUT",
        mode: "cors",
        headers: {
            "Authorization": token,
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: data,
    })
    return response.json();
}
function Click(obj, class_name, later) {
    for (let i = 0; i < obj.length; i++) {
        obj[0].classList.add(class_name);
        obj[i].addEventListener("click", () => {
            for (let j = 0; j < obj.length; j++) {
                obj[j].classList.remove(class_name);
            }
            obj[i].classList.add(class_name);
            later(i);
        })
    }
}
function FormToString(form) {
    let result = ""
    form = new FormData(form);
    for (let pair of form.entries()) {
        result = result + pair[0] + "=" + pair[1] + "&"
    }
    result = result.substr(0, result.length - 1);
    return result;
}

function MakeUrl(path) {
    let oldUrl = window.location.href
    let indexof = oldUrl.lastIndexOf("/")
    let newurl = oldUrl.substr(0, indexof) + path
    return newurl
}


async function LoginByToken() {
    let response = await GetDataByToken("/user/getuserinfo")
    if (response.info == "无效的Token") {
        localStorage.removeItem("token")
        return false
    } else {
        return response.data
    }
}

async function LoginChecked() {
    let downl = document.querySelector("#download");
    function show(x) {
        downl.style.display = "block";
    }
    function show_out(x) {
        downl.style.display = "none";
    }
    let username_a = document.querySelector("#username_a")
    let loginafterhover = document.querySelector("#loginafterhover")
    loginafterhover.children[0].addEventListener("click",() => {
        window.location.href = MakeUrl("/people.html")
    })
    loginafterhover.children[1].addEventListener("click",() => {
        localStorage.removeItem("token")
        location.reload()
    })
    username_a.addEventListener("click", (event) => {
        loginafterhover.style.display = "block"
        event.stopPropagation()
    })
    document.addEventListener("click", () => {
        loginafterhover.style.display = "none"
    })
    let nav_right = document.querySelector("#nav_right")
    nav_right.children[1].addEventListener("click",() =>{
        window.location.href = MakeUrl("/login.html")
    })
    let userdata =await LoginByToken()
    if (userdata) {
        for (let i = 0; i < nav_right.children.length; i++) {
            nav_right.children[i].style.display = "none"
        }
        username_a.textContent = userdata.username + "的账号"
        nav_right.lastElementChild.style.display = "block"
    }
    let nav_3 = document.querySelector("#nav_3")
    nav_3.children[3].href = MakeUrl("/chart.html")
    nav_3.children[4].href = MakeUrl("/tag.html?limit=20")
    let search = document.querySelector("#search")
    search.children[0].href = MakeUrl("/index.html")
    let search_go2 = document.querySelector("#search_go2")
    let search_go1 = document.querySelector("#search_go1")
    search_go2.addEventListener("click",() => {
        if(search_go1.value != ""){
            window.location.href = MakeUrl("/search.html?name="+search_go1.value)
        }
    })
}

async function submitWantOrWatched(){
    let jdsa = document.querySelectorAll(".jdsa")
    let save = document.querySelector("#save")
    let c_stars1 = document.querySelectorAll(".c_stars1")
    let makerequestData = ""
    save.children[0].addEventListener("click",async() => {
        if(jdsa[0].children[0].checked){
            makerequestData ="want=1"
        }else if(jdsa[1].children[0].checked){
            makerequestData = "watched=1"
        }
        let comment_tag = document.querySelector("#comment_tag")
        makerequestData += "&&tags="+comment_tag.value
        let short_comment = document.querySelector("#short_comment")
        let score = 0.0;
        makerequestData += "&&txt="+short_comment.value
        for(let i = 0; i < c_stars1.length;i++){
            let temp_a  = c_stars1[i].src.split("/")
            if(temp_a[temp_a.length-1] == "staryellow.png"){
                score +=2.0
            }
        }

        makerequestData += "&&score="+score + ".0"
        let film_id = window.location.search.substr(9)
        makerequestData += "&&film_id="+film_id
        console.log(makerequestData)
        let wanRequest =await SendDataByToken("/shortpost/addshortpost",makerequestData)
        makerequestData = ""
        if(wanRequest.status){
            document.location.reload()
        }
    })
}

export { PostData, Click, FormToString, MakeUrl, LoginByToken,LoginChecked,GetDataByToken,GetData,SendDataByToken,submitWantOrWatched,PostDataByToken };