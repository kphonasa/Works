<?php
//kicks users out if they are not logged in
	session_start();
	if (!isset($_SESSION['email']))
	{
		header('Location: login.php');
		exit;
	}
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
	
		<title>Manufacturers</title>
	</head>
	
	<body>
	<div class="row">
			<div class="col-xs-12">
				<div class="navbar navbar-inverse">
				<!--Menu-->
					<div class="container fluid">
					<ul class="nav nav-pills">
						<li><a href="inputHW5.php">Cars</a></li>
						<li class="active"><a href="">Manufacturers</a></li>
						<li><a href="logout.php">Logout</a></li>
					</ul>
					</div>
				</div>
			</div>
		</div>
	<!--code to manage form data-->
	<?php
	include_once('config.php');
	include_once('dbutils.php');
	//check if form data needs to be processed
	if (isset($_POST['submit']))
	{
		
		//form was submitted and data needs to be processed
		//get data from form
		$NAME=$_POST['NAME'];
		$COUNTRY=$_POST['COUNTRY'];
	
		
		//check if form is complete
		$isComplete=true;
		$errorMessage="";
		if (!$NAME)
		{
			$errorMessage.="Please enter the name of the manufacturer.\n";
			$isComplete=false;
		}
		else 
		{
			$db=connectDB($DBHost,$DBUser,$DBPasswd,$DBName);
			$query ="SELECT NAME FROM MANUFACTURERHW5 WHERE NAME='$NAME';";

			$result=queryDB($query,$db);
			
			if (nTuples($result)>0)
			{
				$isComplete=false;
				$errorMessage.="This manufacturer is already in the database.\n";
			}
		}
		if (!$COUNTRY)
		{
			$errorMessage.="Please enter the manufacturer's country of origin.\n";
			$isComplete=false;
		}

		
		if (!$isComplete){punt($errorMessage);}
		
		$query ="INSERT INTO MANUFACTURERHW5(NAME, COUNTRY) VALUES('$NAME', '$COUNTRY');";
		
		
		$db=connectDB($DBHost,$DBUser,$DBPasswd,$DBName);
		
		$result=queryDB($insert,$db);
		
		echo("The manufacturer has successfully been submitted.");
	
	}
	?>
	<div class='row'>
		<div class="col-xs-12">
			<h1>Manufacturers</h1>
		</div>
	</div>
	
	<!--New Manufacturer Form-->
	<div class='row'>
		<div class='col-xs-12'>
		
		<form action='inputmanufacturerHW5.php' method='post'>
		<!--Name-->
		<div class='form-group'>
			<label for='NAME'>Manufacturer Name:</label>
			<input type='text' class='form-control' name='NAME'/>
		</div>
		
		<!--Country-->
		<div class='form-group'>
			<label for='COUNTRY'>Country of Origin:</label>
			<input type='text' class='form-control' name='COUNTRY'/>
		</div>
		
		<button type='submit' class='btn btn-default' name='submit'>Save</button>
		</form>
		
		</div>
	</div>
	
	<!--table-->
	<div class='row'>
		<div class='col-xs-12'>
	
	<!--set up html table to show contents-->
	<table class='table table-hover'>
		<!--table headers-->
		<thead>
			<th>Name</th>
			<th>Country</th>
		</thead>

		<!--Lists all cars in database-->
		<!--include config and util files-->
		<?php
			
		//connect to the database
		$db = connectDB($DBHost,$DBUser,$DBPasswd,$DBName);

		

		//Set up the query to get information on the cars from the database
		$query = "SELECT * FROM MANUFACTURERHW5;";
		
		//run the query
		$result= queryDB($query, $db);
				
		while($row = nextTuple($result))
		{
			echo'<tr>';
			echo '<td>' . $row['NAME'] . '</td>';
			echo '<td>' . $row['COUNTRY'] . '</td>';
			echo'</tr>';
		}
		
		?>
	</table>
		</div>
	</div>		
	</body>
</html>