
var buttonColors = ["red", "blue", "green", "yellow"];
var gamePatterns = [];
var userClickedPattern = [];
var toggle = false;
var level = 0;
var sequencePosition = 0;
var gameOver = false;

function nextSequence(){
  level++;
  $("#level-title").text("level " + level);
  var randomNumber = Math.floor(Math.random()*4);
  var randomChosenColor = buttonColors[randomNumber];
  gamePatterns.push(randomChosenColor);
  // console.log(gamePatterns);
  $("#" + randomChosenColor).fadeOut(100).fadeIn(100);
  playSound(randomChosenColor);
}

$(".btn").on("click", function(event){
  var userChosenColor = event.target.id;
  userClickedPattern.push(userChosenColor);
  playSound(userChosenColor);
  // console.log(userClickedPattern);
  animatePress(userChosenColor);
  checkSequence(userChosenColor);

});

function playSound(color){
  var audio = new Audio("sounds/" + color + ".mp3");
  audio.play();
}

function animatePress(pressedColor){
  $("#"+pressedColor).addClass("pressed");
  setTimeout(function(){
    $("#"+pressedColor).removeClass("pressed");
  }, 100);
  // console.log("Working!");
}

$(document).on("keydown", function(){
  if(toggle == false){
    nextSequence();
    toggle = true;
    $("#level-title").text("level " + level);
  }else if(gameOver == true){
    console.log("Restaring..");
    startOver();
  }
});

function checkSequence(color){
  // console.log(color + " == " + gamePatterns[sequencePosition]);
  // console.log("position before changing "+sequencePosition);
    if(color == gamePatterns[sequencePosition]){

      if(userClickedPattern.length == gamePatterns.length){
        sequencePosition = 0;
        // console.log("position after changing "+sequencePosition);
        userClickedPattern = [];
        setTimeout(function(){
          nextSequence();
        }, 500);
      }else{
        sequencePosition++;
      }

    }else{
      // console.log("game reset");
      playSound("wrong")
      $("body").addClass("game-over");
      $("#level-title").text("Game Over, Press Any Key to Restart");
      setTimeout(function(){
        $("body").removeClass("game-over");
      }, 200);
      gameOver = true;
    }
}

function startOver(){
  gamePatterns = [];
  userClickedPattern = [];
  toggle = false;
  level = 0;
  sequencePosition = 0;
  $("#level-title").text("Press A Key to Start");
  gameOver = false;
}
