function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $.get('/house/area_facility/', function(data){
        if(data.code == '200'){
            for(var i=0; i<data.areas.length; i++){
                area_str = '<option value="' + data.areas[i].id + '">' + data.areas[i].name + '</option>'
                $('#area-id').append(area_str)
            }

            for(var j=0; j<data.facilitys.length; j++){
                facility_str = '<li><div class="checkbox"><label>'
                facility_str += '<input type="checkbox" name="facility" value="' + data.facilitys[j].id + '">' + data.facilitys[j].name
                facility_str += '</label></div></li>'

                $('.house-facility-list').append(facility_str)
            }

        }
    });
});