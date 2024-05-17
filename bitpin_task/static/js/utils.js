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


function getCSRFToken(){
    $.ajaxSetup({ 
        beforeSend: function(xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        } 
   });
}
function InitListData(url, holderID, itemCreatorCallBack, show_more_btn_id){
    $("#"+holderID).html("");
    loadContentByURL(url, holderID, itemCreatorCallBack, show_more_btn_id);
}

$(function(){
    getCSRFToken();
});