import { LoginByToken,LoginChecked,MakeUrl,PostData,GetData,GetDataByToken, SendDataByToken} from "./moudle.js";
LoginChecked()
let box05 = document.querySelectorAll(".box05")
let useornoIMG = document.querySelectorAll(".useornoIMG")

for(let i = 0; i <box05.length;i++){
    box05[i].addEventListener("mouseover",() => {
        useornoIMG[i].style.top = "-1.2rem"

    })
    box05[i].addEventListener("mouseout",() => {
        useornoIMG[i].style.top = "0.45rem"
    })
}
let film_id = window.location.search.substr(1)
async function tedd(){
    let discussionRequest =await PostData("/longpost/getlongpostbyfilmid",film_id)
    let discussionData = discussionRequest.data
    let n = discussionData.length-1
    console.log(discussionData)
    let userimg = document.querySelector("#userimg")
    let userinfoRequest = await GetDataByToken("/user/getuserinfo")
    let userinfo = userinfoRequest.data
    userimg.src = userinfo.picture_url
    let bottom_userimg = document.querySelector("#bottom_userimg")
    bottom_userimg.src = userinfo.picture_url
    console.log(userinfo)
    let username = document.querySelector("#username")
    username.textContent = userinfo.username
    let comment_title = document.querySelector("#comment_title")
    comment_title.textContent = discussionData[n].title
    let comment_info = document.querySelector("#comment_info")
    comment_info.textContent = discussionData[n].txt
    let time = document.querySelector("#time")
    time.textContent = discussionData[n].post_time.substr(0,19)
    let filmdatarequest =await PostData("/film/getfilm",film_id)
    let filmdata = filmdatarequest.data
    let filmname = document.querySelector("#filmname")
    filmname.addEventListener("click",() => {
        window.location.href = MakeUrl("/subject.html?film_id="+(parseInt(film_id.substr(8))-1))
    })
    filmname.textContent = filmdata.name
    let useinfo = document.querySelector("#useinfo")
    useinfo.children[0].textContent = discussionData[n].likes
    let nouseinfo =document.querySelector("#nouseinfo")
    nouseinfo.children[0].textContent = discussionData[n].dislikes
    usefull.addEventListener("click",async() => {
        SendDataByToken("/longpost/likelongpost",discussionData[n].post_id)
        location.reload()
    })
    nouseinfo.addEventListener("click",async () => {
        let re =await SendDataByToken("/longpost/dislikelongpost",discussionData[n].post_id)
        location.reload()
    })
    let inputre = document.querySelector("#inputre")
    let submit = document.querySelector("#submit")
    submit.addEventListener("click",async () => {
        if(inputre.value != ""){
            let lpcommentRequest =await SendDataByToken("/lpcomment/addlpcomment","post_id="+discussionData[n].post_id+"&&txt="+inputre.value)
            let lpcomment = lpcommentRequest.data
            window.location.reload()
        }
    })
    let getLpcommetnRequest = await PostData("/lpcomment/getlpcomment","post_id="+discussionData[n].post_id)
    let getLpcomment = getLpcommetnRequest.data
    console.log(getLpcomment)
    let response_box = document.querySelector("#response_box")
    if(getLpcomment){
        for(let i = 0; i < getLpcomment.length;i++){
            let tempuser_response = document.createElement("div")
            tempuser_response.innerHTML = "<img src='' classers='u_responseimg' class='img' alt=''><div class='user_response_right'><div class='user_iiiii'><div class='user_response_name'>null</div><div class='user_response_time'>null</div></div><div class='user_response_info'>null</div></div>"
            tempuser_response.classList.add("user_response")
            tempuser_response.children[1].children[0].children[0].textContent = getLpcomment[i].username
            tempuser_response.children[1].children[0].children[1].textContent = getLpcomment[i].comment_time.substr(0,19)
            tempuser_response.children[1].children[1].textContent = getLpcomment[i].txt
            response_box.append(tempuser_response)
        }
    }
}
tedd()