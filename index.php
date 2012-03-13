<!DOCTYPE html>
<html>

<head>

	<title> There and Back Again </title>
	<link href='http://fonts.googleapis.com/css?family=Fondamento' rel='stylesheet' type='text/css'>
	<link rel='Stylesheet' type='text/css' HREF = 'style.css'>

</head>

<body>
<blockquote>
<p>
<?php 
	$arrCSV = array();
	if (($handle = fopen("sentences.csv", "r")) !==FALSE) {
 		$key = 0;

		while (($data = fgetcsv($handle , 0, "|")) !==FALSE) {
			$c = count($data);

			for ($x=0;$x<$c;$x++) {
				$arrCSV[$key][$x] = $data[$x];
			}
		$key++;
		}
		fclose($handle);
	}
?>
<?php 
	$max = max(array_map('count', $arrCSV));
	$num = rand(0,$max);
	echo $num;
?>
</p>
</blockquote>
</body>

</html>