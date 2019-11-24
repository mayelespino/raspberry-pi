<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<body>

<h1>17440 Holiday Drive</h1>
<h2>sounds</h2>

<form action="sounds.php" method="post">
    <input type="submit" name="mute" value="mute"/>
    <input type="submit" name="nature" value="nature"/>
    <input type="submit" name="scanner" value="scanner"/>
    <input type="submit" name="pink" value="pink"/>
</form>
<br/>

<?php 


if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['mute']))
{
    play_mute();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['nature']))
{
    play_nature();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['scanner']))
{
    play_scanner();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['pink']))
{
    play_pink();
}

function play_mute(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/mute/"; 
	// Initialize a CURL session. 
	$ch = curl_init(); 
	// Return Page contents. 
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
	//grab URL and pass it to the variable. 
	curl_setopt($ch, CURLOPT_URL, $url); 
	curl_setopt($ch, CURLOPT_POST, 1); 
	$result = curl_exec($ch); 
	echo $result; 
}

function play_nature(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/nature/"; 
	// Initialize a CURL session. 
	$ch = curl_init(); 
	// Return Page contents. 
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
	//grab URL and pass it to the variable. 
	curl_setopt($ch, CURLOPT_URL, $url); 
	curl_setopt($ch, CURLOPT_POST, 1); 
	$result = curl_exec($ch); 
	echo $result; 
}

function play_scanner(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/scanner/"; 
	// Initialize a CURL session. 
	$ch = curl_init(); 
	// Return Page contents. 
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
	//grab URL and pass it to the variable. 
	curl_setopt($ch, CURLOPT_URL, $url); 
	curl_setopt($ch, CURLOPT_POST, 1); 
	$result = curl_exec($ch); 
	echo $result; 
}

function play_pink(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/pink/"; 
	// Initialize a CURL session. 
	$ch = curl_init(); 
	// Return Page contents. 
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
	//grab URL and pass it to the variable. 
	curl_setopt($ch, CURLOPT_URL, $url); 
	curl_setopt($ch, CURLOPT_POST, 1); 
	$result = curl_exec($ch); 
	echo $result; 
}

?> 

</body>
</html>
