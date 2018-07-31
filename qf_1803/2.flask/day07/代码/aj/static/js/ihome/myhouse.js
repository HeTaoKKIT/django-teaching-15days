$(document).ready(function(){
    $(".auth-warn").show();

    $.get('/house/house_info/', function(data){
        if(data.code == '200'){
            $('.auth-warn').hide()
        }else{
           $('#houses-list').hide()
        }
    });
})