import { LoginByToken,LoginChecked,GetDataByToken,SendDataByToken} from "./moudle.js";

LoginChecked()
let username_kinds_info = document.querySelector("#username_kinds_info")
let tag_people = document.querySelector("#tag_people")
let mater = ["我的电影主页","我想看的电影","我看过的电影"]
let username = document.querySelector("#username")
for(let i = 0; i < tag_people.children.length;i++){
    tag_people.children[i].addEventListener("click",() => {
        for(let j = 0; j < username_kinds_info.children.length;j++){
            username_kinds_info.children[j].style.display = "none"
        }
        username_kinds_info.children[i].style.display = "block"
        username.textContent = mater[i]
    })
}

let setintobox = document.querySelector("#setintobox")
let userintroduction = document.querySelector("#userintroduction")
userintroduction.children[1].addEventListener("click",(event) => {
    userintroduction.children[0].style.display = "none"
    setintobox.children[0].style.display = "inline-block"
    setintobox.children[1].textContent = "提交"
    event.stopPropagation()
})
setintobox.children[1].addEventListener("click",(event) => {
    if(setintobox.children[0].value != ""){
        SendDataByToken("/user/updateintroduction","introduction="+setintobox.children[0].value)
        setInterval(() => {
            location.reload()
        },500)
    }
})
window.addEventListener("click",()=> {
    userintroduction.children[0].style.display = "inline-block"
    setintobox.children[0].style.display = "none"
    setintobox.children[0].value = ""
    setintobox.children[1].textContent = "修改简介"
})
async function PeopleGetData(){
    let userData =await LoginByToken()
    let userimg = document.querySelector("#userimg")
    console.log(userData)
    userintroduction.children[0].textContent = userData.introduction
    userimg.src = userData.picture_url
    let watchFilms =await GetDataByToken("/user/getwant")
    let watchedFilms =await GetDataByToken("/user/getwatched")
    
}
PeopleGetData()