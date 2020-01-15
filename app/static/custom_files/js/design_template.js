$(document).ready(function(){

    $("button.color-button").on('click', function(){
        var x = $(this).text();

        var backgrounds = {
            "1" : "template_header",
            "2" : "template_header_orange",
            "3" : "template_header_blue",
        };

        $("#invoice_template_body").find(".card-header").removeClass().addClass("card-header").addClass(backgrounds[x]);
        

    });



});

