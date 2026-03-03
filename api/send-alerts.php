<?php

function send_alert($message, $phone_numbers, $emails) {
    // Send SMS notifications
    foreach ($phone_numbers as $number) {
        // Assuming a fictional function send_sms exists
        send_sms($number, $message);
    }
    
    // Send Email notifications
    foreach ($emails as $email) {
        // Assuming a fictional function send_email exists
        send_email($email, 'Emergency Alert', $message);
    }
}

?>