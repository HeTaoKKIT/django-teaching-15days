$(document).ready(function(){
    $(".auth-warn").show();
})


$(document).ready(function(){

    $.get('/house/house_info/', function(data){
        if(data.code == '200'){
            $('.auth-warn').hide()
            $('#houses-list').show()
        }
        if(data.code == '1013'){
            $('.auth-warn').show()
            $('#houses-list').hide()
        }
    })
})