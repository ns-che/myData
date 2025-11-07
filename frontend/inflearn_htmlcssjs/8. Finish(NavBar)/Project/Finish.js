/* HEADER */
window.addEventListener('load', scrollFunction);
window.addEventListener('scroll', scrollFunction);

// 스크롤 될때
function scrollFunction() {
    var header = document.getElementById("header");

    if(document.documentElement.scrollTop > 70){
        if(document.documentElement.scrollTop < 90){
            return;
        }

        if(!header.classList.contains("navbar-fixed")){
            header.classList.add("navbar-fixed");
            // document.getElementsByTagName("body")[0].style.marginTop = "150px";
            console.log(document.documentElement.scrollTop);

            // 페이드 효과(잠깐 안보이다가 40밀리초 후에 다시 보이게)
            header.style.display = "none";
            setTimeout(function(){
                header.style.display = "block";
            },40);

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

/* PORTFOLIO AREA */

filterSelection("all"); // 처음에 all 항목 선택된 상태로 시작

function filterSelection(id) {
    var x, i;

    x = document.getElementsByClassName("listItem");
    for(i=0; i<x.length; i++){
        removeClass(x[i], "active");
    }
    addClass(document.getElementById(id), "active");
    
    x = document.getElementsByClassName("filterItem");
    if(id === "all") id = ''; // all이면 공백으로 변경 => 모든 항목 표시하기 위함
    for(i=0; i<x.length; i++){
        removeClass(x[i], "show");
        // 존재하거나 공백이면 0 이상
        if(x[i].className.indexOf(id) > -1){
            addClass(x[i], "show");
        }
    }
}

function addClass(element, name) {
    if(element.className.indexOf(name) == -1){
        element.className += " " + name;
    }
    //if(!element.classList.contains(name)) element.classList.add(name);
}
function removeClass(element, name) {
    var arr;
    arr = element.className.split(" ");

    while(arr.indexOf(name) > -1){
        arr.splice(arr.indexOf(name), 1); // name이 존재하는 인덱스에서 1개 요소 제거(해당 클래스명 제거)
    }
    element.className = arr.join(" ");
    //if(element.classList.contains(name)) element.classList.remove(name);
}

document.getElementById("all").addEventListener("click", filterSelection.bind(null, "all"));
document.getElementById("uiux").addEventListener("click", filterSelection.bind(null, "uiux"));
document.getElementById("java").addEventListener("click", filterSelection.bind(null, "java"));
document.getElementById("db").addEventListener("click", filterSelection.bind(null, "db"));

function viewPortfolio(event){
    var polyNode = event.target;

    if(polyNode.tagName.toLowerCase() == "i"){
        polyNode = polyNode.parentNode; // i 태그의 부모 요소(overlay 클래스 요소)로 변경
    }
    
    var overlayNode = polyNode;
    var imageNode = overlayNode.nextElementSibling; // overlay 클래스 요소의 다음 태그(img 태그)
    
    var itemNode = overlayNode.parentNode; 
    var mainNode = itemNode.nextElementSibling;
    var subNode = mainNode.nextElementSibling;
    var textNode = subNode.nextElementSibling;
    
    document.getElementById("modalImage").src = imageNode.src;
    document.getElementById("modalMain").innerHTML = mainNode.innerHTML;
    document.getElementById("modalSub").innerHTML = subNode.innerHTML;
    document.getElementById("modalText").innerHTML = textNode.innerHTML;

    document.getElementById("portfolioModal").style.display = "block";


}

document.getElementById("modalClose").addEventListener("click", function(){
    document.getElementById("portfolioModal").style.display = "none";
});

var filterItems = document.getElementsByClassName("overlay");

for(var i=0; i<filterItems.length; i++){
    filterItems[i].addEventListener("click", viewPortfolio);
}

/* REVIEW AREA */
var reviewSlideIndex = 0;

function reviewSlideTimer(){
    plusReviewSlides(1);
}
var reviewTimer = setInterval(reviewSlideTimer, 3000); // 3초마다 리뷰 슬라이드 넘기기

function plusReviewSlides(n){
    clearInterval(reviewTimer); // 기존 타이머 제거
    reviewTimer = setInterval(reviewSlideTimer, 3000); // 새로운 타이머 설정
    showReviewSlides(reviewSlideIndex += n);
}
function showReviewSlides(n){
    var i;
    var review_slides = document.getElementsByClassName("review-slide"); // 모든 리뷰 슬라이드 요소들
    const SHOWPAGE = 3; // 한 번에 보여줄 리뷰 슬라이드 개수

    if(n >= review_slides.length - SHOWPAGE){
        reviewSlideIndex = 0; // 처음으로 돌아감
    }
    if(n < 0){
        reviewSlideIndex = review_slides.length - SHOWPAGE; // 마지막으로 감
    }

    for(i=0; i<review_slides.length; i++){
        removeClass(review_slides[i], "show");
        removeClass(review_slides[i], "res-show");
        addClass(review_slides[i], "hide");
    }

    removeClass(review_slides[reviewSlideIndex], "hide");
    addClass(review_slides[reviewSlideIndex], "res-show");

    var reviewnextSlideIndex = reviewSlideIndex;
    for(i=1; i<SHOWPAGE; i++){
        reviewnextSlideIndex = (reviewSlideIndex + i) % review_slides.length;
        removeClass(review_slides[reviewSlideIndex + i], "hide");
        addClass(review_slides[reviewSlideIndex + i], "show");
    }
}

document.getElementById("reviewPrev").addEventListener("click", plusReviewSlides.bind(null, -1));
document.getElementById("reviewNext").addEventListener("click", plusReviewSlides.bind(null, 1));

/* NAVBAR ANCHOR */
function moveTo(id){
    if(id == 'brand'){
        window.scrollTo({top: 0, behavior: 'smooth'});
    } else{
        window.scrollTo({top: document.getElementById(id).offsetTop - 70, behavior: 'smooth'});
    }

    document.getElementById("menu").classList.remove("show");
}

document.getElementById("navbarBrand").addEventListener("click", moveTo.bind(null, 'brand'));
document.getElementById("navbarAbout").addEventListener("click", moveTo.bind(null, 'about'));
document.getElementById("navbarService").addEventListener("click", moveTo.bind(null, 'service'));
document.getElementById("navbarPortfolio").addEventListener("click", moveTo.bind(null, 'portfolio'));
document.getElementById("navbarReview").addEventListener("click", moveTo.bind(null, 'review'));