function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function(){

    $(".book-house").show();

    var search_url = location.search
    house_id = search_url.split('=')[1]
    $.get('/house/detail/' + house_id + '/', function(data){
        if(data.code == '200'){
            for(var i=0;i<data.house_detail.images.length;i++){
                var swiper_li = '<li class="swiper-slide"><img src="/static/media/' + data.house_detail.images[i] + '"></li>'
                $('.swiper-wrapper').append(swiper_li)
            }
            var mySwiper = new Swiper ('.swiper-container', {
                loop: true,
                autoplay: 2000,
                autoplayDisableOnInteraction: false,
                pagination: '.swiper-pagination',
                paginationType: 'fraction'
            })
            $('.house-price span').html(data.house_detail.price)
            $('.book-house').attr('href', '/house/booking/?house_id=' + house_id)
        }


    })
})