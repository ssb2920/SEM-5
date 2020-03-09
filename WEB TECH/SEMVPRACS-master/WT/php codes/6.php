

<?php
//6.	Write a PHP program to that reads a date (dd/mm/yyy) as input and prints the day of the date. Jan. 1, 2016, is Friday. Note Leap years are to be considered.

// Two integers m and d separated by a single space in a line, m ,d represent the month and the day.
// Sample Input:
// 9 15
// Sample Output:

// The day is: Thursday


$days = explode(',', '0,31,60,91,121,152,182,213,244,274,305,335');
$format = explode(',', 'Wednesday,Thursday,Friday,Saturday,Sunday,Monday,Tuesday');
while (($line = trim(fgets(STDIN))) !== '') {
    sscanf($line, '%d %d', $m, $d);
    if ($m === 0) {
        break;
    }
    $n = $days[$m - 1] + $d;
    $today = $format[$n % 7];
    echo "The day is: ".$today, PHP_EOL;
}
?>

