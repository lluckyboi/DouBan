import { LoginByToken,LoginChecked,GetData, MakeUrl} from "./moudle.js";

LoginChecked()
let film_name_information = document.querySelectorAll(".film_name_information")

for(let i = 0; i < film_name_information.length ;i++){
    if(film_name_information[i].textContent.length > 98){
        film_name_information[i].textContent = film_name_information[i].textContent.substr(0,98) + "..."
    }
}
let chart_left_content = document.querySelector("#chart_left_content")
async function getfilmdata(){
    let filmrequest =await GetData("/film/filmlist")
    let filmData = filmrequest.data
    for(let i = 0; i < filmData.length ; i++){
        let temp_film_in = document.createElement("div")
        temp_film_in.classList.add("film_in")
        temp_film_in.innerHTML="<div class='film_pic'><img src='' alt='' class='fime_picture'></div><div class='pic_right'><div class='small_film_name'>null</div><div class='film_name_information'>null</div><div class='eva'><div class='starsAndscore'><span class='star'></span><span class='star-point'>8</span><div class='peo_numbers'>(null)</div></div></div></div>"
        chart_left_content.append(temp_film_in)
    }
    let film_in = document.querySelectorAll(".film_in")
    let name = document.querySelectorAll(".name")
    for(let i = 0; i < filmData.length;i++){
        film_in[i].children[0].children[0].src = filmData[i].poster_url
        film_in[i].children[1].children[0].textContent = filmData[i].name
        let film_information = filmData[i].release_time + " / " + filmData[i].directer + " / " + filmData[i].screenwriter + " / " + filmData[i].length + " / " + filmData[i].type + " / " + filmData[i].language
        film_in[i].children[1].children[1].textContent = film_information
        film_in[i].children[1].children[2].children[0].children[1].textContent = filmData[i].score
        film_in[i].children[1].children[2].children[0].children[2].textContent = "("+filmData[i].post_num + "人评价)"
        film_in[i].children[0].children[0].addEventListener("click",() => {
            location.href = MakeUrl("/subject.html?film_id="+(filmData[i].id-1))
        })
        film_in[i].children[1].children[0].addEventListener("click",() => {
            location.href = MakeUrl("/subject.html?film_id="+(filmData[i].id-1))
        })
    }
    for(let i = 0; i < 20; i++){
        name[i].textContent = filmData[i].name
        name[i].addEventListener("click",() => {
            location.href = MakeUrl("/subject.html?film_id="+(filmData[i].id-1))
        })
    }
    let top_film = document.querySelectorAll(".top_film")
    for(let i = 0; i <top_film.length ; i++){
        top_film[i].children[0].children[0].src = filmData[i].poster_url
        if(filmData[i].name.length>10){
            top_film[i].children[1].textContent = filmData[i].name.substr(0,10) + "..."
        }else{
            top_film[i].children[1].textContent = filmData[i].name
        }
        top_film[i].children[0].children[0].addEventListener("click",() =>{
            location.href = MakeUrl("/subject.html?film_id="+(filmData[i].id-1))
        })
        top_film[i].children[1].addEventListener("click",() => {
            location.href = MakeUrl("/subject.html?film_id="+(filmData[i].id-1))
        })
    }
    restar()
}
getfilmdata()