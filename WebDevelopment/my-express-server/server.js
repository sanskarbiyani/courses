// jshint esversion:6

const express = require("express");
const app = express();

app.get("/", function(req, res){
  res.send("<h1>Hello, World!</h1>");
});

app.get("/contact", function(req, res){
  res.send("<h3>Contact me at: something@gmail,xom</h3>");
});

app.get("/about", function(req, res){
  res.send("<h3>My name is Sanskar Biyani</h3>");
});

app.listen(3000, function(){
  console.log("Server started at port 3000");
});
