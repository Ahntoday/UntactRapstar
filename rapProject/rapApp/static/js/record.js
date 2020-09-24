function play(id) { 
    var audios = document.querySelectorAll('audio');
    var audio = document.getElementById(id); 
    if (audio.paused) { 
        for(var i=0;i<audios.length;i++){
            audios[i].pause();
        }
        audio.play(); 
    }else{ 
        audio.pause(); 
        audio.currentTime = 0 
    } 
} 