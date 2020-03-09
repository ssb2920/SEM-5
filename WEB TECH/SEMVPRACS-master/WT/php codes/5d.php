//d.	Write a PHP script to display source code of a webpage

<?php
//d.	Write a PHP script to display source code of a webpage



$all_lines = file('https://www.w3resource.com/');
foreach ($all_lines as $line_num => $line)
 {
 	echo "Line No.-{$line_num}: " . htmlspecialchars($line) . "\n";
 }
?>
