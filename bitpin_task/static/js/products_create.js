function createNewProduct(productTitle){
    $.ajax({
        url: '/api/products/',
        method: 'POST',
        data: {
            'title': productTitle
        },
        success: function(response){
            console.log("moving");
            window.location = '/'; 
        },
        error: function(response){
            alert("something went wrong, please try again");
        }
    });
}

$(function(){
    const newProductSaveBtn = $("#new_product_save_btn");
    const new_product_txt_input = $("#new_product_txt_input");

    newProductSaveBtn.on('click', function(){
        const product_name = new_product_txt_input.val();

        if (product_name){
            createNewProduct(new_product_txt_input.val());
        }else{
            alert("enter a name");
        }
    });
});