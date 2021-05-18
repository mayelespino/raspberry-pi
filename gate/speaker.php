<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<body>

<h1>3336 Fontana Pl</h1>
<a href="index.php">[HOME]</a>

<h2>Speaker</h2>

<br/>
<B>
<?php
date_default_timezone_set('America/Los_Angeles');
$date   = new DateTime(); //this returns the current date time
echo date_format($date,"Y/m/d H:i:s");
echo $result;
?>
<B/>
<br/>
<br/>

<form action="speaker.php" method="post">
    <hr/>
    <input type="submit" name="mute" value="mute"/>
    <input type="submit" name="100%" value="100%"/>
    <input type="submit" name="95%" value="95%"/>
    <input type="submit" name="85%" value="85%"/>
    <input type="submit" name="75%" value="75%"/>
    <input type="submit" name="50%" value="50%"/>
    <br/>
    <hr/>
    <input type="submit" name="nature" value="nature"/>
    <input type="submit" name="scanner" value="scanner"/>
    <input type="submit" name="pink" value="pink"/>
    <input type="submit" name="birds" value="birds"/>
    <input type="submit" name="kcbs" value="kcbs"/>
    <input type="submit" name="bible" value="bible"/>
    <input type="submit" name="biblia" value="biblia"/>
    <br/>
    <hr/>
    <input type="submit" name="siri_news" value="siri_news"/>
    <input type="submit" name="siri_waitwait" value="siri_waitwait"/>
    <input type="submit" name="siri_stop" value="siri_stop"/>
    <br/>
    <hr/>
    <input type="submit" name="google_news" value="google_news"/>
    <input type="submit" name="google_stop" value="google_stop"/>
    <br/>
    <hr/>
    <input type="submit" name="cron" value="cron"/>
    <input type="submit" name="date_time" value="date_time"/>
    <br/>
    <hr/>
</form>
<br/>

<?php 


if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['mute']))
{
  echo post_it("mute");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['nature']))
{
  echo post_it("nature");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['scanner']))
{
  echo post_it("scanner");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['pink']))
{
  echo post_it("pink");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['birds']))
{
  echo post_it("birds");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['kcbs']))
{
  echo post_it("kcbs");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['bible']))
{
  echo post_it("bible");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['biblia']))
{
  echo post_it("biblia");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['100%']))
{
  echo post_it("100");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['95%']))
{
  echo post_it("95");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['85%']))
{
  echo post_it("85");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['75%']))
{
  echo post_it("75");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['50%']))
{
  echo post_it("50");
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

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['google_news']))
{
    google("news");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['google_stop']))
{
    google("stop");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['cron']))
{
  echo post_it("cron");
}

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['date_time']))
{
  echo post_it("date_time");
}

function siri($word){
	$path = sprintf("siri_%s",$word);
	echo post_it($path);
}

function google($word){
	$path = sprintf("google_%s",$word);
	echo post_it($path);
}

function post_it($path) {
	require_once('functions.php');
	$url = sprintf("http://speaker.local:5000/%s/", $path);
	$result = post_url($url); 
	return(str_replace("\n", "<br/>", $result)); 
}

?> 

</body>
</html>
