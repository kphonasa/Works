//array practice: Sum of numbers in array
//array of numbers
var numbers = [1,2,3,4,5];

//create a variable to hold the sum
var sum = 0;

function adder(number){
  sum += number;
}

//loop over the array, incrementing the usum variable
numbers.forEach(adder);

sum;




//Using the forEach helper, calculate the area of 
//each image and store it in a new array called 'areas'.  
//The area of an image can be calculated as 'image.height * image.width'.
var images = [
  { height: 10, width: 30 },
  { height: 20, width: 90 },
  { height: 54, width: 32 }
];
var areas = [];

images.forEach(function(image){
    var area = image.height*image.width;
    areas.push(area);
});


