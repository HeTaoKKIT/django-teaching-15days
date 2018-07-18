
function addgoods(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/axf/addtocard/',
        type:'POST',
        data:{'goods_id': id},
        dataType:'json',
        headers:{'X-CSRFToken': csrf},
        success:function(data){
            if(data.code=='200'){
                $('#goods_'+ id).html(data.c_num)

                get_count_price()
            }
        },
        error:function(data){
            console.log(data)
            alert('请求失败')
        }
    });
}


function subgoods(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/axf/subtocard/',
        data:{'goods_id':id},
        dataType:'json',
        type:'POST',
        headers:{'X-CSRFToken': csrf},
        success:function(data){
            if(data.code == '200'){
                $('#goods_'+ id).html(data.c_num)
                if(data.c_num == '0'){
                    $('#cart_goods_id_'+ id).remove()
                }
                get_count_price()
            }
        },
        error:function(data){
            alert('删除商品失败')
        }
    });
}

$.get('/axf/goodsnum/', function(data){
    if (data.code == '200'){
        for(var i=0;i<data.carts.length;i++){
            $('#goods_'+ data.carts[i].goods_id).html(data.carts[i].c_num)
        }
    }
})

function changeCartStatus(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/axf/changeCartStatus/',
        data:{'cart_id': id},
        dataType:'json',
        type:'POST',
        headers:{'X-CSRFToken': csrf},
        success: function(data){
            if(data.code == '200'){
                if(data.is_select){
                    s= '√'
                }else{
                    s= 'x'
                }
                $('#cart_goods_is_select_'+ id).html(s)
            }
        },
        error:function(data){
            alert('请求失败')
        }
    });
}

function get_count_price(){

    $.get('/axf/goodsCount/', function(data){
        if(data.code == '200'){
            $('#all_price').html(data.count)
        }
    });
}

get_count_price()
