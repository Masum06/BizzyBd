$('#theme_form').hide();

$(function(){

    $('#publish').click(function () {
        var div1 = $('#div1').html();
        var div2 = $('#div2').html();
        var div3 = $('#div3').html();
        var url = $('#url_name').val();
        console.log("my editor value");
        // console.log(url);
        // alert(url)
        // alert(mysave);
        $('#id_div1').val(div1);
        $('#id_div2').val(div2);
        $('#id_div3').val(div3);
        $('#id_url').val(url);

        $('#theme_form').submit();

    });
});




$(function(){
    $(document).ready(function() {
    	$("#url_name").bind('keyup', check_url);
    });
});  

function check_url()
{
  var url = $("#url_name").val();
  $.ajax({
          "type"     : "GET",
          "url"      : "/ajax_request/url/?url=" + url,
          "dataType" : "json",
          "cache"    : false,
          "success"  : function(json) {
          	  $('#url_status').text(json['status']);
          }           
  });

}