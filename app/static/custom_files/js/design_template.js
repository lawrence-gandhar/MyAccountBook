$(document).ready(function(){

    $("button.color-button").on('click', function(){
        var x = $(this).text();

        var backgrounds = {
            "1" : ["template_header", "template_body_green", "th_green"],
            "2" : ["template_header_orange", "template_body_orange", "th_orange"],
            "3" : ["template_header_blue", "template_body_blue", "th_blue"],
            "4" : ["template_header_white", "template_body_white", "th_white"],
            "5" : ["template_header_grey", "template_body_grey", "th_grey"],
        };

        $("#invoice_template_body").find(".card-header").removeClass().addClass("card-header").addClass(backgrounds[x][0]);
        $("#template_body").removeClass().addClass("card-body").addClass(backgrounds[x][1]);
        $("#address_bar").removeClass().addClass(backgrounds[x][2])
    });



});

