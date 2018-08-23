

function addToCart(good_id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/home/add_to_cart/',
        type:'POST',
        dataType:'json',
        data:{'goods_id': good_id},
        headers:{'X-CSRFToken': csrf},
        success:function(data){
            goods_count()
            $('#num_'+good_id).html(data.data.c_num)
        }
    })
}

function subToCart(goods_id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/home/sub_to_cart/',
        dataType:'json',
        data:{'goods_id':goods_id},
        headers:{'X-CSRFToken': csrf},
        type: 'POST',
        success: function(data){
            goods_count()
            if(data.c_num == '0'){
//            第一种方式：强刷整个页面
//                location.reload()
//            第二种方式：删除商品个数为0的元素,移除整个li
                $('#cart_' + goods_id).remove()
            }else{
                $('#num_' + goods_id).html(data.c_num)
            }
        }
    })

}

$.get('/home/refresh_goods/', function(d){
    if(d.code == '200'){
        for(var i=0; i<d.data.length;i++){
            $('#num_'+ d.data[i][0]).html(d.data[i][1])
        }
    }
})

function change_goods_status(goods_id){

    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/home/change_cart_goods/',
        type:'POST',
        dataType:'json',
        headers:{'X-CSRFToken': csrf},
        data:{'goods_id': goods_id},
        success:function(data){

            if(data.code == '200'){
                goods_count()
                if(data.is_select){
                    $('#cart_goods_select_' + goods_id).html('√')
                }else{
                    $('#cart_goods_select_' + goods_id).html(' ')
                }
                if(data.all_select){
                    $('#all_select').html('√')
                }else{
                    $('#all_select').html('')
                }
            }
        }
    })
}

function goods_count(){
    $.get('/home/goods_count/', function(data){
        if(data.code == '200'){
            $('#goods_money').html('总价：'+ data.sum_money)
        }
    })
}
goods_count()

function all_select_goods(i){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/home/change_all_cart_goods/',
        type:'POST',
        data:{'all_select': i},
        dataType:'json',
        headers:{'X-CSRFToken':csrf},
        success:function(data){
            goods_count()
            if(i == '1'){
                s = '<span  style="height:30px;" id="all_select" onclick="all_select_goods(0)">√</span>'
            }else{
                s= '<span  style="height:30px;" id="all_select" onclick="all_select_goods(1)"></span>'
            }
            $('#change_all_select').html(s)
            for(var j=0; j<data.all_goods_id.length;j++){
                if( i == '1'){
                     $('#cart_goods_select_' + data.all_goods_id[j]).html('√')
                }else{
                    $('#cart_goods_select_' + data.all_goods_id[j]).html('')
                }
            }
        }
    })
}