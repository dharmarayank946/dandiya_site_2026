<?php
/* ==========================================================================
   Dandiya Connect Pune 2026 - Hostinger MySQL Backend API
   ========================================================================== */

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');

// Hostinger Database Configuration
$db_host = 'localhost';          // Standard Hostinger MySQL Host
$db_user = 'u123456789_dandiya'; // Replace with your Hostinger DB Username
$db_pass = 'YOUR_DB_PASSWORD';   // Replace with your Hostinger DB Password
$db_name = 'u123456789_pass_db'; // Replace with your Hostinger DB Name

// Connect to MySQL
$conn = new mysqli($db_host, $db_user, $db_pass, $db_name);

if ($conn->connect_error) {
    http_response_code(500);
    echo json_encode([
        'status' => 'error',
        'message' => 'Database Connection Failed: ' . $conn->connect_error
    ]);
    exit();
}

// Handle POST Request
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $fullname   = isset($_POST['fullname']) ? trim($_POST['fullname']) : '';
    $email      = isset($_POST['email']) ? trim($_POST['email']) : '';
    $phone      = isset($_POST['phone']) ? trim($_POST['phone']) : '';
    $pass_type  = isset($_POST['pass_type']) ? trim($_POST['pass_type']) : '';
    $quantity   = isset($_POST['quantity']) ? intval($_POST['quantity']) : 1;
    $total_price = isset($_POST['total_price']) ? floatval($_POST['total_price']) : 0.00;

    if (empty($fullname) || empty($email) || empty($phone) || empty($pass_type)) {
        http_response_code(400);
        echo json_encode([
            'status' => 'error',
            'message' => 'Please fill in all required fields.'
        ]);
        exit();
    }

    // Insert into MySQL Database
    $stmt = $conn->prepare("INSERT INTO bookings (fullname, email, phone, pass_type, quantity, total_price) VALUES (?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("ssssid", $fullname, $email, $phone, $pass_type, $quantity, $total_price);

    if ($stmt->execute()) {
        echo json_encode([
            'status' => 'success',
            'booking_id' => $stmt->insert_id,
            'message' => 'Pass booked successfully! Confirmation sent to your email.'
        ]);
    } else {
        http_response_code(500);
        echo json_encode([
            'status' => 'error',
            'message' => 'Booking failed: ' . $stmt->error
        ]);
    }

    $stmt->close();
} else {
    http_response_code(405);
    echo json_encode([
        'status' => 'error',
        'message' => 'Invalid Request Method.'
    ]);
}

$conn->close();
?>
