<!DOCTYPE html>
<html>
<body>


<h1>
<?php
date_default_timezone_set("America/Los_Angeles");
echo  date("h:i:sa");
?>
<h1/>


<h2>Current Alarms<h2/>
<textarea rows="4" cols="50">
<?php
$file = file_get_contents('./alarms.txt', true);
echo "  $file;"
?>
</textarea>


<?php
 if(isset($_POST['select']))
{
    fnPHP();
}
else
{
    fnPHP2();
}
?>


<br/>
<form action="index.php" method="post">
<input type="submit" class="button" name="fnPHP" value="fnPHP" />
</form>


<?php
function fnPHP()
{
   //do something
}
function fnPHP2()
{
   //do something
}
?>
</body>
</html>