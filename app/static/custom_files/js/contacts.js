
$("#edit_contact").click(function(){
    $(this).hide();
    $("#cancel_edit_contact").show();
    $("#save_edit_contact").show();
    $(".disabled_form_elements input, .disabled_form_elements select, .disabled_form_elements checkbox").prop("disabled", false);
});


$("#cancel_edit_contact").click(function(){
    $(this).hide();
    $("#edit_contact").show();
    $("#save_edit_contact").hide();
    $(".disabled_form_elements input, .disabled_form_elements select, .disabled_form_elements checkbox").prop("disabled", true);
});


function has_app_id(elem){
    $("#app_id_input").find("input").val("");

    if($(elem).prop("checked") == true){
        $("#app_id_input").removeClass("hide-row").addClass("show-row");
    }
    else if($(elem).prop("checked") == false){
        $("#app_id_input").removeClass("show-row").addClass("hide-row");
    }
}

//******************************************* 
//  CHECK IF APPLICATION ID EXISTS 
//********************************************

function check_app_id(elem){

    csrf = $("form").find("input[name='csrfmiddlewaretoken']").val();


    if($(elem).val()!=""){
        $.post('/contacts/check_appid/',{'id':$(elem).val(), 'csrfmiddlewaretoken':csrf}, function(data){
            
            data = JSON.parse(data);

            if(data["ret"] == 0){ 
                alert('Invalid Application ID');
                $("#id_app_id_check").empty().append('<i class="fa fa-fw fa-times" style="color: #ff0000;"></i>');
            }
            if(data["ret"]=='1'){
                $("#id_app_id_check").empty().append('<i class="fa fa-fw fa-check" style="color: #11640b;"></i>');
            }
        });
    }
}