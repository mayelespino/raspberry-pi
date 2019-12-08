<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<body>

<h1>17440 Holiday Drive</h1>
<a href="index.php">[HOME]</a>
<br/>

<h2>Speaker</h2>

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
    <input type="submit" name="siri_news" value="siri_news"/>
    <input type="submit" name="siri_waitwait" value="siri_waitwait"/>
    <input type="submit" name="siri_stop" value="siri_stop"/>
    <br/>
    <hr/>
    <input type="submit" name="100%" value="100%"/>
    <input type="submit" name="95%" value="95%"/>
    <input type="submit" name="85%" value="85%"/>
    <input type="submit" name="75%" value="75%"/>
    <input type="submit" name="50%" value="50%"/>
    <br/>
    <hr/>
    <input type="submit" name="cron" value="cron"/>
    <input type="submit" name="date" value="date"/>
    <br/>
    <hr/>
</form>
<br/>

<?php 


if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['mute']))
{
    play("mute");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['nature']))
{
    play("nature");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['scanner']))
{
   play("scanner");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['pink']))
{
    play("pink");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['birds']))
{
    play("birds");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['ocean']))
{
    play("ocean");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['bible']))
{
    play("bible");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['biblia']))
{
   play("biblia");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['100%']))
{
    vol("100");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['95%']))
{
    vol("95");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['85%']))
{
    vol("85");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['75%']))
{
    vol("75");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['50%']))
{
    vol("50");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['siri_news']))
{
    siri("news");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['siri_waitwait']))
{
    siri("waitwait");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['siri_stop']))
{
    siri("stop");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['cron']))
{
    cron();
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['date_time']))
{
    date_time();
}

function vol($word){
	// From URL to get webpage contents. 
	$url = sprintf("http://speaker.local:5000/%s/",$word);
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

function play($word){
	// From URL to get webpage contents. 
	$url = sprintf("http://speaker.local:5000/%s/",$word);
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

function siri($word){
	// From URL to get webpage contents. 
	$url = sprintf("http://speaker.local:5000/siri_%s/",$word);
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

function cron(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/cron/";
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

function date_time(){
	// From URL to get webpage contents. 
	$url = "http://speaker.local:5000/date_time/";
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
