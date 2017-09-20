//array helper filter practice
//make a new array of only products with the type of fruit
var products = [
  {name: 'cucumber', type: 'vegetable'},
  {name: 'apple', type: 'fruit'},
  {name: 'celery', type: 'vegetable'},
  {name: 'orange', type: 'fruit'}
];

var filteredProducts = products.filter(function(product){
	return product.type === 'fruit';
});

filteredProducts;



//of the product array, create a new array
//type=vegetable, quantity>0, price<10
var products = [
  {name: 'cucumber', type: 'vegetable', quantity:0, price:1},
  {name: 'apple', type: 'fruit', quantity:10, price:15},
  {name: 'celery', type: 'vegetable', quantity:30, price:9},
  {name: 'orange', type: 'fruit', quantity:3, price:1}
];

var filteredProducts = products.filter(function(product){
	return product.type === 'vegetable'
  && product.quantity>0
  && product.price<10;
});

filteredProducts;



//create a new array of comments that match the postid

var post = {id:4, title:'New Post'};
var comments = [
  {postID:4, content:'awesome post'},
  {postID:3, content:'it was ok'},
  {postID:4, content:'neat'}
];

function commentsForPost(post, comments){
	return comments.filter(function(comment){
  	return comment.postID === post.id
  });
}

commentsForPost(post, comments);




//Filter the array of numbers using the filter helper, creating a new array that only contains numbers greater than 50.  
//Assign this new array to a variable called 'filteredNumbers'. 
var numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95];

var filteredNumbers = numbers.filter(function(number){
    return number > 50;
});

filteredNumbers;





//Filter the array of users, only returning users who have admin level access.  
//Assign the result to the variable 'filteredUsers'.
var users = [
 { id: 1, admin: true },  
 { id: 2, admin: false },
 { id: 3, admin: false },
 { id: 4, admin: false },
 { id: 5, admin: true },
];

var filteredUsers = users.filter(function(user){
    return user.admin === true;
});

filteredUsers;




// Create a function called 'reject'.  
//Reject should work in the opposite way of 'filter' - if a function returns 'true', the item should *not* be included in the new array.
var numbers = [10, 20, 30];

function reject(array, iteratorFunction) {
  return array.filter(function(item) {
      return !iteratorFunction(item);
  });
}

var lessThanFifteen = reject(numbers, function(number){
  return number > 15;
}); 
  
lessThanFifteen;





