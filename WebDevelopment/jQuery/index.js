$("h1").addClass("big-title");

var textEntered = "";
$(document).keydown(function(event){
  if(event.key == " "){
    $("h1").text(textEntered);
    textEntered = "";
  }else{
    console.log("Hii");
    textEntered = textEntered + event.key;
  }
  console.log(textEntered);
});

$(document).on("mousemove", function(event){
  $(".mouse").css("top", event.clientY);
  $(".mouse").css("left", event.clientX);
  console.log(event.offsetX + "     " + event.offsetY);
  console.log(event);
});
