$(document).ready(function(){

    $("#menu li").each(function(){
        
        $("#menu li").removeClass("active");

        link_text = $(this).find("a").find("span").text();

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


function edit_form_button(form_type, obj){
    var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();

    $.post('/contacts/fetch_extra_edit_forms/', {csrfmiddlewaretoken: CSRFtoken, form_type: form_type, ins:obj}, function(data){
        data = $.parseJSON(data);
        htm = '';

        $.each(data, function(i,v){
            htm += '<div class="d-table-row" style="padding:10px 0px;">';
            htm += '<div class="d-table-cell" style="padding:0px 10px;">';
            htm += '<label style="'+v["label_style"]+'">'+v["label"]+'</label></div>';
            htm += '<div class="d-table-cell" style="padding:5px 10px;">'+v["field"]+'</div>';
            htm += '</div>';
        });

        $("#extra_form_layout").empty().append(htm);
        $("#editModal").modal("show");
    });
}



