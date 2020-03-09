<?php
class dragonBall{
    private $ballCount;

    public function __construct(){
        $this->ballCount = 0;
    }

    public function iFoundaBall(){
        $this->ballCount++;
        if($this->ballCount===7){
            echo "You can ask for your wish.";
            $this->ballCount = 0;
        }
        else{
            echo "$this->ballCount";
            echo "<br>";
            echo "
            <form action='javascript:void(0);' method='POST'>
            <input name='fullname' type='text'/>
			<button type='submit'>Send</button>
            </form>
            ";
        }
    }
}

$db = new dragonBall();
if($_POST['fullname']){
    $db->iFoundaBall();
}
?>