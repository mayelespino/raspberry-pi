<html>
<head>
<style>
body {
  background-color: #DCDCDC;
}
</style>
</head>
<body>
<h1>3336 Fontana Pl</h1>
<h2>Ambiant sensors</h2>
<br>
<a href="index.php">[HOME]</a>
<pre>
<?php
$homepage = file_get_contents('http://wttr.in/94509');
echo $homepage;
?>
</pre>
Weather brought to you by: http://wttr.in
</body>
</html>
