$(document).ready(function(){})

//********************************************************************************* */
// ADD PRODUCT TO INVOICE
//********************************************************************************** */
//
$("#add_shopping_cart").on("click", function(){

    var tr_html = $("tr#tr-set-0").html();
    var rowCount = $('#product_table tr').length;

    tr_html = tr_html.replace(/invoiceproducts_set-0/g, "invoiceproducts_set-"+rowCount);
    tr_html = tr_html.replace(/id_invoiceproducts_set-0/g, "id_invoiceproducts_set-"+rowCount);

    new_html = '<tr id="tr-set-'+rowCount+'"></tr>';
    $('#product_table tbody').append(new_html);
    $("#tr-set-"+rowCount).empty().append(tr_html);

    //$("#tr-set-"+rowCount).find("input").attr("")

});