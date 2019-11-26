<html>
<head>
</head>
<body>

<h1>17440 Holiday Drive</h1>

<table>
<tr>
<td>
<a href="sensor.php">sensor</a>
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

<a href="sounds.php">sounds</a>

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
<td>
<a href="weather.php">weather at 95037</a>
</td>
</tr>

</table>

</body>
</html>
