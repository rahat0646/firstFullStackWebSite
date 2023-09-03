
$('.plus-wishlist').click(function(){
    var id=$(this).attr("pid").toString()
    var name=$(this).attr("pname").toString()
    var brandname=$(this).attr("pbname").toString()
    $.ajax({
        type:'GET',
        url:'/pluswishlist',
        data:{
            prod_id:id
        },
        success:function(data){
            window.location.href = `/product/${id}/${brandname}${name}`
        }
    })
})

$('.minus-wishlist').click(function(){
    var id=$(this).attr("pid").toString()
    var name=$(this).attr("pname").toString()
    var brandname=$(this).attr("pbname").toString()
    $.ajax({
        type:'GET',
        url:'/minuswishlist',
        data:{
            prod_id:id
        },
        success:function(data){
            window.location.href = `/product/${id}/${brandname}-${name}`
        }
    })
})