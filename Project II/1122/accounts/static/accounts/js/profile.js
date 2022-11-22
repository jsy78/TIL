//메뉴 움직임
$(function () {
    $(".tab-content").hide();
    $(".tab-content:first").show();

    $("ul.personal-tabs li").click(function () {
        $("ul.personal-tabs li").removeClass("active").css("color", "#ffffff");
        $(this).addClass("active").css("color", "#ECE7B4");
        $(".tab-content").hide()
        var activeTab = $(this).attr("rel");
        $("#" + activeTab).fadeIn()
    });
});