$(document).ready( function() {
$('form').submit(function(){
    
   
   $.ajax({
            type: "POST",
            url: "sev_days/",
            data: $("#dateform").serialize(),
            dataType : "json"
          })
            .done(function(data) {
               var trHTML = '';
               for (var i in data.zn1) {
               trHTML += '<tr class="success" style="font-size:75%"><td>' + '('+data.cur_day+')' + '</td>' + '<td>' + data.zn1[i] + '</td>' + '<td>' + data.zn2[i] + '</td>' + '<td>' + data.zn3[i] + '</td>' + '<td>' + data.zn4[i] + '</td>' + '<td>' + data.zn1[i] + '</td>' + '<td>' + data.zn2[i] + '</td>' + '<td>' + data.zn3[i] + '</td>' + '<td>' + data.zn4[i] + '</td></tr>';
               }
                $('#data_time').html(trHTML);
                alert("Data Saved" + data.zn1);
                $('#info').html(data.zn1[0]);
                });            
               
               
               return false;
               
       
    });
});

/* 
            success: function(data){
               var trHTML = '';
               for (var i in data.zn1) {
               trHTML += '<tr class="success" style="font-size:75%"><td>' + data.ftime[i]+' '+'('+data.cur_day+')' + '</td>' + '<td>' + data.zn1[i] + '</td>' + '<td>' + data.zn2[i] + '</td>' + '<td>' + data.zn3[i] + '</td>' + '<td>' + data.zn4[i] + '</td>' + '<td>' + data.zn1[i] + '</td>' + '<td>' + data.zn2[i] + '</td>' + '<td>' + data.zn3[i] + '</td>' + '<td>' + data.zn4[i] + '</td></tr>';
               }
               $('#data_time').html(trHTML);
               $('#info').html('Everythin Ok');});
               */
               
