<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<body>

<h1>17440 Holiday Drive</h1>
<a href="index.php">[HOME]</a>
<br/>

<h2>sounds</h2>

<form action="sounds.php" method="post">
    <hr/>
    <input type="submit" name="mute" value="mute"/>
    <input type="submit" name="nature" value="nature"/>
    <input type="submit" name="scanner" value="scanner"/>
    <input type="submit" name="pink" value="pink"/>
    <input type="submit" name="birds" value="birds"/>
    <input type="submit" name="ocean" value="ocean"/>
    <input type="submit" name="bible" value="bible"/>
    <input type="submit" name="biblia" value="biblia"/>
    <br/>
    <hr/>
    <input type="submit" name="100%" value="100%"/>
    <input type="submit" name="95%" value="95%"/>
    <input type="submit" name="85%" value="85%"/>
    <input type="submit" name="75%" value="75%"/>
    <input type="submit" name="50%" value="50%"/>
    <br/>
    <hr/>
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

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['birds']))
{
    play_birds();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['ocean']))
{
    play_ocean();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['bible']))
{
    play_bible();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['biblia']))
{
    play_biblia();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['100%']))
{
    vol_100();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['95%']))
{
    vol_85();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['85%']))
{
    vol_85();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['75%']))
{
    vol_75();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['50%']))
{
    vol_50();
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

function vol_100(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/100/"; 
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

function vol_95(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/95/"; 
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

function vol_85(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/85/"; 
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

function vol_75(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/75/"; 
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

function vol_50(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/50/"; 
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

function play_birds(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/birds/"; 
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

function play_ocean(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/ocean/"; 
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

function play_bible(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/bible/"; 
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

function play_biblia(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/biblia/"; 
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
