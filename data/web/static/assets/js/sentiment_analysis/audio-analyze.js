$(document).ready(function(){
    $("#datatablesSimple").on('click','.btnSelect',function(){
        
        let id_audio = ($(this).attr("value"));
        
        let td_button_parent = $(this).parent();
        let tr_parent = td_button_parent.parent();
        let td_div_child = tr_parent.children("td").eq(1); // Contains the sentiment analysis score
       
        let button_div_child = $(this).children("div").eq(0);; 
        button_div_child.css("display", "inline-block");
        
        //   initializes an empty FormData
        let data = new FormData();
        //   appends the recorded file 
        data.append("id_audio", id_audio);
        console.log(id_audio)
        
        $.ajax({
            url: "/audio_analyze/",
            method: "POST",
            data: data,
            dataType: 'json',
            success: function (response) {
                console.log("POST SUCCESS", response)
                result_sentiment_analysis = response["data"]["body"]["score"]
            },
            complete: function (response){
                button_div_child.css("display", "none");
                td_div_child.html(result_sentiment_analysis);
            },
            error: function (error) {
                console.error(error);
            },
            cache: false,
            processData: false,
            contentType: false,
        })
        
    });
});

$(document).ready(function(){
    $("#datatablesSimple").on('click','.btn-danger',function(){
        
        let id_audio = ($(this).attr("value"));
        
        //   initializes an empty FormData
        let data = new FormData();
        //   appends the recorded file 
        data.append("id_audio", id_audio);
        console.log(id_audio)
        
        $.ajax({
            url: "/audio_delete/",
            method: "POST",
            data: data,
            dataType: 'json',
            success: function (response) {
                console.log("POST SUCCESS", response)
                location.reload();
            },
            error: function (error) {
                console.error(error);
            },
            cache: false,
            processData: false,
            contentType: false,
        })
        
    });
});