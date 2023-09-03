document.addEventListener('DOMContentLoaded',function(){
    const newsletterForm = document.querySelector('.newsletter-subscription')
    const numberInput = newsletterForm.querySelector('input[type="number"]')
    const subscribeButton = newsletterForm.querySelector('button')

    newsletterForm.addEventListener('submit',function(event){
        event.preventDefault()

        const number = numberInput.nodeValue

        newsletterForm.innerHTML = '<p>Gysga wagt içinde siz bilen habarlaşars</p>'
    })
})

