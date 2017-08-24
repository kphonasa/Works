<?php 
//This php file prompts useres on whether they want to delete
//a car. It obtains the id for the car to delete from an id
//variable passed using the GET method in the URL

	include_once('config.php');
	include_once('dbutils.php');
	
//If the user just made a decision on a deletion by using the form below, we process that below
	if(isset($_POST['submit']))
	{
		//Process the deletion (if selected) if the form below was submitted
		//Get data from form
		$id=$_POST['id'];
		$delete=$_POST['delete'];
		
		if ($delete=='yes')
		{
			//if the user said yes to delete, we need to delete the car with the id =$id
			//Connect to database
			$db=connectDB($DBHost,$DBUser,$DBPasswd,$DBName);
			
			//First delete brand records that point to this car
			$query="DELETE FROM BRAND WHERE ID=$id;";
			
			//Run the delete statement to remove brand records that point to this car
			queryDB($query, $db);
			
			//Next we need to delete the actual car
			$query="DELETE FROM CAR WHERE ID=$id;";
			
			//Run the delete statement to remove brand records that point to this car
			queryDB($query, $db);
		}
		//Send user back to input.php and exit
		header('Location: input.php');
		exit;
	}
	
//Check if GET variable was passed with the id for the car
	
	if(isset($_GET['id']))
	{
		//if the id was not passed through the urldecode
		//send them out to input.php and stop executing code in this page
		header('Location: input.php');
		exit;
	}
	
	//Now check to make sure the id passed through the GET variable 
	//matches the id of a car in the database
	
	//Connect to database
	$db = connectDB($DBHost, $DBUser, $DBPasswd, $DBName);
	
	//Set up a query
	$id = $_GET['id'];
	$query = "SELECT * FROM CARS WHERE ID=$id;";
	
	//Run the query
	$result = queryDB($query, $db);
	
	//If the id is not in the car table, then we send the user back to input.php
	if(nTuples($result)==0)
	{
		//send them to input.php and stop executing the code
		header('Location: input.php');
		exit;
	}
	
	//Now we know we got a valid car id through the GET variable
	//Get some data from the car table to ask a better question when confirming deletion
	$row = nextTuple($result);
	$name = $row['name'];
?>

<html>
	<head>
	
		<neta name="viewport" content="width=device-widthe, initial-scale-1.0">
    
		<!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

		<!-- Optional theme -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

		<!-- Latest compiled and minified JavaScript -->
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
	
		<title>Delete <?php echo $name; ?> car?</title>
	</head>
	
	<body>
	
<!--Visible title-->
<div class = "row">
	<div class = "col-xs-12">
	<form action="delete.php" method="post">
		<div class="radio">
			<label>
				<input type = "radio" name="delete" value ="yes">
				Yes
			</label>
		</div>
		<div class="radio">
			<label>
				<input type = "radio" name="delete" value ="no">
				No
			</label>
		</div>
		
		<input type="hidden" name="id" value="<?ohp echo $id; ?>"/>
		
		<button type='submit' class='btn btn-default' name='submit'>Submit</button>
	</form>
	</div>
</div>

	</body>
</html>