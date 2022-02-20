import { LoginByToken,LoginChecked} from "./moudle.js";

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
