$(document).ready(function() {
  
  
// Challenge 1: Creating a random number.
// Requirements: 
  // how to write a function
  // how to write a return statement
  // finding randomization equation
  
  // Write your code here
  
  function getRandomNum() {
    return Math.floor(Math.random() * (100-0) + 0);
  }
  
  
  
  
// Challenge 2: Assigning a variable.
// Requirements:
  // how to write and define a variable
  
  // Write your code here
  var randomNum = getRandomNum();
  var numOfGuesses = 0;
  var response;
     

  
// Challenge 3: Using if/else and value comparison
// Requirements:
  // how to write a function
  // how to write if/else statements
  // how to write equations that compare values
  function resetGame(){
    
  }
  
  function checkGuess(guess) {
    // Write your code 
    if (guess == randomNum){
      numOfGuesses++;
      response = ("You won using " + numOfGuesses + " guess(es)! A new game has been started!");
      numOfGuesses = 0;
      randomNum = getRandomNum();
      //console.log helps to keep track of the number when unit testing
      //console.log(randomNum);
      
    }
    else{
      numOfGuesses++;
      if (guess > (randomNum + 10) || guess < (randomNum - 10)){
        response = ("Your guess is incorrect. You are cold.");
      }
      else{
        response = ("Your guess is incorrect. You are hot.");
      }
    }
  }

  //console.log helps to keep track of the number when unit testing
  //console.log(randomNum);
  
  
  
  

// This code uses jQuery, a javascript library, to run.
// You don't need to know how this works, 
// just that it makes the submit button function.
  $('.guessingForm').submit(function(event) {
    event.preventDefault();
    var guess = $('#js-user-guess').val();
    $('#js-user-guess').val('');
    checkGuess(guess);
    
    $('.guessCount').text("Number of Guesses: " + numOfGuesses);
    $('.responseText').text(response);
  });  
// document.ready end    
  $('.resetForm').submit(function(event){
    numOfGuesses = 0;
    randomNum = getRandomNum();
    alert("A new game has been started.");
    
  });

});




// Possible additions
// 1. Tracking number of guesses
// 2. Hot or cold (more if statements)
// 3. New game/reset button
