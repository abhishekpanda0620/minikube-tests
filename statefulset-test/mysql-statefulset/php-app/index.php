<?php
$host = 'mysql-0.mysql';
$user = 'root';
$pass = 'my-secret-pw';

$conn = new mysqli($host, $user, $pass);
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully to MySQL!<br>";

$result = $conn->query("SELECT NOW() as now;");
$row = $result->fetch_assoc();
echo "Time from DB: " . $row['now'];
?>
