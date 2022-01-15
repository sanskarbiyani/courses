const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/fruitsDB", { useNewUrlParser: true, useUnifiedTopology: true });

const fruitSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, "Name field is required!"]
  },
  rating: {
    type: Number,
    min: [1, "Not possible"],
    max: [10, "More than the highest possible rating"]
  },
  review: String
});

const Fruit = mongoose.model("Fruit", fruitSchema);

// const pineapple = new Fruit({
//   name: "Pineapple",
//   rating: 10,
//   review: "Yummy!"
// });
//
// pineapple.save()
//
const peach = new Fruit({
  name: "Peach",
  rating: 4,
  review: "Great!"
});

peach.save();

const personSchema = mongoose.Schema({
  name: String,
  age: Number,
  favouriteFruit: fruitSchema
});

const Person = mongoose.model("Person", personSchema);

// const person = new Person({
//   name: "Jack",
//   age: 19,
//   favouriteFruit: pineapple
// });

// person.save()

const Kiwi = new Fruit({
  name: "Kiwi",
  rating: 5,
  review: "So-so"
});

// const Banana = new Fruit({
//   name: "Banana",
//   rating: 7,
//   review: "Healty"
// });
//
// const Orange = new Fruit({
//   name: "Orange",
//   rating: 9,
//   review: "Good Fruits"
// });

// Fruit.insertMany([Kiwi, Banana, Orange], (err)=>{
//   if(err){
//     console.log(err);
//   } else{
//     console.log("Operation successfull!");
//   }
// });

// Fruit.find({rating: {$lt: 6}}, (err, fruits)=>{
//   if (err){
//     console.log(err);
//   } else {
//     mongoose.connection.close();
//   fruits.forEach((fruit)=>{
//     console.log(fruit.name);
//   });
//     // console.log(fruits);
//   }
// });
//
Person.updateOne({name: "John"}, {favouriteFruit: peach}, (err)=>{
  if(err){
    console.log(err);
  } else {
    console.log("Updation successfull");
  }
});


// Fruit.deleteMany({name:"Peach"}, (err)=>{
//   if(err){
//     console.log(err);
//   } else {
//     console.log("Deletion successfull");
//     mongoose.connection.close();
//   }
// });

// Person.find((err)=>{
//   if(err){
//       console.log(err);
//   } else {
//     console.log("Updation successfull");
//   }
// });
