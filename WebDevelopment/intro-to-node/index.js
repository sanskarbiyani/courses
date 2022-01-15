//jshint esversion:6

var sh = require("superheroes");
var heroName = sh.random();

var sv = require("supervillains");
var villainName = sv.random();

console.log(heroName + " fights " + villainName);
