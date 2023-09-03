const slides = document.querySelectorAll('.slide')
const bottom_slider = document.querySelectorAll('.bottom')
const navPills = document.querySelectorAll('.nav-pills li')
const prevBanButton = document.querySelector('.prev-ban-button')
const nextBanButton = document.querySelector('.next-ban-button')
let currentSlide = 0

slides[currentSlide].style.display = 'block'

// navPills[currentSlide].classList.add('active')
bottom_slider[currentSlide].classList.add('active')

function showSlide(index,i) {
    slides.forEach((slide)=>{
        slide.classList.remove('active')
    })

    // navPills.forEach((pill) => {
    //     pill.classList.remove('active')
    // })

    bottom_slider.forEach((image)=>{
        image.classList.remove('active')
    })

    slides[index].classList.add('active')
    bottom_slider[index].classList.add('active')


    // navPills[index].classList.add('active')
}
setInterval(function () {
    currentSlide = (currentSlide + 1) % slides.length
    showSlide(currentSlide)
}, 3000);

function nextSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length
    showSlide(currentSlide)
}

function prevSlide() {
    currentSlide = (currentSlide + 1) % slides.length
    showSlide(currentSlide)
}



// prevBanButton.addEventListener('click',prevSlide)
// nextBanButton.addEventListener('click',nextSlide)

$(document).ready(function(){
    $('.slider-pro').slick({
        slidesToShow:4,
        slidesToScroll:1,
        autoplay:true,
        autoplaySpeed:3000,
        responsive:[
        {
            breakpoint:768,
            settings:{
                slidesToShow:2
            }
        },
        {
            breakpoint:280,
            setting:{
                slidesToShow:1
            }
        },

    ]
    })
    $('.slider-pro-prev').click(function(){
        $('.slider-pro').slick('slickPrev')
    })
    $('.slider-pro-next').click(function(){
        $('.slider-pro').slick('slickNext')
    })
})

$(document).ready(function(){
    $('.slider-brand').slick({
        slidesToShow:4,
        slidesToScroll:1,
        autoplay:true,
        autoplaySpeed:3000,
        responsive:[
        {
            breakpoint:768,
            settings:{
                slidesToShow:2
            }
        },
        {
            breakpoint:280,
            setting:{
                slidesToShow:1
            }
        },

    ]
    })
})
