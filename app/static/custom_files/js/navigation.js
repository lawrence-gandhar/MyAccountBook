
$(document).ready(function(){

    $("#accordionSidebar li.nav-item").each(function(){
        
        $("#accordionSidebar li.nav-item").removeClass("active");

        if($(this).find("a").text() == active_link){
            $(this).addClass("active");
        }
    });




})