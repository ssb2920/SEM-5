<?php 
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "crudDB";

$conn = new mysqli($servername, $username, $password, $dbname);

if($conn->connect_error){
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM `person_info`";

$result = $conn->query($sql);

if($result->num_rows === 0){
    echo "No Data Available";
}
else{
    while($row = $result->fetch_assoc()){
        echo "Name: " . $row['name'] . " DOB: " . $row['dob'] . " Contact: " . $row["contact"] . " Email: " . $row["email"] . "<br>";
    }
}

$conn->close();

?>

<html>
    <button><a href="options.html">Home</a></button>
</html>