$("#app_id_input_2").removeClass("show-row").addClass("hide-row");

$("#more_address_table").find("input").attr('disabled', "true");
$("#more_address_table").find("select").attr('disabled', "true");

$("#tr-id_user_address_details_set-tr-0 td:nth-child(2)").find("table > tbody tr:nth-child(1)").hide();


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



/****************************************************************/
// Add Address Block
/****************************************************************/

$("#add_more_addresses").on("click",function(){

    inc = $("#id_user_address_details_set-TOTAL_FORMS").val();

    htm_all = '';

    htm = $("tr#tr-id_user_address_details_set-tr-0").html();

    htm_all = '<tr>';
    htm_all += '<td style="padding-top:10px; color:#FF0000; border:0px; border-bottom:3px solid #ccc;" colspan="2">';
    htm_all += '<i class="material-icons pull-right" style="cursor:pointer;" onclick="delete_address_block($(this),'+(parseInt(inc)-1)+')">delete_forever</i></td></tr>';
    htm_all += '<tr id="tr-id_user_address_details_set-tr-'+(parseInt(inc)-1)+'">'+htm+'</tr>';

    ids = parseInt(inc) + 1;
    row_num = 0;
    
    htm_all = htm_all.replace(/user_address_details_set-0/g, "user_address_details_set-"+ids);
    htm_all = htm_all.replace(/user_address_details_set-1/g, "user_address_details_set-"+parseInt(ids + 1));
    
    $("#address_table > tbody").append(htm_all);

    $("#tr-id_user_address_details_set-tr-"+(parseInt(inc)-1)+" td:nth-child(2)").find("table > tbody tr:nth-child(1)").hide();

    $("#id_user_address_details_set-TOTAL_FORMS").val(parseInt(inc) + 2);

});



/****************************************************************/
// Remove Address Block
/****************************************************************/

function delete_address_block(elem, ids){
    inc = $("#id_user_address_details_set-TOTAL_FORMS").val();
    $(elem).closest('tr').remove();
    $("#tr-id_user_address_details_set-tr-"+ids).remove();
    $("#id_user_address_details_set-TOTAL_FORMS").val(parseInt(inc) -2);
}


$(".disabled-tr").find("input").attr("disabled","true");
$(".disabled-tr").find("select").attr("disabled","true");

$(".set_required").find("input").attr("required", "true");
$(".set_required").find("select").attr("required", "true");

$("#editAccountsModal").find("input").attr("required", "true");


/********************************************************************/
// Billing Clicked
/********************************************************************/

function billing_clicked(elem){

    var ids = $(elem).attr("id");

    ids = ids.replace("id_user_address_details_set-", "").replace("-is_billing_address", "");

    if(ids == 0){
        
    }


    if($(elem).prop("checked") == true){
        alert("its true");
    }else{
        alert("its false");
    }
    
}