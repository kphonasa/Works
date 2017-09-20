//array helper map practice
//make a new array of only car prices
var cars =[ 
  {model: 'Buick', price: 'CHEAP'},
  {model: 'Camaro', price: 'expensive'}
  ];

var prices = cars.map(function (car) {
  return car.price;
});

prices;




//Using map, create a new array that contains the 'height' property of each object. 
// Assign this new array to the variable 'heights'.
var images = [
  { height: '34px', width: '39px' },
  { height: '54px', width: '19px' },
  { height: '83px', width: '75px' },
];

var heights = images.map(function(image){
    return image.height;
});





//Using map, create a new array that contains the distance / time value from each trip.  
//In other words, the new array should contain the (distance / time) value.  Assign the result to the variable 'speeds'.
var trips = [
  { distance: 34, time: 10 },
  { distance: 90, time: 50 },
  { distance: 59, time: 25 }
];

var speeds = trips.map(function(trip){
    return (trip.distance/trip.time);
});





//Implement a 'pluck' function.  
//Pluck should accept an array and a string representing a property name and return an  array containing that property from each object. 
function pluck(array, property) {
    var newArray = array.map(function(prop){
       return prop[property];
    });
    return newArray;
    
}

var paints = [ { color: 'red' }, { color: 'blue' }, { color: 'yellow' }];
pluck(paints, 'color'); // returns ['red', 'yellow', 'blue'];
