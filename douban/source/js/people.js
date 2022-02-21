import { LoginByToken,LoginChecked,GetDataByToken,SendDataByToken, PostData, MakeUrl, GetData} from "./moudle.js";

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
    userintroduction.children[0].textContent = userData.introduction
    userimg.src = userData.picture_url
    let getDataRequest01 = await GetDataByToken("/shortpost/getshortpostsofuser")
    let getData01 = getDataRequest01.data
    let want_films = document.querySelector("#want_films")
    let see_films = document.querySelector("#see_films")
    let username_want = document.querySelector("#username_want")
    let username_see = document.querySelector("#username_see")
    let pos_numbers = document.querySelectorAll(".pos_numbers")
    for(let i = 0; i <getData01.length;i++){
        let want_n = 0;
        let see_n = 0;
        if(getData01[i].want == 1){
            want_n++;
            pos_numbers[0].textContent = "共"+ want_n +"部"
            console.log(getData01[i].film_id)
            let getfilmrequest = await PostData("/film/getfilm","film_id="+((parseInt(getData01[i].film_id))+1))
            let getfilm = getfilmrequest.data
            let tempimg = document.createElement("IMG")
            tempimg.addEventListener("click",() => {
                window.location.href = MakeUrl("/subject.html?film_id="+(parseInt(getData01[i].film_id)))
            })
            tempimg.src = getfilm.poster_url
            tempimg.classList.add("main_film_img")
            want_films.append(tempimg)
            let temp_comment_box = document.createElement("div")
            temp_comment_box.innerHTML = "<img src='' class='comment_film_imgb' alt=''><div class='film_right_info'><div class='film_title_comment'><span>null</span></div><div class='film_more_information'><span>null</span></div><div class='my_comment'><div class='time'>null</div><div class='my_tag'>标签:<span>null</span></div></div><span class='my_comment_content'>null</span></div>"
            temp_comment_box.children[0].src = getfilm.poster_url
            temp_comment_box.children[1].children[0].children[0].textContent = getfilm.name+" / "+getfilm.other_name
            temp_comment_box.children[1].children[1].children[0].textContent = getfilm.release_time +" / "+getfilm.directer+" / "+getfilm.screenwriter + " / "+getfilm.length + " / "+getfilm.type + " / " + getfilm.language
            temp_comment_box.children[1].children[2].children[0].textContent = getData01[i].post_time.substr(0,10)
            temp_comment_box.children[1].children[2].children[1].children[0].textContent = getData01[i].tags
            temp_comment_box.children[1].children[3].textContent = getData01[i].txt
            temp_comment_box.classList.add("comment_box")
            temp_comment_box.children[0].addEventListener("click",() => {
                window.location.href = MakeUrl("/subject.html?film_id="+(parseInt(getData01[i].film_id)))
            })
            temp_comment_box.children[1].children[0].children[0].addEventListener("click",() => {
                window.location.href = MakeUrl("/subject.html?film_id="+(parseInt(getData01[i].film_id)))
            })
            
            username_want.append(temp_comment_box)
        }else{
            see_n++;
            pos_numbers[1].textContent = "共"+ see_n + "部"
            let getfilmrequest = await PostData("/film/getfilm","film_id="+((parseInt(getData01[i].film_id))+1))
            let getfilm = getfilmrequest.data
            let tempimg = document.createElement("IMG")
            tempimg.src = getfilm.poster_url
            tempimg.classList.add("main_film_img")
            see_films.append(tempimg)
            let temp_comment_box = document.createElement("div")
            temp_comment_box.innerHTML = "<img src='' class='comment_film_imgb' alt=''><div class='film_right_info'><div class='film_title_comment'><span>null</span></div><div class='film_more_information'><span>null</span></div><div class='my_comment'><div class='time'>null</div><div class='my_tag'>标签:<span>null</span></div></div><span class='my_comment_content'>null</span></div>"
            temp_comment_box.children[0].src = getfilm.poster_url
            temp_comment_box.children[1].children[0].children[0].textContent = getfilm.name+" / "+getfilm.other_name
            temp_comment_box.children[1].children[1].children[0].textContent = getfilm.release_time +" / "+getfilm.directer+" / "+getfilm.screenwriter + " / "+getfilm.length + " / "+getfilm.type + " / " + getfilm.language
            temp_comment_box.children[1].children[2].children[0].textContent = getData01[i].post_time.substr(0,10)
            temp_comment_box.children[1].children[2].children[1].children[0].textContent = getData01[i].tags
            temp_comment_box.children[1].children[3].textContent = getData01[i].txt
            temp_comment_box.classList.add("comment_box")
            temp_comment_box.children[0].addEventListener("click",() => {
                window.location.href = MakeUrl("/subject.html?film_id="+(parseInt(getData01[i].film_id)))
            })
            temp_comment_box.children[1].children[0].children[0].addEventListener("click",() => {
                window.location.href = MakeUrl("/subject.html?film_id="+(parseInt(getData01[i].film_id)))
            })
            
            username_see.append(temp_comment_box)
        }
    }
    let get_film_commentrequest = await GetDataByToken("/longpost/longpostsofuser")
    let get_film_comment = get_film_commentrequest.data
    pos_numbers[2].textContent = "共"+get_film_comment.length + "条"
    console.log(get_film_comment)
    let my_film_comment = document.querySelector("#my_film_comment")
    for(let i = 0; i < get_film_comment.length;i++){
        let temp_film_comment_box = document.createElement("div")
        temp_film_comment_box.classList.add("film_comment_box")
        temp_film_comment_box.innerHTML = "<img src='' alt='' class='film_img'><div class='film_right_part_box'><div class='my_comment_title'>null</div><div class='my_co_info'><span>null</span><span>评论:</span><span>null</span></div><div class='my_comment_more_info'>null</div></div>"
        my_film_comment.append(temp_film_comment_box)
        let getfilmrequesttemp = await PostData("/film/getfilm","film_id="+get_film_comment[i].film_id)
        let getfilmtemp = getfilmrequesttemp.data
        temp_film_comment_box.children[0].src = getfilmtemp.poster_url
        temp_film_comment_box.children[1].children[0].textContent = get_film_comment[i].title
        temp_film_comment_box.children[1].children[1].children[0].textContent = get_film_comment[i].username
        temp_film_comment_box.children[1].children[1].children[2].textContent = getfilmtemp.name
        temp_film_comment_box.children[1].children[2].textContent = get_film_comment[i].txt
    }
    let myfilmpostRe = await GetData("/post/lookpost")
    let myfilmpost = myfilmpostRe.data
    console.log(myfilmpost)

}
let my_comment_more_info = document.querySelectorAll(".my_comment_more_info")
for(let i = 0; i < my_comment_more_info.length;i++){
    if(my_comment_more_info[i].textContent.length >115){
        my_comment_more_info[i].textContent = my_comment_more_info[i].textContent.substr(0,114) +"..."
    }
}

PeopleGetData()