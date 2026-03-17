<?php
declare(strict_types=1);

header('Content-Type: application/json');

const MAX_MESSAGE_LENGTH = 280;

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Method not allowed.']);
    exit;
}

$rawPayload = file_get_contents('php://input');
$data = json_decode($rawPayload ?? '', true);

if (!is_array($data)) {
    http_response_code(400);
    echo json_encode(['status' => 'error', 'message' => 'Invalid JSON payload.']);
    exit;
}

$message = trim((string)($data['message'] ?? ''));
if ($message === '') {
    http_response_code(400);
    echo json_encode(['status' => 'error', 'message' => 'Message is required.']);
    exit;
}

if (strlen($message) > MAX_MESSAGE_LENGTH) {
    http_response_code(400);
    echo json_encode([
        'status' => 'error',
        'message' => 'Message exceeds the maximum length.'
    ]);
    exit;
}

$location = null;
if (isset($data['location']) && is_array($data['location'])) {
    $lat = filter_var($data['location']['lat'] ?? null, FILTER_VALIDATE_FLOAT);
    $lng = filter_var($data['location']['lng'] ?? null, FILTER_VALIDATE_FLOAT);

    if ($lat !== false && $lng !== false) {
        $location = ['lat' => $lat, 'lng' => $lng];
    }
}

$timestampRaw = trim((string)($data['timestamp'] ?? ''));
$timestamp = null;
if ($timestampRaw !== '') {
    $normalizedTimestamp = str_replace('Z', '+00:00', $timestampRaw);
    $timestampObject = DateTimeImmutable::createFromFormat(DateTimeInterface::ATOM, $normalizedTimestamp)
        ?: DateTimeImmutable::createFromFormat('Y-m-d\\TH:i:s.uP', $normalizedTimestamp);

    if (!$timestampObject) {
        http_response_code(400);
        echo json_encode([
            'status' => 'error',
            'message' => 'Invalid timestamp format.'
        ]);
        exit;
    }

    $timestamp = $timestampObject->format(DateTimeInterface::ATOM);
}

$record = [
    'message' => $message,
    'location' => $location,
    'timestamp' => $timestamp,
    'received_at' => gmdate('c')
];

$logFile = __DIR__ . '/alerts.log';
file_put_contents(
    $logFile,
    json_encode($record, JSON_UNESCAPED_SLASHES) . PHP_EOL,
    FILE_APPEND | LOCK_EX
);

echo json_encode([
    'status' => 'ok',
    'message' => 'Alert received. Help is on the way.',
    'location' => $location
]);
?>
