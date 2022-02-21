import { LoginByToken,LoginChecked,MakeUrl,PostData} from "./moudle.js";

LoginChecked()
let commentbox_close = document.querySelector("#commentbox_close")
commentbox_close.addEventListener("click",()=> {
    commentboxborder.style.display = "none"
})
let wan = document.querySelectorAll(".wan")
for(let i = 0; i < wan.length ; i++){
    wan[i].addEventListener("click",() => {
        commentboxborder.style.display = "block"
    })
}
let score_ch = ["很差","较差","还行","推荐","力荐"]
let c_stars1 = document.querySelectorAll(".c_stars1")
let eva1_score = document.querySelector("#eva1_score")
for (let i = 0; i < c_stars1.length;i++){
    c_stars1[i].addEventListener("mouseover",() => {
        for(let k = 0; c_stars1.length ; k++){
            if(k <= i){
                c_stars1[k].src = "./pictures/subject/staryellow.png"
            }if (k > i){
                c_stars1[k].src = "./pictures/subject/star.png"
            }
            eva1_score.textContent = score_ch[i]
        }

    })
}
let eva1_star = document.querySelector("#eva1_star")
eva1_star.addEventListener("mouseout",() => {
    for(let i = 0; i < c_stars1.length ; i++){
        c_stars1[i].src = "./pictures/subject/star.png"
    }
    eva1_score.textContent = ""
})
let search_title = document.querySelector("#search_title")
search_title.textContent = "搜索"+decodeURI(window.location.search.substr(6))
async function getFilmData(){
    let filmRequest = await PostData("/film/searchfilm","name="+decodeURI(window.location.search.substr(6))+"&&"+"aim=name")
    let filmData = filmRequest.data
    let search_content = document.querySelector("#search_content")
    for(let i = 0;i < filmData.length;i++){
        let temp_search_film_box = document.createElement("div")
        temp_search_film_box.classList.add("search_film_box")
        temp_search_film_box.innerHTML = "<img src='' class='search_film_img' alt=''><div class='search_film_information'><div class='filmnameAndYears'>null</div><div class='starsAndscore'><span class='star'></span><span class='star-point'>8</span><span class='starnumbers'>(null人评价)</span></div><div class='film_info01'>null</div><div class='film_info02'>null</div><div class='wantorsee'><div class='wan'>想看</div><div class='wan'>看过</div></div></div>"
        search_content.append(temp_search_film_box)
    }
    let search_film_box = document.querySelectorAll(".search_film_box")
    for(let i = 0;i < filmData.length;i++){
        search_film_box[i].children[0].src=filmData[i].poster_url
        search_film_box[i].children[1].children[0].textContent = filmData[i].name+"("+filmData[i].release_time.substr(0,4)+")"
        search_film_box[i].children[1].children[1].children[1].textContent = filmData[i].score
        search_film_box[i].children[1].children[1].children[2].textContent = filmData[i].post_num + "人评价"
        search_film_box[i].children[1].children[2].textContent = filmData[i].location + " / " +filmData[i].type + " / " +filmData[i].other_name + " / " + filmData[i].length
        search_film_box[i].children[1].children[3].textContent = filmData[i].directer + " / "+filmData[i].screenwriter
        search_film_box[i].children[0].addEventListener("click",()=> {
            window.location.href = MakeUrl("/subject.html?film_id="+(filmData[i].id-1))
        })
        search_film_box[i].children[1].children[0].addEventListener("click",()=> {
            window.location.href = MakeUrl("/subject.html?film_id="+(filmData[i].id-1))
        })
    }
}
getFilmData()