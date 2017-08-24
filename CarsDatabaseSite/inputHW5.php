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
	
		<title>Cars</title>
	</head>
	
	<body>
	<div class="row">
			<div class="col-xs-12">
				<div class="navbar navbar-inverse">
				<!--Menu-->
					<div class="container fluid">
					<ul class="nav nav-pills">
						<li class="active"><a href="">Cars</a></li>
						<li><a href="inputmanufacturerHW5.php">Manufacturers</a></li>
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
		$BID=$_POST['BID'];
		$MODEL=$_POST['MODEL'];
		$MODELYEAR=$_POST['MODELYEAR'];
		$CARTRIM=$_POST['CARTRIM'];
		$URL=$_POST['URL'];
		
		//check if form is complete
		$isComplete=true;
		$errorMessage="";
		if (!$BID)
		{
			$errorMessage.="Please select the manufacturer.\n";
			$isComplete=false;
		}
		if (!$MODEL)
		{
			$errorMessage.="Please enter car model.\n";
			$isComplete=false;
		}
		else 
		{
			$db=connectDB($DBHost,$DBUser,$DBPasswd,$DBName);
			$query ="SELECT MODEL FROM CARSHW5 WHERE MODEL='$MODEL';";

			$result=queryDB($query,$db);
			
			if (nTuples($result) > 0)
			{
				$isComplete=false;
				$errorMessage.= "This model is already in the database.\n";
			}
		}
		if (!$MODELYEAR)
		{
			$errorMessage.="Please enter car model year.\n";
			$isComplete=false;
		}
		if (!$CARTRIM)
		{
			$errorMessage.="Please enter car color.\n";
			$isComplete=false;
		}
		if (!$URL)
		{
			$errorMessage.="Please post a link to a video of the car.\n";
			$isComplete=false;
		}
		
		if (!$isComplete){punt($errorMessage);}
		
		$query ="INSERT INTO CARSHW5(BID, MODEL, MODELYEAR, CARTRIM, URL) VALUES('$BID', '$MODEL', '$MODELYEAR', '$CARTRIM','$URL');";
		
		$db=connectDB($DBHost,$DBUser,$DBPasswd,$DBName);
		
		$result=queryDB($insert,$db);
		
		echo("The car has successfully been submitted.");

	}
	?>
	
	<div class='row'>
		<div class="col-xs-12">
			<h1>Cars</h1>
		</div>
	</div>
	
	<!--New Car Form-->
	<div class='row'>
		<div class='col-xs-12'>
		
		<form action='inputHW5.php' method='post'>
		<!--Brand-->
		<div class='form-group'>
			<label for='BID'>Car Brand:</label>
			<?php 
			mysql_connect($DBHost,$DBUser,$DBPasswd);
			mysql_select_db($DBName);
			$query ="SELECT NAME, BID FROM MANUFACTURERHW5;";

			$result=mysql_query($query);
			echo "<select class='form-control' name='BID'>";
			
			while($row=mysql_fetch_array($result))
			{
				echo "<option value='". $row['BID'] . "'>" . $row['NAME'] . "</option>\n";
			}
			echo "</select>";
			?>
		</div>
		
		<!--Model-->
		<div class='form-group'>
			<label for='MODEL'>Model:</label>
			<input type='text' class='form-control' name='MODEL'/>
		</div>
		
		<!--Year-->
		<div class='form-group'>
			<label for='MODELYEAR'>Year:</label>
			<input type='number' class='form-control' name='MODELYEAR'/>
		</div>
		
		<!--Color-->
		<div class='form-group'>
			<label for='CARTRIM'>Color:</label>
			<input type='text' class='form-control' name='CARTRIM'/>
		</div>
		
		<div class='form-group'>
			<label for='URL'>URL:</label>
			<input type='text' class='form-control' name='URL'/>
		</div>
		
		<button type='submit' class='btn btn-default' name='submit'>Save</button>
		</form>
		
		</div>
	</div>
	
	<!--cars table-->
	<div class='row'>
		<div class='col-sm-8'>
	
	<!--set up html table to show contents-->
	<table class='table table-hover'>
		<!--table headers-->
		<thead>
			<th>Manufacturer ID</th>
			<th>Model</th>
			<th>Year</th>
			<th>Color</th>
			<th>URL Link</th>
		</thead>
	
		<!--Lists all cars in database-->
		<!--include config and util files-->
		<?php

		//connect to the database
		$db = connectDB($DBHost,$DBUser,$DBPasswd,$DBName);

		//Set up the query to get information on the cars from the database
		$query = "SELECT * FROM CARSHW5;";
		
		//run the query
		$result= queryDB($query, $db);
				
		while($row = nextTuple($result))
		{
			echo'<tr>';
			echo '<td>' . $row['BID'] . '</td>';
			echo '<td>' . $row['MODEL'] . '</td>';
			echo '<td>' . $row['MODELYEAR'] . '</td>';
			echo '<td>' . $row['CARTRIM'] . '</td>';
			echo '<td>' . $row['URL'] . '</td>';
			echo'</tr>';
		}
		?>
	</table>
		</div>
	</div>
	</body>
</html>