
<?php

if($_GET){

    if(isset($_GET['insert'])){

        insert();

    }elseif(isset($_GET['select'])){

        select();

    }

}



    function select()

    {

       echo "The select function is called.";

    }

    function insert()

    {

       echo "The insert function is called.";

    }



?>



<input type="text" name="user" placeholder="enter a text" />
<input type="submit" value="submit" />