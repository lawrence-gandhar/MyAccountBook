$(document).ready(function(){

    $("#menu li").each(function(){
      
        $("#menu li").removeClass("active");

        link_text = $(this).find("a").find("p").text();

        if(active_link === link_text){            
            $(this).addClass("active");
            return false;
        }
    });


    disabled_elems = document.querySelectorAll(".disabled_form_elements input, .disabled_form_elements select, .disabled_form_elements checkbox")

    for (var i = 0; i < disabled_elems.length; i++) {
        disabled_elems[i].disabled = !disabled_elems[i].disabled;
    }

});

//
//
//
function close_modal(elem){
    $("#wait_Modal").hide();
}
