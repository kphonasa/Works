//array practice with some and every helper functions
var numbers = [10,20,30];
var sum = 0;

for (var i = 0; i < numbers.length; i++){
	sum += numbers[i];
}

numbers.reduce(function(sum, number){
	return sum + number;
}, 0);

var strings = ["abc","defg","hij"];
var newstring;

strings.reduce(function(newstring,string){
	return string + newstring;
});






//take the colors in this array and create a new array of just the color values
var primaryColors = [
  {color: 'red'},
  {color: 'yellow'},
  {color: 'blue'}
];

primaryColors.reduce(function(previous, primaryColor){
	previous.push(primaryColor.color);
  return previous;
},[]);






//write a function that figures out if the parenthesis are balanced or not
function balancedParens(string){
	return !string.split("").reduce(function(previous, char){
    if (previous < 0) {return previous;}
  	if (char === "(" ) {return ++previous; }
    if (char === ")" ) {return --previous; }
    return previous;
  }, 0);
}

balancedParens("((((");
balancedParens(")(");
balancedParens("(())");





//Use the 'reduce' helper to find the sum of all the distances traveled.  Assign the result to the variable 'totalDistance'
var trips = [{ distance: 34 }, { distance: 12 } , { distance: 1 }];

var totalDistance = trips.reduce(function(sum, trip ){
    return sum + trip.distance;
}, 0);






//Use the 'reduce' helper to create an object that tallies the number of sitting and standing desks.  
//The object returned should have the form '{ sitting: 3, standing: 2 }'.  
var desks = [
  { type: 'sitting' },
  { type: 'standing' },
  { type: 'sitting' },
  { type: 'sitting' },
  { type: 'standing' }
];

var deskTypes = desks.reduce(function(tally, desk) {
    if (desk.type==='sitting'){++tally.sitting;}
    else{++tally.standing;}
    return tally;
    
}, { sitting: 0, standing: 0 });








//Write a function called 'unique' that will remove all the duplicate values from an array.
var numbers = [1, 1, 2, 3, 4, 4];

function unique(array) {
  return array.reduce(function(newArray, arrayEl) {
    var uniqueNum = !newArray.find(function(newArrayEl){
      return newArrayEl == arrayEl;
    });
    if (uniqueNum) {
      newArray.push(arrayEl);
    }
    return newArray;
  }, [])
}
unique(numbers);