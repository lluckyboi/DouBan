import { LoginByToken, LoginChecked, GetData, MakeUrl } from "./moudle.js";


LoginChecked()
function order(obj) {
    let temp = obj[obj.length - 1]
    for (let i = obj.length - 2; i >= 0; i--) {
        obj[i + 1] = obj[i];
    }
    obj[0] = temp;
}
let arrow2_left = document.querySelector('#arrowhead_2_01');
let arrow2_right = document.querySelector('#arrowhead_2_02');
let rec_box = document.querySelectorAll('.rec_box');
let recomand = document.querySelector('#recommend');
let n = 0;
let last_time_01 = Date.now() - 1600;
arrow2_left.addEventListener('click', () => {
    clearInterval(recomend_lunbo);
    if (Date.now() - last_time_01 >= 1600) {
        images_move("left");
        last_time_01 = Date.now();
    }
    recomend_lunbo = setInterval(() => {
        images_move("right");
    }, 10000);
})
arrow2_right.addEventListener('click', () => {
    clearInterval(recomend_lunbo);
    if (Date.now() - last_time_01 >= 1600) {
        images_move("right");
        last_time_01 = Date.now();
    }
    recomend_lunbo = setInterval(() => {
        images_move("right");
    }, 5000);
})
for (let i = 0; i < rec_box.length; i++) {
    rec_box[i].style.left = i * 45 + "rem";
}
setTimeout(() => {
    for (let i = 0; i < rec_box.length; i++) {
        rec_box[i].classList.add("rec_box_remove");
    }
}, 100)
let recomend_lunbo = setInterval(() => {
    images_move("right");
}, 5000);
let recommend_n = 1;
let pro02_left = document.querySelector("#pro02_left");
function images_move(position) {

    if (position === "left") {
        for (let i = 0; i < rec_box.length; i++) {
            rec_box[i].style.left = getNum(parseInt(rec_box[i].style.left)) + 45 + "rem";
        }
        let temp_child = recomand.removeChild(recomand.lastElementChild);
        temp_child.style.left = "0rem";
        recomand.insertBefore(temp_child, recomand.firstElementChild);
        recommend_n--;
    }
    if (position === "right") {
        for (let i = 0; i < rec_box.length; i++) {
            rec_box[i].style.left = getNum(parseInt(rec_box[i].style.left)) - 45 + "rem";
        }
        let temp_child = recomand.removeChild(recomand.firstElementChild);
        temp_child.style.left = (rec_box.length - 1) * 45 + "rem";
        recomand.appendChild(temp_child);
        recommend_n++;
    }
    if (recommend_n <= 0) {
        recommend_n = 7;
    } else if (recommend_n > 7) {
        recommend_n = 1;
    }
    pro02_left.textContent = recommend_n;
}

function getNum(val) {
    if (isNaN(val)) {
        return 0;
    } else {
        return val;
    }
}



let hot_mid_film = document.querySelectorAll(".hot_mid_film")
let hotingFilm = document.querySelectorAll(".hotingFilm")
for (let i = 0; i < hot_mid_film.length; i++) {
    hot_mid_film[i].style.left = i * 45 + "rem"
    for (let j = 0; j < hot_mid_film[i].children.length; j++) {
        hot_mid_film[i].children[j].style.left = j * 9.3 + "rem";
    }
}
let hover_film_hot = document.querySelector(".hover_film_hot")
let hotingImg = document.querySelectorAll(".hotingImg")
for (let i = 0; i < hotingImg.length; i++) {
    hotingImg[i].addEventListener("mouseover", () => {
        async function hotimghover() {
            let films = await GetData("/film/filmlist")
            let filmsArry = films.data
            hover_film_hot.children[0].children[0].textContent = filmsArry[i].name
            hover_film_hot.children[1].children[0].children[0].children[1].textContent = filmsArry[i].score
            hover_film_hot.children[1].children[1].textContent = "(" + filmsArry[i].post_num + "人评价)"
            hover_film_hot.children[2].children[0].textContent = filmsArry[i].length
            hover_film_hot.children[2].children[1].textContent = filmsArry[i].location
            hover_film_hot.children[3].children[0].children[0].textContent = filmsArry[i].directer
            hover_film_hot.children[3].children[1].children[0].textContent = filmsArry[i].screenwriter
            restar()
        }
        hotimghover()
        hover_film_hot.style.left = parseInt(hotingFilm[i].style.left) + 8.5 + "rem"
        hover_film_hot.style.display = "block"
    })
    hotingImg[i].addEventListener("mouseout", () => {
        hover_film_hot.style.display = "none"
    })
}
let filmBigbox = document.querySelectorAll(".filmBigbox")


//娣诲姞瀛╁瓙蹇呴』鍦ㄨ繖涓嚱鏁颁箣鍓�
function lunboPosreload() {
    for (let i = 0; i < filmBigbox.length; i++) {
        let m = 0
        for (let j = 0; j < filmBigbox[i].children[1].children.length; j++) {
            filmBigbox[i].children[1].children[j].style.left = j * 45 + "rem"
            let n = 0
            for (let k = 0; k < filmBigbox[i].children[1].children[j].children.length; k++) {
                filmBigbox[i].children[1].children[j].children[k].style.left = 9.3 * n + "rem"
                filmBigbox[i].children[1].children[j].children[k].style.top = m * 15 + "rem"
                n++
                if (n == 5) {
                    n = 0
                    m++
                }
            }
            m = 0
        }
    }
}
let hover_big_box = document.querySelectorAll(".hover_big_box")
let hover_toptag = document.querySelectorAll(".hover_toptag")
let tempARRR
async function makelunbobox() {
    let films = await GetData("/film/filmlist")
    let filmsArry = films.data
    for (let n = 0; n < filmbbbbox.length; n++) {
        let makefilmMidboxNum = 0
        let filmsSmallboxNum = filmsArry.length
        makefilmMidboxNum = Math.ceil(filmsArry.length / 10)
        for (makefilmMidboxNum; makefilmMidboxNum > 0; makefilmMidboxNum--) {
            let temp_filmMidboxNum = document.createElement("div")
            temp_filmMidboxNum.classList.add("filmMidbox")
            for (let temp_num = 0; temp_num < 10 && filmsSmallboxNum > 0; temp_num++) {
                let temp_filmsSmallbox = document.createElement("div")
                temp_filmsSmallbox.classList.add("filmsSmallbox")
                temp_filmsSmallbox.innerHTML = "<img src='' alt='' class='filmimgbiu'><div class='filmname filmnamebiu warp'>2<span class='filmpointsbiu'>null</span></div>"
                temp_filmMidboxNum.append(temp_filmsSmallbox)
                filmsSmallboxNum--
            }
            filmbbbbox[n].append(temp_filmMidboxNum)
        }
        filmbbbbox[n].insertBefore(filmbbbbox[n].lastElementChild, filmbbbbox[n].firstElementChild)
        lunboPosreload()
    }

    let hover_bigbig = document.querySelectorAll(".hover_bigbig")
    // for (let i = 0; i < filmBigbox.length; i++) {
    //     for (let j = 0; j < filmBigbox[i].children[1].children.length; j++) {
    //         for (let k = 0; k < filmBigbox[i].children[1].children[j].children.length; k++) {
    //             filmBigbox[i].children[1].children[j].children[k].addEventListener("mouseover", () => {
    //                 hover_bigbig[i].style.display = "block"
    //                 console.log(filmBigbox[i].children[1].children[j].children[k])
    //                 hover_bigbig[i].style.left = parseInt(filmBigbox[i].children[1].children[j].children[k].style.left) + 7.7 + "rem"
    //                 if (i == 0) {
    //                     hover_bigbig[i].style.top = parseInt(filmBigbox[i].children[1].children[j].children[k].style.top) + 24.6 + "rem"
    //                 }
    //                 if (i == 1) {
    //                     hover_bigbig[i].style.top = parseInt(filmBigbox[i].children[1].children[j].children[k].style.top) + 60.6 + "rem"
    //                 }
    //             })
    //             filmBigbox[i].children[1].children[j].children[k].addEventListener("mouseout", () => {
    //                 hover_bigbig[i].style.display = "none"
    //             })
    //         }
    //     }
    // }
    for (let i = 0; i < filmbbbbox.length; i++) {
        let p = 0
        for (let j = 0; j < filmbbbbox[i].children.length; j++) {
            // let tempj = j
            // if(j == 0){
            //     j = 2
            // }else if(j == 2){
            //     j = 0
            // }
            for (let k = 0; k < filmbbbbox[i].children[j].children.length; k++) {
                filmbbbbox[i].children[j].children[k].p = p
                filmbbbbox[i].children[j].children[k].addEventListener("mouseover", () => {
                    console.log(filmbbbbox[i].children[j].children[k].p)
                    hover_big_box[i].children[0].children[0].innerHTML = filmsArry[filmbbbbox[i].children[j].children[k].p].name + "<span class='filmyears hover_topfilmyears'>("+filmsArry[filmbbbbox[i].children[j].children[k].p].release_time.substr(0,4)+")</span>"
                    hover_big_box[i].children[0].children[1].children[0].children[1].textContent = filmsArry[filmbbbbox[i].children[j].children[k].p].score
                    let tempstr = filmsArry[filmbbbbox[i].children[j].children[k].p].length + " / "+filmsArry[filmbbbbox[i].children[j].children[k].p].location + " / "+filmsArry[filmbbbbox[i].children[j].children[k].p].type + " / "+filmsArry[filmbbbbox[i].children[j].children[k].p].directer+"(导演)" + " / "+filmsArry[filmbbbbox[i].children[j].children[k].p].screenwriter
                    let temparr = tempstr.split(" / ")
                    for(let e = 0; e < temparr.length; e++){
                        let temp_e = document.createElement("div")
                        temp_e.textContent = temparr[e]
                        hover_toptag[i].append(temp_e)
                    }
                    tempARRR=hover_toptag[i].innerHTML
                    hover_bigbig[i].style.display = "block"
                    hover_bigbig[i].style.left = parseInt(filmbbbbox[i].children[j].children[k].style.left) + 7.7 + "rem"
                    if (i == 0) {
                        hover_bigbig[i].style.top = parseInt(filmbbbbox[i].children[j].children[k].style.top) + 24.6 + "rem"
                    }
                    if (i == 1) {
                        hover_bigbig[i].style.top = parseInt(filmbbbbox[i].children[j].children[k].style.top) + 60.6 + "rem"
                    }
                    restar()
                })
                filmbbbbox[i].children[j].children[k].addEventListener("mouseout", () => {
                    hover_bigbig[i].style.display = "none"
                    hover_toptag[i].textContent = ""
                })
                p++
            }
            // j = tempj
        }
    }
    for (let i = 0; i < hover_bigbig.length; i++) {
        hover_bigbig[i].addEventListener("mouseover", () => {
            hover_bigbig[i].style.display = "block"
            hover_toptag[i].innerHTML = tempARRR
        })
        hover_bigbig[i].addEventListener("mouseout", () => {
            hover_bigbig[i].style.display = "none"
            hover_toptag[i].textContent = ""
        })
    }
    restar()
}
makelunbobox()
let pro01 = document.querySelector("#pro01")
if (hotingFilm.length % 5 == 0) {
    pro01.children[1].textContent = hotingFilm.length / 5
} else {
    pro01.children[1].textContent = hotingFilm.length / 5 + 1
}

let arrow1_left = document.querySelector('#arrowhead_1_01');
let arrow1_right = document.querySelector('#arrowhead_1_02');
let recommend_n2 = 1
function images_move02(position, obj, objfather, recommend_n, C = 0) {

    if (position === "left") {
        for (let i = 0; i < obj.length; i++) {
            obj[i].style.left = getNum(parseInt(obj[i].style.left)) + 45 + "rem";
        }
        let temp_child = objfather.removeChild(objfather.lastElementChild);
        temp_child.style.left = "0rem";
        objfather.insertBefore(temp_child, objfather.firstElementChild);
        recommend_n--;
    }
    if (position === "right") {
        for (let i = 0; i < obj.length; i++) {

            obj[i].style.left = getNum(parseInt(obj[i].style.left)) - 45 + "rem";
        }
        let temp_child = objfather.removeChild(objfather.firstElementChild);
        temp_child.style.left = (obj.length - 1 + C) * 45 + "rem";
        objfather.appendChild(temp_child);
        recommend_n++;
    }
    if (recommend_n <= 0) {
        recommend_n = obj.length;
    } else if (recommend_n > obj.length) {
        recommend_n = 1;
    }
    return recommend_n
}
let left_01_imgboxs = document.querySelector("#left_01_imgboxs")

let lunbo01 = setInterval(() => {
    recommend_n2 = images_move02("right", hot_mid_film, left_01_imgboxs, recommend_n2);
    pro01.children[0].textContent = recommend_n2;
}, 5000);
let last_time_02 = 0;
arrow1_left.addEventListener('click', () => {
    clearInterval(lunbo01);
    if (Date.now() - last_time_01 >= 500) {
        recommend_n2 = images_move02("left", hot_mid_film, left_01_imgboxs, recommend_n2);
        pro01.children[0].textContent = recommend_n2;
        last_time_01 = Date.now();
    }
    lunbo01 = setInterval(() => {
        recommend_n2 = images_move02("right", hot_mid_film, left_01_imgboxs, recommend_n2);
        pro01.children[0].textContent = recommend_n2;
    }, 5000);
})
arrow1_right.addEventListener('click', () => {
    clearInterval(lunbo01);
    if (Date.now() - last_time_01 >= 500) {
        recommend_n2 = images_move02("right", hot_mid_film, left_01_imgboxs, recommend_n2);
        pro01.children[0].textContent = recommend_n2;
        last_time_01 = Date.now();
    }
    lunbo01 = setInterval(() => {
        recommend_n2 = images_move02("right", hot_mid_film, left_01_imgboxs, recommend_n2);
        pro01.children[0].textContent = recommend_n2;
    }, 5000);
})
let last_time_03 = 0
let arrowheads = document.querySelectorAll(".arrowheads")
let arr1_rnum = 1
let arr2_rnum = 1

let recommend_n3 = 1
let filmbbbbox = document.querySelectorAll(".filmbbbbox")
let ar01 = document.querySelector("#ar01")
let ar02 = document.querySelector("#ar02")
let ar03 = document.querySelector("#ar03")
let ar04 = document.querySelector("#ar04")
let recommend_04 = 1
let last_time_04 = 0
function arr_num(number) {
    if (number == 0) {
        return 3
    }
    if (number == 4) {
        return 1
    }
    return number
}



let score_ch = ["很差", "较差", "还行", "推荐", "力荐"]
let commentboxborder = document.querySelector("#commentboxborder")
let commentbox_close = document.querySelector("#commentbox_close")
commentbox_close.addEventListener("click", () => {
    commentboxborder.style.display = "none"
})
let writecomment = document.querySelectorAll(".writecomment")
for (let i = 0; i < writecomment.length; i++) {
    writecomment[i].addEventListener("click", () => {
        commentboxborder.style.display = "block"
    })
}

let c_stars1 = document.querySelectorAll(".c_stars1")
let eva1_score = document.querySelector("#eva1_score")
for (let i = 0; i < c_stars1.length; i++) {
    c_stars1[i].addEventListener("mouseover", () => {
        for (let k = 0; c_stars1.length; k++) {
            if (k <= i) {
                c_stars1[k].src = "./pictures/subject/staryellow.png"
            } if (k > i) {
                c_stars1[k].src = "./pictures/subject/star.png"
            }
            eva1_score.textContent = score_ch[i]
        }
    })
}




for (let i = 0; i < arrowheads.length; i++) {
    let rel1_pos = 0;
    let rel2_pos = 0;
    arrowheads[i].children[1].style.backgroundColor = "rgb(97,152,215)"
    for (let j = 1; j < arrowheads[i].children.length - 1; j++) {
        arrowheads[i].children[j].addEventListener("click", () => {
            for (let k = 1; k < arrowheads[i].children.length - 1; k++) {
                arrowheads[i].children[k].style.backgroundColor = "rgb(216,216,216)"
            }
            arrowheads[i].children[j].style.backgroundColor = "rgb(97,152,215)"
            if (i == 0) {
                rel1_pos = j - arr1_rnum
                arr1_rnum = j
            } else {
                rel2_pos = j - arr2_rnum
                arr2_rnum = j
            }
            console.log(rel1_pos)
            console.log(rel2_pos)
            if (rel1_pos > 0) {
                for (let p = 0; p < rel1_pos; p++) {
                    setTimeout(() => {
                        recommend_n3 = images_move02("right", filmbbbbox[0].children, filmbbbbox[0], recommend_n3, 1)
                    }, p * 500)
                }
                rel1_pos = 0
            }
            if (rel1_pos < 0) {
                for (let p = 0; p < rel1_pos * (-1); p++) {
                    setTimeout(() => {
                        recommend_n3 = images_move02("left", filmbbbbox[0].children, filmbbbbox[0], recommend_n3, 1)
                    }, p * 500)

                }
                rel1_pos = 0
            }
            if (rel2_pos > 0) {
                for (let p = 0; p < rel2_pos; p++) {
                    setTimeout(() => {
                        recommend_04 = images_move02("right", filmbbbbox[1].children, filmbbbbox[1], recommend_04, 1)
                    }, p * 500)

                }
                rel2_pos = 0
            }
            if (rel2_pos < 0) {
                for (let p = 0; p < rel2_pos * (-1); p++) {
                    setTimeout(() => {
                        recommend_04 = images_move02("left", filmbbbbox[1].children, filmbbbbox[1], recommend_04, 1)
                    }, p * 500)
                }
                rel2_pos = 0
            }
        })
    }
}
ar01.addEventListener("click", () => {
    if (Date.now() - last_time_03 >= 500) {
        for (let i = 1; i < arrowheads[0].children.length - 1; i++) {
            arrowheads[0].children[i].style.backgroundColor = "rgb(216,216,216)"
        }
        arr1_rnum = arr_num(--arr1_rnum)
        arrowheads[0].children[arr1_rnum].style.backgroundColor = "rgb(97,152,215)"
        recommend_n3 = images_move02("left", filmbbbbox[0].children, filmbbbbox[0], recommend_n3, 1)
        last_time_03 = Date.now();
    }
})
ar02.addEventListener("click", () => {
    if (Date.now() - last_time_03 >= 500) {
        for (let i = 1; i < arrowheads[0].children.length - 1; i++) {
            arrowheads[0].children[i].style.backgroundColor = "rgb(216,216,216)"
        }
        arr1_rnum = arr_num(++arr1_rnum)
        arrowheads[0].children[arr1_rnum].style.backgroundColor = "rgb(97,152,215)"
        recommend_n3 = images_move02("right", filmbbbbox[0].children, filmbbbbox[0], recommend_n3, 1)
        last_time_03 = Date.now();
    }
})
ar03.addEventListener("click", () => {
    if (Date.now() - last_time_04 >= 500) {
        for (let i = 1; i < arrowheads[1].children.length - 1; i++) {
            arrowheads[1].children[i].style.backgroundColor = "rgb(216,216,216)"
        }
        arr2_rnum = arr_num(--arr2_rnum)
        arrowheads[1].children[arr2_rnum].style.backgroundColor = "rgb(97,152,215)"
        recommend_04 = images_move02("left", filmbbbbox[1].children, filmbbbbox[1], recommend_04, 1)
        last_time_04 = Date.now();
    }
})
ar04.addEventListener("click", () => {
    if (Date.now() - last_time_04 >= 500) {
        for (let i = 1; i < arrowheads[1].children.length - 1; i++) {
            arrowheads[1].children[i].style.backgroundColor = "rgb(216,216,216)"
        }
        arr2_rnum = arr_num(++arr2_rnum)
        arrowheads[1].children[arr2_rnum].style.backgroundColor = "rgb(97,152,215)"
        recommend_04 = images_move02("right", filmbbbbox[1].children, filmbbbbox[1], recommend_04, 1)
        last_time_04 = Date.now();
    }
})
async function initialize() {
    let films = await GetData("/film/filmlist")
    let filmsArry = films.data
    for (let i = 0; i < hotingFilm.length; i++) {
        hotingFilm[i].children[0].src = filmsArry.poster_url
        hotingFilm[i].children[1].textContent = filmsArry[i].name
        hotingFilm[i].children[1].addEventListener("click",() => {
            location.href = MakeUrl("/subject.html?film_id="+i)
        })
        hotingFilm[i].children[2].children[0].children[1].textContent = filmsArry[i].score
    }
    for (let i = 0; i < filmbbbbox.length; i++) {
        let p = 0;
        for (let j = 0; j < filmbbbbox[i].children.length; j++) {
            for (let k = 0; k < filmbbbbox[i].children[j].children.length; k++) {
                filmbbbbox[i].children[j].children[k].children[0].src = filmsArry[p].poster_url
                filmbbbbox[i].children[j].children[k].p = p
                filmbbbbox[i].children[j].children[k].children[1].innerHTML = filmsArry[p].name + "<span class='filmpointsbiu'>" + filmsArry[k].score + "</span>"
                filmbbbbox[i].children[j].children[k].addEventListener("click",() =>{
                    location.href =MakeUrl("/subject.html?film_id="+filmbbbbox[i].children[j].children[k].p)
                })
                p++
            }
        }
    }
    let rb2_02 = document.querySelectorAll(".rb2_02")
    for(let i = 0; i < rb2_02.length;i++){
        rb2_02[i].children[0].textContent = filmsArry[i].name
        rb2_02[i].children[0].href = MakeUrl("/subject.html?film_id="+i)
    }
    restar()
}

setInterval(()=>{
    for(let i = 0; i <hotingImg.length;i++){
        hotingImg[i].addEventListener("click",() => {
            location.href = MakeUrl("/subject.html?film_id="+i)
        })
    }
},200)
//清楚所有定时器
// for(var i = 1; i < 1000; i++) {
//     clearInterval(i);
//     }
for(let i = 0; i <writecomment.length ; i++){
    writecomment[i].addEventListener("click",() =>{
        if(localStorage.getItem("token") == null){
            location.href = MakeUrl("/login.html")
        }
    })
}
initialize()