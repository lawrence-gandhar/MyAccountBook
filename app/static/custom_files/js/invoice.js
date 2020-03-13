$(document).ready(function(){

    $("#tr-set-0").find("i").hide();

})

//********************************************************************************* */
// ADD PRODUCT TO INVOICE
//********************************************************************************** */
//
$("#add_shopping_cart").on("click", function(){

    var tr_html = $("tr#tr-set-0").html();
    var rowCount = $('#product_table tr').length;

    tr_html = tr_html.replace(/invoiceproducts_set-0/g, "invoiceproducts_set-"+(rowCount-1));
    tr_html = tr_html.replace(/id_invoiceproducts_set-0/g, "id_invoiceproducts_set-"+(rowCount-1));

    new_html = '<tr id="tr-set-'+(rowCount-1)+'"></tr>';
    $('#product_table tbody').append(new_html);
    $("#tr-set-"+(rowCount-1)).empty().append(tr_html);

    $("#tr-set-"+(rowCount-1)).find("i").show();

    $("#id_invoiceproducts_set-TOTAL_FORMS").val(rowCount);

});

//**************************************************************************************** */
// DELETE PRODUCT FORM
//**************************************************************************************** */
//

function delete_product_from_invoice_form(elem){
    var tr = $(elem).parents('tr');    

    if(tr.attr("id") != 'tr-set-0'){
        $("#"+tr.attr("id")).remove();
        var rowCount = $('#product_table tr').length;
        $("#id_invoiceproducts_set-TOTAL_FORMS").val(rowCount);
        console.log($("#id_invoiceproducts_set-TOTAL_FORMS").val());
    }
}

//**************************************************************************************** */
// FETCH CONTACTS DETAILS
//**************************************************************************************** */
//

$("select#id_service_recipient").on("change", function(){

    var ids = $(this).val();

    $.get('/fetch_contact_addresses/'+ids+'/', function(data){
        data = $.parseJSON(data);

        var htm = '';

        $.each(data.addresses, function(i,v){
            htm += '<p style="font-weight:bold; margin:0px">'+v.flat_no+', ';
            htm += v.street+', ';
            htm += v.city+', ';
            htm += v.state+', ';
            htm += +v.country+', ';
            htm += v.pincode+'</p>';
        });

        $("td#contact_addresses").empty().append(htm);
        $("td#organization_name").empty().text(data.organization_name);

    });
});

//**************************************************************************************** */
// FETCH PRODUCT DETAILS
//**************************************************************************************** */
//

function get_product_details(elem){

    ids = $(elem).val();
    atr = $(elem).attr("id");

    atr = atr.replace("id_invoiceproducts_set-","")
    atr = atr.replace("-product","")

    $.get('/fetch_product_details/'+ids+'/', function(data){
        data = $.parseJSON(data);

        $("#id_invoiceproducts_set-"+atr+"-producttype").val(data.product_type);

        quantity_in_stock_html = '';
        for(i=0; i <= data.quantity_in_stock; i++){
            quantity_in_stock_html += '<option>'+i+'</option>';
        }

        $("#id_invoiceproducts_set-"+atr+"-quantity").empty().append(quantity_in_stock_html);
        $("#id_invoiceproducts_set-"+atr+"-price").val(data.details[0].selling_price);
        $("#id_invoiceproducts_set-"+atr+"-discount").val(data.details[0].discount);
        $("#id_invoiceproducts_set-"+atr+"-tax").val(data.details[0].gst+"%");        
    });
}

//**************************************************************************************** */
//
//**************************************************************************************** */
//

function product_quantity(elem){
    atr = $(elem).attr("id");

    atr = atr.replace("id_invoiceproducts_set-","");
    atr = atr.replace("-quantity","");

    subtotal = $(elem).val() * $("#id_invoiceproducts_set-"+atr+"-price").val();
    $("#id_invoiceproducts_set-"+atr+"-subtotal").val(subtotal);
  
    //
    var np_forms = $("#id_invoiceproducts_set-TOTAL_FORMS").val();

    sum = 0;
    for(i=0; i<np_forms; i++){
        sum += parseInt($("#id_invoiceproducts_set-"+i+"-subtotal").val());
    }

    $("#id_subtotal").val(sum);
    $("#id_total").val(sum);
}

//**************************************************************************************** */
//
//**************************************************************************************** */
//
$("#id_invoice_type").on("change", function(){
    $("tr#tr-recurring").hide();
    if($(this).val()==1) $("tr#tr-recurring").show();
});


//**************************************************************************************** */
//
//**************************************************************************************** */
//
function ajax_add_product(){
    $.post("/ajax_add_product/", $("#addProductModal_form").serialize(), function(data){
        $.get("/fetch_products_dropdown/", function(data){
            $(".product_dropdown_select").empty().append(data);
        });
    });
}
