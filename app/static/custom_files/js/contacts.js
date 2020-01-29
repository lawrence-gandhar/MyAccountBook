
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

$("#app_id_input_2").removeClass("show-row").addClass("hide-row");

//******************************************* 
//  CHECK IF APPLICATION ID EXISTS 
//********************************************

function check_app_id(elem){

    csrf = $("form").find("input[name='csrfmiddlewaretoken']").val();

    if($(elem).val()!=""){
        $("#wait_Modal").show();
        $("#wait_Modal").find("#loader_container").show();
        $("#wait_Modal").find("#modal-text").empty()

        $.post('/contacts/check_appid/',{'id':$(elem).val(), 'csrfmiddlewaretoken':csrf}, function(data){

            data = JSON.parse(data);

            if(data.ret == 0){ 
                
                $("#wait_Modal").find("#modal-text").html('<span style="color:#FF0000; font-weight:bold">Invalid Application ID</span>');              
                $("#id_app_id_check").empty().append('<i class="fa fa-fw fa-times" style="color: #ff0000;"></i>');
                $("#app_id_input_2").removeClass("show-row").addClass("hide-row");
                $("#success_svg").hide();
                $("#failure_svg").show().css("display", "block");
            }
            if(data.ret =='1'){
                $("#id_app_id_check").empty().append('<i class="fa fa-fw fa-check" style="color: #11640b;"></i>');
                $("#wait_Modal").find("#modal-text").html('<span style="color:#00cc00; font-weight:bold">Found Application ID</span>');              
                $("#app_id_input_2").removeClass("hide-row").addClass("show-row");
                $("#failure_svg").hide();
                $("#success_svg").show().css("display", "block");
                $("#id_imported_user").val(data.id)
            }

            $("#svg_container").show();
            $("#wait_Modal").find(".modal-title").empty().text("Result");
            $("#wait_Modal").find("#loader_container").hide();
        });
    }
}

$("#id_is_imported_user").on("click", function(){

    if($(this).prop("checked") === true){

        csrf = $("form").find("input[name='csrfmiddlewaretoken']").val();

        $.post('/contacts/user_exists_in_list/',{'id':$("#id_imported_user").val(), 'csrfmiddlewaretoken':csrf}, function(data){
                        
            if(data == 0){
                var r = confirm("Do you want to use the existing details of this user as the contact details");
                if (r === true) {
                    $("#id_contact_name").val('Existing App User');
                }else{
                    $(this).prop("checked", false);
                }
            }
            if(data >=1){
                var r = confirm("A user with the same AppId exists in your contact list. Do you still want to create a new contact?");
                if (r === true) {
                    $("#id_contact_name").val('Existing App User');
                }else{
                    $(this).prop("checked", false);
                }
            }
        });
    }
});
