import { MakeUrl, PostData} from "./moudle.js";
let film_id = window.location.search.substr(1)
let film_box = document.querySelector("#film_box")
async function initialize(){
    let filmrequest =await PostData("/film/getfilm",film_id)
    let filmdata = filmrequest.data
    film_box.children[0].src = filmdata.poster_url
    film_box.children[1].children[0].children[0].textContent = filmdata.name
    film_box.children[1].children[1].textContent = "导演:"+filmdata.directer + " 主演:"+filmdata.screenwriter+" / "+filmdata.location +" / " +filmdata.score+"分("+filmdata.post_num+"人评价)"
    film_box.children[1].children[0].children[0].addEventListener("click",()=>{
        window.location.href = MakeUrl("/subject.html?film_id="+(parseInt(window.location.search.substr(9))-1))
    })
}
let index = document.querySelector(".index")
index.addEventListener("click",() => {
    window.location.href = MakeUrl("/index.html")
})
initialize()