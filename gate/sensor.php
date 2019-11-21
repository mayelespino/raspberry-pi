<html>
<head>
</head>
<body>

<h1>17440 Holiday Drive</h1>
<h2>Ambiant sensors</h2>
<b>
<?php
$homepage = file_get_contents('http://sensor.local:5000/time-stamp/');
echo $homepage;
?>
</b>
<br/>

<h2>Brightness</h2>
<?php
$homepage = file_get_contents('http://sensor.local:5000/brightness/');
echo $homepage;
?>
</br>

<h2>Humidity</h2>
<?php
$homepage = file_get_contents('http://sensor.local:5000/humidity/');
echo $homepage;
?>
</br>

<h2>On-board Temperature</h2>
<?php
$homepage = file_get_contents('http://sensor.local:5000/onboard-temp/');
echo $homepage;
?>
</br>

<h2>Temperature</h2>
<?php
$homepage = file_get_contents('http://sensor.local:5000/temperature/');
echo $homepage;
?>
</br>

<h2>Barometer</h2>
<?php
$homepage = file_get_contents('http://sensor.local:5000/barometer/');
echo $homepage;
?>
</br>


<h2>Human sensor</h2>
<?php
$homepage = file_get_contents('http://sensor.local:5000/human/');
echo $homepage;
?>
</br>


<h2>AirNow</h2>
<iframe height="340" src="https://epa.gov/cgi-bin/schoolflagwidgetcurrentforecast.cgi?z=95037&n=AirNow" width="230"></iframe>

<h2>weatherwidget <h2/>
<a class="weatherwidget-io" href="https://forecast7.com/en/37d13n121d65/morgan-hill/" data-label_1="MORGAN HILL" data-label_2="WEATHER" data-theme="original" >MORGAN HILL WEATHER</a>
<script>
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
</script>

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
