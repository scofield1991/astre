$(document).ready( function() {
$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
//    $('#like_count').html(catid)
    $.get('like_category/', {point_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
       });
    });
});


$(document).ready( function() {
$('#min30').click(function(){
    var pointid;
    pointid = $(this).attr("data-pointid");
//    $('#like_count').html(catid)
    $.getJSON('time_30/', {point_id: pointid}, function(data){
               var trHTML = '';
               for (var i in data.zn1) {
               trHTML += '<tr class="success" style="font-size:75%"><td>' + data.ftime[i]+' '+'('+data.cur_day+')' + '</td>' + '<td>' + data.zn1[i]*2 + '</td>' + '<td>' + data.zn2[i]*2 + '</td>' + '<td>' + data.zn3[i]*2 + '</td>' + '<td>' + data.zn4[i]*2 + '</td>' + '<td>' + data.zn1[i] + '</td>' + '<td>' + data.zn2[i] + '</td>' + '<td>' + data.zn3[i] + '</td>' + '<td>' + data.zn4[i] + '</td></tr>';
               }
               $('#data_time').html(trHTML);
           
       });
    });
});

$(document).ready( function() {
$('#hour').click(function(){
    var pointid;
    pointid = $(this).attr("data-pointid");
//    $('#like_count').html(catid)
    $.getJSON('time_hour/', {point_id: pointid}, function(data){
               var trHTML = '';
               for (var i in data.zn1) {
               trHTML += '<tr class="success" style="font-size:75%"><td>' + data.ftime[i]+' '+'('+data.cur_day+')' + '</td>' + '<td>' + data.zn1[i] + '</td>' + '<td>' + data.zn2[i] + '</td>' + '<td>' + data.zn3[i] + '</td>' + '<td>' + data.zn4[i] + '</td>' + '<td>' + data.zn1[i] + '</td>' + '<td>' + data.zn2[i] + '</td>' + '<td>' + data.zn3[i] + '</td>' + '<td>' + data.zn4[i] + '</td></tr>';
               }
               $('#data_time').html(trHTML);
               
       });
    });
});
