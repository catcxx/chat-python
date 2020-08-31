(function($){
    // Settings
    var repeat = localStorage.repeat || 0,
        shuffle = localStorage.shuffle || 'false',
        continous = true,
        autoplay = true,
        playlist=[];
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth()+1;
    var day = date.getDate();
    var hour = date.getHours();
    var minute = date.getMinutes();
    var second = date.getSeconds();
    var dataStr=year+'年'+month+'月'+day+'日 '+hour+':'+minute+':'+second;
    playlist = [
        {
            title: '欢迎你呀！快来和我聊聊天呐！！现在时间是: '+dataStr,
            artist: 'CXX&CF'
        }];

    function send(msg) {
        var tmp={
            "info":msg
        };

        $.ajax({
            url: 'http://47.110.38.123:329/chat',
            type: "POST",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(tmp),
            async: false,
            success: function (r) {
                console.log("----------------------获取的数据--------------------"+r);
                var tmp={
                    title: r,
                    artist: "CXX&CF"
                };
                playlist=[];
                playlist.push(tmp);
                load();
            }
        });
    }


    // Load playlist
    load();
    function load() {
        for (var i=0; i<playlist.length; i++){
            var item = playlist[i];
            $('#playlist').append('<li>'+item.artist+' - '+item.title+'</li>');
        }
    }

    $("#btSend").click(function () {
        playlist=[];
        var value=$("#inputValue").val();
        var tmp={
            title: value,
            artist: "visitor",
            album: value,
            cover:value,
            mp3: value
        };
        playlist.push(tmp);
        load();
        send(value);
        $("#inputValue").val("");
    });

})(jQuery);
