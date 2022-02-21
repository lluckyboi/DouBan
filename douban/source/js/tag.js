import { LoginByToken,LoginChecked,MakeUrl, PostData,GetData} from "./moudle.js";

LoginChecked()
let clissify_choices = document.querySelectorAll(".clissify_choices")
for(let i = 0; i <clissify_choices.length;i++){
    clissify_choices[i].firstElementChild.classList.add("choice_hover")
}
let nocl = document.querySelectorAll(".nocl")
function hover_choice_listen(){
    for(let i = 0; i < clissify_choices.length;i++){
        for(let j = 0; j < clissify_choices[i].children.length;j++){
            if(i == 4&& j >= clissify_choices[4].children.length-2){
                break
            }
            clissify_choices[i].children[j].addEventListener("click",() => {
                for(let k = 0; k < clissify_choices[i].children.length; k++){
                    clissify_choices[i].children[k].classList.remove("choice_hover")
                    clissify_choices[i].children[k].classList.add("cchoice_hover")
                }
                clissify_choices[i].children[j].classList.remove("cchoice_hover")
                clissify_choices[i].children[j].classList.add("choice_hover")
                for(let m = 0; m < nocl.length ; m++){
                    nocl[m].classList.remove("cchoice_hover")
                    nocl[m].classList.remove("choice_hover")
                }
            })
        }
    }
}
hover_choice_listen()
let sub_selfchoice = document.querySelector(".sub_selfchoice")
nocl[0].addEventListener("click",() => {
    nocl[0].style.display = "none"
    sub_selfchoice.style.display = "inline-block"
})
let sub_self = document.querySelector("#sub_self")
let self_text = document.querySelector("#self_text")
sub_self.addEventListener("click",() => {
    if(self_text.value){
        let temp = document.createElement("div")
        temp.classList.add("clissify_cchoice")
        temp.classList.add("cchoice_hover")
        temp.textContent = self_text.value
        temp.addEventListener("click",() => {
            hover_choice_listen()
        })
        clissify_choices[4].insertBefore(temp,nocl[0])
        self_text.value = ""
        nocl[0].style.display = "inline-block"
        sub_selfchoice.style.display = "none"
        hover_choice_listen()
    }
})
let top_choice = document.querySelectorAll(".top_choice")
for(let i = 0; i < top_choice.length; i++){
    top_choice[i].addEventListener("click",() => {
        for(let j = 0; j < top_choice.length ; j++){
            top_choice[j].classList.remove("top_choice_click")
        }
        top_choice[i].classList.add("top_choice_click")
    })
}
let mk_choice = document.querySelectorAll(".mk_choice")
for(let i = 0; i < mk_choice.length;i++){
    let flag = 0;
    mk_choice[i].addEventListener("click",() => {
        if(flag == 0){
            mk_choice[i].children[0].style.display = "none"
            mk_choice[i].children[1].style.display = "block"
            flag = 1;
        }else{
            mk_choice[i].children[0].style.display = "block"
            mk_choice[i].children[1].style.display = "none"
            flag = 0;
        }
    })
}
let img_coice = document.querySelectorAll(".img_coice-1")
img_coice[0].children[0].style.display = "block"
img_coice[0].children[1].style.display = "none"
img_coice[1].children[0].style.display = "none"
img_coice[1].children[1].style.display = "block"
let film_big_box = document.querySelectorAll(".film_big_box")
for(let i = 0; i < img_coice.length; i++){
    img_coice[i].addEventListener("click",() => {
        for(let k = 0; k < 2; k++){
            if(i == 0){
                img_coice[0].children[0].style.display = "block"
                img_coice[0].children[1].style.display = "none"
                img_coice[1].children[0].style.display = "none"
                img_coice[1].children[1].style.display = "block"
                film_big_box[0].classList.remove("film_hidden")
                film_big_box[1].classList.add("film_hidden")
            }else{
                img_coice[0].children[0].style.display = "none"
                img_coice[0].children[1].style.display = "block"
                img_coice[1].children[0].style.display = "block"
                img_coice[1].children[1].style.display = "none"
                film_big_box[0].classList.add("film_hidden")
                film_big_box[1].classList.remove("film_hidden")
            }
        }
    })
}
let load_more = document.querySelector("#load_more")
window.history.pushState(null,null,(location.href.split("?")[0]+"?limit=20"))
let limit =parseInt(window.location.search.substr(7))
let film_big_box01 = document.querySelector("#film_big_box01")
let film_big_box02 = document.querySelector("#film_big_box02")
let clissify_cchoice = document.querySelectorAll(".clissify_cchoice")
async function filmdata(){
    let filmrequest = await GetData("/film/filmlist")
    let filmdata = filmrequest.data
    for(let i = 1; i < clissify_choices.length;i++){
        for(let j = 0; j < clissify_choices[i].children.length;j++){
            clissify_choices[i].children[j].addEventListener("click",async () => {
                let supersearchrequset
                if(i == 1 && j != 0){
                    supersearchrequset = await PostData("/film/supersearch","type="+clissify_cchoice[i].textContent)
                }
                if(i == 2 && j != 0){
                    supersearchrequset = await PostData("/film/supersearch","location="+clissify_cchoice[i].textContent)
                }
                if(i == 3 && j != 0){
                    supersearchrequset = await PostData("/film/supersearch","release_time="+clissify_cchoice[i].textContent)
                }
                if(i == 4 && j != 0){
                    supersearchrequset = await PostData("/film/supersearch","tag="+clissify_cchoice[i].textContent)
                }
                if(j == 0){
                    supersearchrequset =  await GetData("/film/filmlist")
                }
                let supersearch = supersearchrequset.data
                filmdata = supersearch
                film_big_box01.innerHTML = ""
                film_big_box02.innerHTML = ""
                flush()
            })
        }
    }
    for(let i = 0; i < clissify_cchoice.length;i++){
        clissify_cchoice[i].addEventListener("click",async () => {
            let supersearchrequset = await PostData("/film/supersearch","type="+clissify_cchoice[i].textContent)
            let supersearch = supersearchrequset.data
            filmdata = supersearch
            film_big_box01.innerHTML = ""
            film_big_box02.innerHTML = ""
            flush()
        })
    }
    function flush(){
        for(let i = limit-20; i < limit && i < filmdata.length;i++){
            let temp_filem_small_box = document.createElement("div")
            temp_filem_small_box.classList.add("filem_small_box")
            temp_filem_small_box.innerHTML = "<div class='img_box'><img src='' alt='' class='film_img'></div><div class='name_points'>null<div class='points'>1.0</div></div>"
            film_big_box01.append(temp_filem_small_box)
            let temp_film_in = document.createElement("div")
            temp_film_in.classList.add("film_in")
            temp_film_in.innerHTML = "<div class='film_pic'><img src='' alt='' class='fime_picture'></div><div class='pic_right'><div class='small_film_name'>null</div><div class='eva'><div class='starsAndscore'><span class='star'></span><span class='star-point'>8</span></div></div><div class='film_name_information'><div id='director'>导演:<div class='director_name'></div></div><div id='main_actor'>主演:<div class='main_actor_name'></div></div></div></div>"
            film_big_box02.append(temp_film_in)
        }
        let filem_small_box = document.querySelectorAll(".filem_small_box")
        let film_in = document.querySelectorAll(".film_in")
        for(let i = limit-20; i < limit && i < filmdata.length;i++){
            filem_small_box[i].children[0].children[0].src = filmdata[i].poster_url
            filem_small_box[i].children[1].innerHTML = filmdata[i].name + "<div class='points'>"+ filmdata[i].score+"</div>"
            filem_small_box[i].children[0].children[0].addEventListener("click",() =>{
                location.href = MakeUrl("/subject.html?film_id="+filmdata[i].id)
            })
            filem_small_box[i].children[1].addEventListener("click",() =>{
                location.href = MakeUrl("/subject.html?film_id="+filmdata[i].id)
            })
            film_in[i].children[0].children[0].src = filmdata[i].poster_url
            film_in[i].children[1].children[0].textContent = filmdata[i].name
            film_in[i].children[1].children[1].children[0].children[1].textContent = filmdata[i].score
            film_in[i].children[1].children[2].children[0].children[0].textContent = filmdata[i].directer
            film_in[i].children[1].children[2].children[1].children[0].textContent = filmdata[i].screenwriter
            film_in[i].children[0].children[0].addEventListener("click",()=>{
                location.href = MakeUrl("/subject.html?film_id="+filmdata[i].id)
            })
            film_in[i].children[1].children[0].addEventListener("click",()=>{
                location.href = MakeUrl("/subject.html?film_id="+filmdata[i].id)
            })
        }
    }
    flush()
}
filmdata()
load_more.addEventListener("click",() => {
    limit += 20
    window.history.pushState(null,null,(location.href.split("?")[0]+"?limit="+limit))
    filmdata()
})
console.log(limit)