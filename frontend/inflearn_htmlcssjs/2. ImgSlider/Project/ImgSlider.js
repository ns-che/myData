/* HEADER */
window.addEventListener('load', scrollFunction);
window.addEventListener('scroll', scrollFunction);

// 스크롤 될때
function scrollFunction() {
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

/* WELCOME AREA */
var imageSlideIndex = 1; // 현재 노출되어야 하는 이미지 슬라이드 번호 보관
showImageSlides(imageSlideIndex); // 첫번째 이미지 슬라이드 보여주기

function imageSlideTimer(){ // 자동으로 이미지 슬라이드 넘기기
    plusImageSlides(1);
}

var imageTimer = setInterval(imageSlideTimer, 3000); // 5초마다 이미지 슬라이드 넘기기

function plusImageSlides(n){ // n: 이미지 슬라이드 번호 증감값
    clearInterval(imageTimer); // 기존 타이머 제거
    imageTimer = setInterval(imageSlideTimer, 3000); // 새로운 타이머 설정

    showImageSlides(imageSlideIndex += n);
}
function currentImageSlide(n){ // n: 보여주고자 하는 이미지 슬라이드 번호
    clearInterval(imageTimer); // 기존 타이머 제거
    imageTimer = setInterval(imageSlideTimer, 3000); // 새로운 타이머 설정

    showImageSlides(imageSlideIndex = n);
}

function showImageSlides(n){ // n: 보여주고자 하는 이미지 슬라이드 번호
    var i;
    var slides = document.getElementsByClassName("image-slide"); // 모든 이미지 슬라이드 요소들
    var dots = document.getElementsByClassName("dot"); // 모든 도트 요소들

    if(n > slides.length){
        imageSlideIndex = 1; // 처음으로 돌아감
    }
    if(n < 1){
        imageSlideIndex = slides.length; // 마지막으로 감
    }

    for(i=0; i<slides.length; i++){
        slides[i].style.display = "none"; // 모든 이미지 슬라이드 숨김
    }
    for(i=0; i<dots.length; i++){
        dots[i].className = dots[i].className.replace(' active', ''); // 모든 도트 비활성화
    }
    slides[imageSlideIndex - 1].style.display = "block"; // 현재 이미지 슬라이드 보이기
    dots[imageSlideIndex - 1].className += ' active'; // 현재 도트 활성화
}

document.getElementById("imagePrev").addEventListener("click", plusImageSlides.bind(null, -1));
document.getElementById("imageNext").addEventListener("click", plusImageSlides.bind(null, 1));

document.getElementById("firstDot").addEventListener("click", currentImageSlide.bind(null, 1));
document.getElementById("secondDot").addEventListener("click", currentImageSlide.bind(null, 2));
document.getElementById("thirdDot").addEventListener("click", currentImageSlide.bind(null, 3));
document.getElementById("forthDot").addEventListener("click", currentImageSlide.bind(null, 4));

