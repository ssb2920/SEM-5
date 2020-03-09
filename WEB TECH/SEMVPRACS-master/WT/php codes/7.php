
<!-- 7.	Write a PHP program which reads a text (only alphabetical characters and spaces.) and prints two words. The first one is the word which is arising most frequently in the text. The second one is the word which has the maximum number of letters.
A word is a sequence of letters which is separated by the spaces.
Input: A text is given in a line with following condition:
a. The number of letters in the text is less than or equal to 1000.
b. The number of letters in a word is less than or equal to 32.
c. There is only one word which is arise most frequently in given text.
d. There is only one word which has the maximum number of letters in given text. Sample 
Input: Thank you for your comment and your participation.
Sample Output: 
your participation. -->

<?php
 $str = trim(fgets(STDIN));
$arr = explode(' ', $str);
$arr2 = array_count_values($arr);
$word1 = array_search(max($arr2), $arr2);
$word2 = ''; 
foreach ($arr as $s) {
    if (strlen($s) > strlen($word2)) {
        $word2 = $s;
    }
} 
printf("%s %s\n", $word1, $word2);
?>
