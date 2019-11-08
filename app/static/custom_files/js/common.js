$(document).ready(function(){

    $("#accordionSidebar li.nav-item").each(function(){
        
        $("#accordionSidebar li.nav-item").removeClass("active");

        link_text = $(this).find("a.nav-link").find("span").text();

        if(active_link === link_text){            
            $(this).addClass("active");
            return false;
        }
    });


    disabled_elems = document.querySelectorAll(".disabled_form_elements input, .disabled_form_elements select, .disabled_form_elements checkbox")

    for (var i = 0; i < disabled_elems.length; i++) {
        disabled_elems[i].disabled = !disabled_elems[i].disabled;
    }

})