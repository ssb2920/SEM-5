<?php 
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "crudDB";

$conn = new mysqli($servername, $username, $password, $dbname);

if($conn->connect_error){
    die("Connection failed: " . $conn->connect_error);
}

if(isset($_POST)){
    $name = $_POST['name'];
    $dob = $_POST['dob'];
    $contact = $_POST['phone'];
    $email = $_POST['email'];
    echo $name . "<br>" . $dob . "<br>" . $contact . "<br>" . $email . "<br>";

    $sql = "INSERT INTO `person_info`(`name`, `dob`, `contact`, `email`) VALUES ('$name', '$dob', '$contact', '$email');";

    if($conn->query($sql) === TRUE){
        echo "Data successfully entered";    
    }
    else{
        echo "Error while inserting into table. <br>" . $conn->error;
    }
}
else{
    echo "Error occured while receiving data";
}
$conn->close();

?>

<html>
    <button><a href="options.html">Home</a></button>
</html>
