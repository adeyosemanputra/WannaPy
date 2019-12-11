<?php
$servername = "localhost";
$username = "";
$password = "";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$uuid = $_GET['uuid'];
$key = $_GET['key'];
$sqluuid = mysql_escape_string($uuid);
$sqlkey = mysql_escape_string($key);

if(isset($uuid) && isset($key)) {
    $stmt = $conn->prepare("INSERT INTO `database`.`keys` (`uuid`, `key`) VALUES (?, ?)");
    $stmt->bind_param("ss", $sqluuid, $sqlkey);
    $stmt->execute();
    $stmt->close();
}
