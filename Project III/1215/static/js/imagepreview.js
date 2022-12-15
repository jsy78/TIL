function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();
        // 이벤트 결과를 src에 집어넣음
        reader.onload = function (e) {
        $('#image_section').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#imgInput").off().on("change", function(){

    if (this.files && this.files[0]) {

        var maxSize = 5 * 1024 * 1024;
        var fileSize = this.files[0].size;

        if(fileSize > maxSize){
        alert("사진 용량 5MB 이내로 등록 가능합니다.");
        $(this).val('');
        return false;
        } else {
        readURL(this);
        }
    }
});