<html>
<head>
</head>
<body>

<h1>17440 Holiday Drive</h1>
<h2>Pi status</h2>

<table border=1>
<tr>
<td>

<a href="sensor.php">sensor PI</a>

</td><td>

<?php
// From URL to get webpage contents.
$url = "http://sensor.local/";
// Initialize a CURL session.
$ch = curl_init();
// Return Page contents.
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
//grab URL and pass it to the variable.
curl_setopt($ch, CURLOPT_URL, $url);
$result = curl_exec($ch);
echo $result;
?>

</td><td>

</td><td>

<a href="speaker.php">speaker PI</a>

</td><td>

<?php
// From URL to get webpage contents.
$url = "http://speaker.local/";
// Initialize a CURL session.
$ch = curl_init();
// Return Page contents.
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
//grab URL and pass it to the variable.
curl_setopt($ch, CURLOPT_URL, $url);
$result = curl_exec($ch);
echo $result;
?>

</td>
</td><td>

At home

</td><td>

<?php
// From URL to get webpage contents.
$url = "http://sensor.local:5000/bt-status/";
// Initialize a CURL session.
$ch = curl_init();
// Return Page contents.
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
//grab URL and pass it to the variable.
curl_setopt($ch, CURLOPT_URL, $url);
$result = curl_exec($ch);
echo $result;
?>

</td>
<tr/>
</table>

<h2>Weather</h2>
<iframe src="http://wttr.in/95037" height="130" width="240"></iframe>
<br>
<a href="weather.php">Full weather 95037</a><br/>

<br/>
<h2>Alerts</h2>
<a href="https://twitter.com/hashtag/alertscc">alertscc</a><br/>
<a href="https://www.sccgov.org/sites/oes/alertscc/Pages/home.aspx">sccgov.org</a> <br/>
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
