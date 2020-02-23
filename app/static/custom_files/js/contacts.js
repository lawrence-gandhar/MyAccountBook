$("#app_id_input_2").removeClass("show-row").addClass("hide-row");

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

$("#more_address_table").find("input").attr('disabled', "true");
$("#more_address_table").find("select").attr('disabled', "true");


/************************************************************ */
//
/************************************************************ */
function has_app_id(elem){

    $("#app_id_input").find("input").val("").removeClass("wrong_input");
    $("#id_app_id_check").empty();

    if($(elem).prop("checked") == true){
        $("#app_id_input").removeClass("hide-row").addClass("show-row");
    }
    else if($(elem).prop("checked") == false){
        $("#app_id_input").removeClass("show-row").addClass("hide-row");
        $("#app_id_input_2").removeClass("show-row").addClass("hide-row");
    }
}



//******************************************* 
//  CHECK IF APPLICATION ID EXISTS 
//********************************************

function check_app_id(elem){

    csrf = $("form").find("input[name='csrfmiddlewaretoken']").val();

    if($(elem).val()!=""){
        $("#wait_Modal").show();
        $("#wait_Modal").find("#loader_container").show();
        $("#wait_Modal").find("#modal-text").empty();

        $.post('/contacts/check_appid/',{'id':$(elem).val(), 'csrfmiddlewaretoken':csrf}, function(data){

            data = JSON.parse(data);

            if(data.ret == 0){ 
                
                $("#wait_Modal").find("#modal-text").html('<span style="color:#FF0000; font-weight:bold">Invalid Application ID</span>');              
                $("#id_app_id_check").empty().append('<i class="material-icons">clear</i>');
                $("#app_id_input_2").removeClass("show-row").addClass("hide-row");
                $("#success_svg").hide();
                $("#failure_svg").show().css("display", "block");
                $(elem).addClass("wrong_input");
            }
            if(data.ret =='1'){
                $("#id_app_id_check").empty().append('<i class="material-icons">check</i>');
                $("#wait_Modal").find("#modal-text").html('<span style="color:#00cc00; font-weight:bold">Found Application ID</span>');              
                $("#app_id_input_2").removeClass("hide-row").addClass("show-row");
                $("#failure_svg").hide();
                $("#success_svg").show().css("display", "block");
                $("#id_imported_user").val(data.id);
                $(elem).removeClass("wrong_input");
            }

            $("#svg_container").show();
            $("#wait_Modal").find(".modal-title").empty().text("Result");
            $("#wait_Modal").find("#loader_container").hide();
        });
    }
}

//******************************************* 
//  
//********************************************

$("#id_is_imported_user").on("click", function(){

    if($(this).prop("checked") === true){

        csrf = $("form").find("input[name='csrfmiddlewaretoken']").val();

        $.post('/contacts/user_exists_in_list/',{'id':$("#id_imported_user").val(), 'csrfmiddlewaretoken':csrf}, function(data){
                        
            if(data == 0){
                r = confirm("Do you want to use the existing details of this user as the contact details");
                if (r === true) {
                    $("#id_contact_name").val('Existing App User');
                }else{
                    $(this).prop("checked", false);
                }
            }
            if(data >=1){
                r = confirm("A user with the same AppId exists in your contact list. Do you still want to create a new contact?");
                if (r === true) {
                    $("#id_contact_name").val('Existing App User');
                }else{
                    $(this).prop("checked", false);
                }
            }
        });
    }
});


//************************************************************* */
// LOAD CONTACT FORMS FOR EDIT
//************************************************************* */
function edit_form_button(form_type, obj){
    var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();

    $.post('/contacts/fetch_extra_edit_forms/', {csrfmiddlewaretoken: CSRFtoken, form_type: form_type, ins:obj}, function(data){
        data = $.parseJSON(data);
        htm = '';

        $.each(data, function(i,v){
            htm += '<div class="d-table-row" style="padding:10px 0px;">';
            htm += '<div class="d-table-cell" style="padding:0px 10px;">';
            htm += '<label style="'+v.label_style+'">'+v.label+'</label></div>';
            htm += '<div class="d-table-cell" style="padding:5px 10px;">'+v.field+'</div>';
            htm += '</div>';
        });

        $("#extra_form_layout").empty().append(htm);
        $("#editModal").modal("show");
    });
}


/****************************************************************/
//
/****************************************************************/

$("#add_more_addresses").on("click",function(){

    console.log($(this).attr("params"));

    if($(this).attr("params") == 1){
        $("#more_address_table").find("input").removeAttr('disabled');
        $("#more_address_table").find("select").removeAttr('disabled');
        $("#more_address_table").removeClass("hide");
        $(this).attr("params","2");
        $("#more_address_table_enabled").val(1);
        $(this).text("Remove Another Address");
    }else{
        $("#more_address_table_enabled").val(0);
        $("#more_address_table").find("input").attr('disabled', "true");
        $("#more_address_table").find("select").attr('disabled', "true");
        $("#more_address_table").addClass("hide");
        $(this).attr("params","1");
        $(this).text("Add Another");
    }
});

$(".edit_contact_details_form").find("input").attr("disabled","true")
$(".edit_contact_details_form").find("select").attr("disabled","true")

$(".edit_tax_details_form").find("input").attr("disabled","true")
$(".edit_tax_details_form").find("select").attr("disabled","true")

$(".contact_address_form_1").find("input").attr("disabled","true")
$(".contact_address_form_1").find("select").attr("disabled","true")

//
//{% url 'edit_contact_details_form' %}


