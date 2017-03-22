$(document).ready(function () {
	$('.color').colorPicker( /* optinal options */ );
    var x = 0;
    $("#addabout").click(function(){
        
    	var add = `<div id="added`+x+`" class="col-xs-12 color" contenteditable="true">
            Some text
        </div>`;
        $("#about .container-fluid").append(add);
//        var id = 'added'+
        CKEDITOR.inline('added'+x);
        x=x+1;
        $('.color').colorPicker( /* optinal options */ );
    });
});