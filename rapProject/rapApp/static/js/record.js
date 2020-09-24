function play() { 
    var audio = document.getElementById('beat_play'); 
    if (audio.paused) { 
        audio.play(); 
    }else{ 
        audio.pause(); 
        audio.currentTime = 0 
    } 
} 