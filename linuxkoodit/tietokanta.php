<?php
$servername = "172.20.241.9";
$username = "dbaccess_ro";
$password = "vsdjkvwselkvwe234wv234vsdfas";
$dbname = "measurements";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
        }

$sql = "SELECT * FROM rawdata WHERE groupid=81 ORDER BY id DESC LIMIT 600";
$result = $conn->query($sql);


if ($result->num_rows > 0) {
    echo '<table border="1" cellpadding="5"><tr>';
   while($row = $result->fetch_assoc()) {
      echo "id: " . $row["id"] . " timestamp: " . $row["timestamp"] . " groupid: " . $row["groupid"] . " from_mac: " . $row["from_mac"]. " to_mac: " . $row["to_mac"] . " x: " . $row["sensorvalue_a"] . " y: " . $row["sensorvalue_b"] . " z: " . $row["sensorvalue_c"] . " mittauksennumero: " . $row["sensorvalue_d"] . " direction: " . $row["sensorvalue_e"] . " sensorvalue_f: " . $row["sensorvalue_f"] ."<br>" ;
   }
}

$conn->close();
?>
