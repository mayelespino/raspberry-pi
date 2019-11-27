<html>
<head>
</head>
<body>

<h1>17440 Holiday Drive</h1>

<table>
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

<a href="sounds.php">speaker PI</a>

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
<tr/>
</table>
<br/>
<a href="weather.php">weather at 95037</a><br/>
<a href="https://www.211bayarea.org/santaclara/crisis-services/">211.org</a><br/> 
<a href="https://twitter.com/hashtag/alertscc">alertscc</a><br/>
<a href="https://www.sccgov.org/sites/oes/alertscc/Pages/home.aspx">sccgov.org</a> <br/>
<br/>

<h2>Useful phone numbers</h2>
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
