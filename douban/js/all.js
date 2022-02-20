function restar(){
    let star_point = document.querySelectorAll(".star-point");
    let star = document.querySelectorAll(".star");
    for(let i = 0; i < star_point.length ; i++){
    points = star_point[i].textContent;
    star[i].style.backgroundPosition = 0+"% " + (100-Math.round(points)*10) + "%"; 
    }
}

restar()