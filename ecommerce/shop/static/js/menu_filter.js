$(document).ready(function(){
    $(".ajaxLoader").hide()
    $("input[name='price-range']").click(function() {
        var range = $(this).val().split('-');
        $("#minPrice").val(range[0]);
        $("#maxPrice").val(range[1]);
    });
    
    $(".filter-checkbox,#priceFilterBtn,#search-btn,#sort-form input").on('click',function(){
        var _filterObj = {}
        var _minPrice = $("#minPrice").val()
        var _maxPrice = $('#maxPrice').val()
            _filterObj.minPrice=_minPrice
            _filterObj.maxPrice=_maxPrice
        var _selectedSort = $('input[name=sort]:checked', '#sort-form').val();
                console.log(_selectedSort)
                _filterObj.selectedSort = _selectedSort
        $(".filter-checkbox").each(function(index,ele){
            var _filterVal=$(this).val()
            var _filterKey=$(this).data('filter')
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')
                ).map(function(el){
                return el.value
            })
        })
        $.ajax({
            url:'/menu/{%for pro in product%}{% if forloop.first%}{{pro.category.menu.id}}/{{pro.category.menu.name}}{%endif%}{%endfor%}/filter-data',
            data:_filterObj,
            dataType:'json',
            beforeSend:function(){
                $(".ajaxLoader").show()
            },
            success:function(res){
                console.log(res)
                $("#filteredProducts").html(res.data)
                $(".ajaxLoader").hide()
            }
        })
    })
    })