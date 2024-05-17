function showProductData(product_id){
    const productNameElem = $("#product_name_elem");

    $.ajax({
        url: '/api/products/' + String(product_id),
        success: function(response){
            productNameElem.html(response['title']);
        }
    })
}

function convertNumberToRating(rating){
    return "★".repeat(rating) + "☆".repeat(5-rating);
}

function saveRating(product_id, rating){
    $.ajax({
        url: `/api/products/${product_id}/ratings/`,
        method: 'post',
        data: {
            product_id: product_id,
            rating: rating
        },
        success: function(response){
            InitListData(`/api/products/${product_id}/ratings`, "rating_list", createRatingItem, "ratings_show_more");
        }
    });
}

function createRatingItem(ratingData){
    return `
        <div>
            ${convertNumberToRating(ratingData['rating'])} 
            (${ratingData['rating']} stars) 
            - by ${ratingData['user']['username']}
        </div>
    `;
}

$(function(){
    const product_id = $("#product_id_holder").val();
    showProductData(product_id);
    
    InitListData(`/api/products/${product_id}/ratings`,
                "rating_list", createRatingItem,
                "ratings_show_more");

    $("#save_rating").on('click', function(){
        const selected_rating = Number($("#rating_select").val());
        saveRating(product_id, selected_rating);
    });
});