<html>
<head>
</head>
<body>
<h1>17440 Holiday Drive</h1>
<h2>Ambiant sensors</h2>
<br>
<a href="index.php">[HOME]</a>
<pre>
<?php
$homepage = file_get_contents('http://wttr.in/95037');
echo $homepage;
?>
</pre>
Weather brought to you by: http://wttr.in
</body>
</html>
