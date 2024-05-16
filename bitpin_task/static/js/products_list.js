function createProductItem(ProductData){
    return `
        <div class="product-item">
            ${ProductData['title']}
        </div>
    `
}

$(function(){
    InitListData("/api/products?page_size=5", "products_list", createProductItem, "products_show_more");
});