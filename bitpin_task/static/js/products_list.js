function createProductItem(productData){
    return `
        <div class="product-item">
            <a href="/products/${productData['id']}">
                ${productData['title']} ${convertNumberToRating(productData['overal_rating'])} (${productData['overal_rating']})
            </a>
        </div>
    `
}

$(function(){
    InitListData("/api/products?page_size=5", "products_list", createProductItem, "products_show_more");
});