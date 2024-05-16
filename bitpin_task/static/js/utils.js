function loadContentByURL(url, holderID, itemCreatorCallBack, show_more_btn_id){
    const holderElement = $("#" + holderID);
    const showMoreBtn = $("#" + show_more_btn_id);

    $.ajax({
        url: url,
        success: function(response){
            if (!response['count']){
                holderElement.html("Nothing to show");
            }

            response['results'].forEach(function(item){
                holderElement.append(
                    itemCreatorCallBack(item)
                );
            });

            if (response['next']){
                showMoreBtn.show();
                showMoreBtn.unbind('click');
                showMoreBtn.on('click', function(){
                    loadContentByURL(response['next'], holderID, itemCreatorCallBack, show_more_btn_id);
                });
            }else{
                showMoreBtn.hide();
            }
            
        }
    })
}

function InitProducts(url, holderID, itemCreatorCallBack, show_more_btn_id){
    $("#"+holderID).html("");
    loadContentByURL(url, holderID, itemCreatorCallBack, show_more_btn_id);
}