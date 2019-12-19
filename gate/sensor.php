<html>
<head>
</head>
<body>

<h1>17440 Holiday Drive</h1>

<a href="index.php">[HOME]</a>

<h2>Sensors</h2>
<br/>

<table border=1>
<tr>
<td>
<h3>Last check</h3>
<b>
<?php
$homepage = file_get_contents('http://sensor.local:5000/time-stamp/');
echo $homepage;
?>

</td>
<td>

<h3>Brightness</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/brightness/');
echo $homepage;
?>

</td>
<td>

<h3>Humidity</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/humidity/');
echo $homepage;
?>

</td>
<td>

<h3>Onboard Temp</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/onboard-temp/');
echo $homepage;
?>

</td>
</tr>
<tr>
<td>

<h3>Temperature</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/temperature/');
echo $homepage;
?>

</td>
<td>

<h3>Barometer</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/barometer/');
echo $homepage;
?>

</td>
<td>

<h3>Motion</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/human/');
echo $homepage;
?>

</td>
<td>
<h3>Bluetooth</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/bt-stamp/');
echo $homepage;
?>
</td>
</tr>

</table>

<h2>History</h2>
<?php
$homepage = file_get_contents('http://sensor.local:5000/temp-history/');
echo str_replace("\n", "<br/>", $homepage);
?>

</body>
</html>
