
$("#id_is_sales").on("click", function(){
    if($(this).prop("checked") === true){
        $("#id_marked_price, #id_sales_account, #id_discount, #id_selling_price").prop("disabled", false);
    }else{
        $("#id_marked_price").prop("disabled", true);
        $("#id_marked_price , #id_sales_account, #id_discount, #id_selling_price").prop("disabled", true);
    }
});


$("#id_is_purchase").on("click", function(){
    if($(this).prop("checked") === true){
        $("#id_cost_price, #id_purchase_account").prop("disabled", false);
    }else{
        $("#id_cost_price, #id_purchase_account").prop("disabled", true);
    }
});