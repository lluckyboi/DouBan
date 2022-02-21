import { LoginByToken, LoginChecked, MakeUrl, PostData } from "./moudle.js";

LoginChecked()
let share_to = document.querySelector("#share_to")
let share_box = document.querySelector("#share_box")
share_to.addEventListener("mousedown", () => {
    share_to.style.backgroundColor = "rgb(255,153,51)"
})
share_to.addEventListener("mouseup", () => {
    share_to.style.backgroundColor = ""
})
let upordown = document.querySelector("#upordown")
let share_com = document.querySelector("#share_com")
share_com.style.display = "none"
{
    let flag = 0
    share_to.addEventListener("click", (event) => {
        if (flag == 0) {
            share_box.classList.add("share_box_border")
            upordown.textContent = "▼"
            share_com.style.display = "block"
            event.stopPropagation()
            flag = 1
        } else {
            share_box.classList.remove("share_box_border")
            share_com.style.display = "none"
            upordown.textContent = "▲"
            flag = 0
        }
    })
}

document.onclick = function () {
    share_box.classList.remove("share_box_border")
    share_com.style.display = "none"
    upordown.textContent = "▲"
}
let actor_id = window.location.search.substr(1)
console.log(actor_id)
async function getActorData() {
    let actorData = await PostData("/actor/searchactor", actor_id)
    let actorMoreData = actorData.data
    let actorname = document.querySelector("#actorname")
    actorname.textContent = actorMoreData.name
    let actorimg = document.querySelector("#actorimg")
    actorimg.src = actorMoreData.poster_url
    let actorrightinfo = document.querySelector("#actorrightinfo")
    actorrightinfo.children[0].children[0].textContent = actorMoreData.sex
    actorrightinfo.children[1].children[0].textContent = actorMoreData.mainrole
    let actorbriefinfo = document.querySelector("#actorbriefinfo")
    actorbriefinfo.textContent = actorMoreData.introduction
    if (actorbriefinfo.textContent.length > 276) {
        let tempcontent = actorbriefinfo.textContent
        actorbriefinfo.innerHTML = actorbriefinfo.textContent.substr(0, 276) + "..." + "<div class='moweidiv'>(展开全部)</div>"
        let moweidiv = document.querySelector(".moweidiv")
        moweidiv.addEventListener("click", () => {
            actorbriefinfo.innerHTML = tempcontent
            moweidiv.style.display = "none"
        })
    }
    let actorFilmss=await PostData("/actor/getfilmids",actor_id)
    let actorFilms = actorFilmss.data
    let actorfilmsbigbox = document.querySelector("#actorfilmsbigbox")
    for(let i = 0; i < actorFilms.length; i++){
        let filmsData = await PostData("/film/getfilm","film_id="+actorFilms[i])
        let filmsDatamore = filmsData.data
        let tempactorfilmssmallbox = document.createElement("div")
        let tempactorfilms = document.createElement("img")
        let tempfilmname = document.createElement("div")
        let tempfilmpoints = document.createElement("span")
        tempfilmpoints.classList.add("filmpoints")
        tempfilmname.classList.add("filmname")
        tempactorfilms.classList.add("actorfilms")
        tempactorfilmssmallbox.classList.add("actorfilmssmallbox")
        tempactorfilms.src = filmsDatamore.poster_url
        tempfilmname.textContent = filmsDatamore.name
        tempfilmpoints.textContent = filmsDatamore.score
        tempactorfilmssmallbox.append(tempactorfilms)
        tempactorfilmssmallbox.append(tempfilmname)
        tempactorfilmssmallbox.append(tempfilmpoints)
        actorfilmsbigbox.append(tempactorfilmssmallbox)
        tempactorfilms.i = i
        tempactorfilms.addEventListener("click",() => {
            location.href = MakeUrl("/subject.html?film_id="+(actorFilms[tempactorfilms.i]-1))
        })
        tempfilmname.addEventListener("click",() => {
            location.href = MakeUrl("/subject.html?film_id="+(actorFilms[tempactorfilms.i]-1))
        })
    }
}
getActorData()