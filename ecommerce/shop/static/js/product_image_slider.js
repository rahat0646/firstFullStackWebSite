const slides = document.querySelectorAll('.pro-img')
const bottom_slider = document.querySelectorAll('.bot-img')
const prevImage = document.querySelector('.prev-image')
const nextImage = document.querySelector('.next-image')
let currentSlide = 0

slides[currentSlide].style.display = 'block'

bottom_slider[currentSlide].classList.add('active')

function showSlide(index,i) {
    slides.forEach((slide)=>{
        slide.classList.remove('active')
    })

    bottom_slider.forEach((image)=>{
        image.classList.remove('active')
    })

    slides[index].classList.add('active')
    bottom_slider[index].classList.add('active')
}

function nextSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length
    showSlide(currentSlide)
}

function prevSlide() {
    currentSlide = (currentSlide + 1) % slides.length
    showSlide(currentSlide)
}