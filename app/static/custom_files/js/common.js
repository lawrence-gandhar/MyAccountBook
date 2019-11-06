$(document).ready(function(){

    $("#accordionSidebar li.nav-item").each(function(){
        
        $("#accordionSidebar li.nav-item").removeClass("active");

        link_text = $(this).find("a.nav-link").find("span").text();

        if(active_link === link_text){
            console.log($(this).find("a.nav-link").find("span").text()+" === "+active_link);

            $(this).addClass("active");
            return false;
        }
    });

})