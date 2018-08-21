

function addToCart(good_id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/home/add_to_cart/',
        type:'POST',
        dataType:'json',
        data:{'goods_id': good_id},
        headers:{'X-CSRFToken': csrf},
        success:function(data){
            console.log(data.data.c_num)
            $('#num_'+good_id).html(data.data.c_num)
        }
    })
}