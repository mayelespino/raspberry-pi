<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<body style="background-color:powderblue;">

<h1>3336 Fontana Pl</h1>
<a href="index.php">[HOME]</a>
<br/>
<?php
date_default_timezone_set('America/Los_Angeles');
$date   = new DateTime(); //this returns the current date time
echo date_format($date,"Y/m/d H:i:s");
echo $result;
?>
<br/>
<form action="speaker.php" method="post">
    <hr/>
    <h2>Volume Control</h2>
    <input type="submit" name="mute" value="mute"/>
    <input type="submit" name="100%" value="100%"/>
    <input type="submit" name="95%" value="95%"/>
    <input type="submit" name="85%" value="85%"/>
    <input type="submit" name="75%" value="75%"/>
    <input type="submit" name="50%" value="50%"/>
    <br/>
    <hr/>
    <h2>Information</h2>
    <input type="submit" name="cron" value="cron"/>
    <input type="submit" name="date_time" value="date_time"/>
    <br/>
    <hr/>

</form>
<h2>Sounds Presets</h2>

<form action="" method="post">
    <select name="preset">
        <?php
        $sounds = array("nature","scanner","pink", "biblia", "nature", "kcbs", "birds", "bible");
        
        foreach($sounds as $item){
            echo "<option value='$item'>$item</option>";
        }
        ?>
    </select>

    <input type="submit" name="submit" vlaue="Choose options">
</form>

<hr/>
<h2>Output</h2>

<?php
    if(isset($_POST['submit'])){
    if(!empty($_POST['preset'])) {
       $selected = $_POST['preset'];
       post_it("mute");
       echo post_it($selected);
    } else {
        echo 'Please select the value.';
    }
    }
?>

<?php 

if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['mute']))
{
  echo post_it("mute");
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
