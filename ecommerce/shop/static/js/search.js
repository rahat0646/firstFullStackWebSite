const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(csrf)

const SearchData = (product) => {
    $.ajax({
        type: "POST",
        url:'/search/',
        data:{
            'csrfmiddlewaretoken':csrf,
            'product':product,
        },
        success: (res)=>{
            console.log(res.data)
            const data = res.data
            if (Array.isArray(data)){
                resultsBox.classList.add('active')
                searchInput.classList.add('active')
                resultsBox.innerHTML = ''
                data.forEach(product=>{
                    resultsBox.innerHTML += `
                    <a href="/product/${product.id}/${product.brand}-${product.name}">
                        <div class="resultPro">
                            <div class="searchImage">
                                <img src="${product.image}" alt="${product.brand} ${product.description}">
                            </div>
                            <div class="searchContent">
                                <div class="brandName">${product.brand}</div>
                                <div class="productName" style="color:#009432;">${product.name}</div>
                            </div>
                            </div>
                        </div>
                    </a>
                `
                $("#button-search").html("<i class='fas fa-spinner fa-pulse mx-1'></i>")
                })
            } else {
                if (searchInput.value.length > 0) {
                    resultsBox.classList.add('active')
                    searchInput.classList.add('active')
                    $("#button-search").html("<i class='fas fa-search'></i>")
                    resultsBox.innerHTML = `<b>${data}</b>`
                } else {
                    searchInput.classList.remove('active')
                    resultsBox.classList.remove('active')
                    $("#button-search").html("<i class='fas fa-search'></i>")
                }
            }
        },
        error: (err)=>{
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup', e => {
    console.log(e.target.value)

    if (resultsBox.classList.contains('active')){
        resultsBox.classList.remove('active')
        resultsBox.style.display = 'block'
    }

    SearchData(e.target.value)
})