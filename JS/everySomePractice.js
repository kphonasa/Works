//array practice with some and every helper functions
//find out if we have computers with over 16 ram that can run a program
var computers = [
  {name: 'Apple', ram: 24},
  {name: 'Compaq', ram: 4},
  {name: 'Acer', ram: 32}
];

var allComputersCanRunProgram = true;
var onlySomeComputersCanRunProgram = false;

for (var i = 0; i < computers.length; i++){
	var computer = computers[i];
  
  if (computer.ram< 16) {
  	allComputersCanRunProgram = false;
  }
  else{
  	onlySomeComputersCanRunProgram = true;
  }
}

"---break---"
allComputersCanRunProgram;
onlySomeComputersCanRunProgram;

"---break---"

computers.every(function(computer){
	return computer.ram > 16;
});

computers.some(function(computer){
	return computer.ram > 16;
});








//find if all and/or some names are about 4 characters long
var names = [
	"Alexandria",
  "Matthew",
  "Joe"
];

names.every(function(name){
	return name.length > 4;
});

names.some(function(name){
	return name.length > 4;
});






//validate that all fields are not empty before submitting forms
function Field(value){
	this.value = value;
}

Field.prototype.validate = function(){
	return this.value.length > 0;
}

var username = new Field("2cool");
var password = new Field("my_password");

username.validate() && password.validate();
var fields = [username, password];
var formIsValid = fields.every(function(field){
	return field.validate();
});

if (formIsValid){
	//allow user to submit form
}
else {
	//throw error
}






//Given an array of users, return 'true' if every user has submitted a request form.  
var users = [
  { id: 21, hasSubmitted: true },
  { id: 62, hasSubmitted: false },
  { id: 4, hasSubmitted: true }
];

var hasSubmitted = users.every(function(user){
    return user.hasSubmitted;
});








//Given an array of network objects representing network requests, 
//assign the boolean 'true' to the variable 'inProgress' if any network request has a 'status' of 'pending'.
var requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' }
];

var inProgress = requests.some(function(request){
    return request.status = 'pending';
});







