//array helper find practice
//Use the find helper function to find alex
var users = [
  {name: 'Jill'},
  {name: 'Alex'},
  {name: 'Bill'}
];

users.find(function(user) {
	return user.name === 'Alex';
});




//find the comment that goes with post id 1
var posts= [
  {id: 1, title: 'New Post'},
  {id: 2, title: 'Old Post'}
];

var comment =
    {postId: 1, content: 'Great Post'};

function postForComment(posts, comment){
  return posts.find(function(post){
    return post.id === comment.postId;
  });
}

postForComment(posts, comment);





//Find the user in the users's array who is an admin.  Assign this user to the variable 'admin'.
var users = [
  { id: 1, admin: false },
  { id: 2, admin: false },
  { id: 3, admin: true }
];

var admin = users.find(function(user){
    return user.admin === true;
});

admin;





//Find the account with a balance of 12 and assign it to the variable 'account'.
var accounts = [
  { balance: -10 },
  { balance: 12 },
  { balance: 0 }
];

var account = accounts.find(function(acc){
    return acc.balance === 12;
});

account;







/*The most common find operation is to an object that has a given property.  
Rather than writing out a full function every time, it would be great if we has a shorthand syntax to find an object like this:
findWhere(ladders, { height: '20 feet' });
The object { ladders: '20 feet' } should be used as the search criteria - 
we would want to find a ladder whose 'height' property was '20 feet';
 Write a 'findWhere' function that achieves this shorthand approach.  'findWhere' should return the found object.*/

var ladders = [
  { id: 1, height: 20 },
  { id: 3, height: 25 }
];

function findWhere(array, criteria){
  var id = Object.keys(criteria);
  
  return array.find(function(arr){
    return arr[id] === criteria[id];
  });
}
findWhere(ladders, { height: 25 });