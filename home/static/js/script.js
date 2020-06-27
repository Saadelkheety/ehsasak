
$("document").ready(function(){
  $(".scrollLink").click(function(){
    $("html,body").animate({
      scrollTop: $("#info").offset().top
    }, 500);
  })
})
