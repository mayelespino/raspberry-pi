<html>
<head>
</head>
<body>

<h1>17440 Holiday Drive</h1>

<a href="index.php">[HOME]</a>

<h2>Ambiant sensors</h2>
<br/>

<table>
<tr>
<td>
<h3>Last check<h3/>
<b>
<?php
$homepage = file_get_contents('http://sensor.local:5000/time-stamp/');
echo $homepage;
?>

<td/>
<td>

<h3>Brightness</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/brightness/');
echo $homepage;
?>

<td/>
<td>
<h3>Humidity</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/humidity/');
echo $homepage;
?>

<td/>
<td>

<h3>On-board Temperature</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/onboard-temp/');
echo $homepage;
?>

<td/>
<tr>
<td>

<h3>Temperature</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/temperature/');
echo $homepage;
?>

<td/>
<td>

<h3>Barometer</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/barometer/');
echo $homepage;
?>

<td/>
<td>

<h3>Human sensor</h3>
<?php
$homepage = file_get_contents('http://sensor.local:5000/human/');
echo $homepage;
?>

<td/>
<tr/>
<table/>


<h2>AirNow</h2>

<table>
<tr>
<td>

<iframe height="340" src="https://epa.gov/cgi-bin/schoolflagwidgetcurrentforecast.cgi?z=95037&n=AirNow" width="230"></iframe>

<td/>
<td>

<h2>weatherwidget <h2/>
<a class="weatherwidget-io" href="https://forecast7.com/en/37d13n121d65/morgan-hill/" data-label_1="MORGAN HILL" data-label_2="WEATHER" data-theme="original" >MORGAN HILL WEATHER</a>
<script>
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
</script>

<td/>
<tr/>
<table/>
<h2>alertscc</h2>


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

<h2>usefull links</h2>
<a href="https://www.211bayarea.org/santaclara/crisis-services/">211.org</a> <br/>
<a href="https://www.sccgov.org/sites/oes/alertscc/Pages/home.aspx">sccgov.org</a> <br/>
<a href="https://twitter.com/hashtag/alertscc">alertscc</a><br>
</body>
</html>
