var player1Dice = Math.floor(Math.random()*6) + 1;
var player2Dice = Math.floor(Math.random()*6) + 1;
document.querySelector(".img1").setAttribute("src", ("images/dice"+player1Dice+".png"));
document.querySelector(".img2").setAttribute("src", ("images/dice"+player2Dice+".png"));
if(player1Dice > player2Dice){
    document.querySelector("h1").innerHTML = "Player 1 wins";
}else if(player1Dice === player2Dice){
    document.querySelector("h1").innerHTML = "It's a tie";
}else{
    document.querySelector("h1").innerHTML = "Player 2 wins";
}
