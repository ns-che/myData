/* HEADER */
window.addEventListener('load', scrollFunction);
window.addEventListener('scroll', scrollFunction);

// 스크롤 될때
function scrollFunction() {
    console.log(document.documentElement.scrollTop);
    var header = document.getElementById("header");

    if(document.documentElement.scrollTop > 70){
        if(!header.classList.contains("navbar-fixed")){
            header.classList.add("navbar-fixed");
            // document.getElementsByTagName("body")[0].style.marginTop = "150px";

            // 페이드 효과(잠깐 안보이다가 40밀리초 후에 다시 보이게)
            header.style.display = "none";
            setTimeout(function(){
                header.style.display = "block";
            },40);

            document.documentElement.scrollTop = Math.max(document.documentElement.scrollTop, 70);
        }
    }
    else{
        if(header.classList.contains("navbar-fixed")){
            header.classList.remove("navbar-fixed");
            // document.getElementsByTagName("body")[0].style.marginTop = "0px";
        }
    }
}
// 메뉴 토글될때
function menuToggle(){
    // menu 아이디를 가진 요소에서 show 클래스가 있으면 제거, 없으면 추가
    document.getElementById("menu").classList.toggle("show");
}

document.getElementById("toggleBtn").addEventListener("click", menuToggle);