//jshint esversion: 6

const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const mongoose = require("mongoose");

const app = express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

mongoose.connect("mongodb://localhost:27017/wikiDB", {useNewUrlParser: true, useUnifiedTopology: true});

const articleSchema = mongoose.Schema({
  title: String,
  content: String
});

const Article = mongoose.model("Article", articleSchema);

// Routes for GENERAL articles
app.route("/articles")
.get((req, res)=>{
  console.log("Inside get");
  Article.find((err, foundArticles)=>{
    if(!err){
    res.send(foundArticles);
    }
  });
})
.post((req, res)=>{
  const article = new Article({
    title: req.body.title,
    content: req.body.content
  });
  article.save((err)=>{
    if(!err){
      res.send("Successfully Added!");
    } else {
      res.send(err);
    }
  });
})
.delete((req, res)=>{
  Article.deleteMany((err)=>{
    if (!err){
      res.send("Successfully Deleted all articles!");
    } else {
      res.send(err);
    }
  });
});

// Routes for SPECIFIC article
app.route("/articles/:articleTitle")
.get((req, res)=>{
  Article.findOne({title: req.params.articleTitle}, (err, foundArticle)=>{
    if (foundArticle){
    res.send(foundArticle);
  } else {
    res.send("No articles found!");
  }
  });
})
.put((req, res)=>{
  // update method is used because we want to rewrite the whole document
  // "overwite= true" tells mongoose not to wrop the content inside the $set which causes the whole document to be overwritten
  Article.update(
    {title: req.params.articleTitle},
    {title: req.body.title, content: req.body.content},
    {overwrite: true},
    function (err){
      if (!err){
        res.send("Operation Successfull!");
      } else {
        res.send(err);
      }
    }
  );
})
.patch((req, res)=>{
  // same as the update method but no overwite option
  Article.updateOne(
    {title: req.params.articleTitle},
    {$set: req.body},
    function (err){
      if (!err){
        res.send("Operation Successfull!");
      } else {
        res.send(err);
      }
    }
  );
})
.delete((req, res)=>{
  Article.deleteOne({title: req.params.articleTitle}, (err)=>{
    if (!err) {
      res.send("Operation successsfull!");
    } else {
      res.send(err);
    }
  })
});

app.listen(3000, ()=>{
  console.log("Server running on port 3000");
})
