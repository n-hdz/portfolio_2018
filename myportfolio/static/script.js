$(document).ready(function () {
 $(".scroller").click(function (e) {
     e.preventDefault();
     goToByScroll($(this).attr("data-section"));
    });

 function goToByScroll(section) {
     $("html,body").animate({
        scrollTop: $("#" + section).offset().top}, 'slow');
    }
})
