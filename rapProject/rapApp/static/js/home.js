var input = document.querySelector(".input");

function isValidSubmit() {
    console.log(input.value);
    if (input.value.length == 0) {
        alert("닉네임을 입력하세요!");
        return false;
    }
}

function TimeCompare(id, dateOpen, dateClose){
    var Timer;
    var openDate = new Date(dateOpen);
    var closeDate = new Date(dateClose);
    var now = new Date();
    var distOpen = openDate - now;
    var distClose = closeDate - now;
    if (distOpen <= 0 && distClose >= 0){
        var id = document.querySelector(id).disabled = false;
    }
    

}
// TimeCompare('.rapper_btn','09/24/2020 00:00 AM', '09/25/2020 02:00 AM');
// TimeCompare('.audience_btn','09/25/2020 02:00 AM', '09/25/2020 03:00 AM');
// TimeCompare('.result_btn','09/25/2020 03:00 AM', '09/26/2020 00:01 AM');