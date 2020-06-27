
$("document").ready(function(){
  $(".scrollLink").click(function(){
    $("html,body").animate({
      scrollTop: $("#about").offset().top - 200
    }, 500);
  })
})
