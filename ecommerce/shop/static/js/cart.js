$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[1]
    $.ajax({
        type:'GET',
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
            eml.innerText=data.quantity
            document.getElementById('amount').innerText = data.amount
        }
    })
})

$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[1]
    var em = this
    $.ajax({
        type:'GET',
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function(data){
            eml.innerText=data.quantity
            document.getElementById('amount').innerText = data.amount
        }
    })
})


$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this
    $.ajax({
        type:'GET',
        url:"/removecart",
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById('amount').innerText = data.amount

            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})