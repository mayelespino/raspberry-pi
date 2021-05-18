<html>
</head>
<body>

<h1>3336 Fontana </h1>
<h2>Pi status</h2>

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

<table border=1>
<tr>
<td>

<a href="sensor.php">sensor PI</a>

</td><td>

<?php
require_once('functions.php');
$url = "http://sensor.local/";
$result = get_url($url);
if ($result == '' ) {
  echo "<b><font color=\"red\">OUT</font></b>";
} else {
  echo "<b><font color=\"green\">OK</font></b>";
}
?>

</td><td>

</td><td>

<a href="speaker.php">speaker PI</a>

</td><td>

<?php
require_once('functions.php');
$url = "http://speaker.local/";
$result = get_url($url);
if ($result == '' ) {
  echo "<b><font color=\"red\">OUT</font></b>";
} else {
  echo "<b><font color=\"green\">OK</font></b>";
}
?>

</td>
</td><td>

At home

</td><td>

<?php
require_once('functions.php');
$url = "http://sensor.local:5000/bt-status/";
$result = get_url($url);
if ($result != "IN" ) {
  echo "<b><font color=\"red\">OUT</font></b>";
} else {
  echo "<b><font color=\"green\">IN</font></b>";
}
?>

</td>
<tr/>
</table>

<h2>Weather</h2>
<iframe src="http://wttr.in/94509" height="130" width="240"></iframe>
<br>
<a href="weather.php">Full weather 94509</a><br/>
<br/>

<h2>Spare the air</h2>
<iframe src="http://baaqmdmapsprod.azurewebsites.net/map-open-burn.html" frameborder="0" height="300" width="300" allowfullscreen="true"></iframe>
<br>

<h2>Alerts</h2>
<a href="https://twitter.com/hashtag/alertscc">alertscc</a><br/>
<a href="https://m.pge.com/#outages">pgne outages</a><br/>
<a href="http://www.sparetheair.org">sparetheair.org</a><br/>
<br/>
<h2>Traffic</h2>
<a href="https://511.org">511.org - Traffic map</a><br/>
<a href="https://511.org/alerts/traffic">511.org - Traffic alerts</a><br/>
<a href="https://511.org/alerts/transit">511.org - Transist alerts</a><br/>
<br/>

<h2>Phone numbers</h2>
<table>
<tr>
<td>
(408) 808-4400 - Santa Clara County Sheriff's Department, Phone
</td>
</tr>
<tr>
<td>
(408) 615-4900 - Santa Clara City Fire Department, Phone
</td>
</tr>
<tr>
<td>
1-800-743-5002 - PGNE
</td>
</tr>
</table>
</body>
</html>
