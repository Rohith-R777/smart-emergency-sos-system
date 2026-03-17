<?php
declare(strict_types=1);

header('Content-Type: application/json');

const MAX_MESSAGE_LENGTH = 280;

function parseLocation(array $locationData): ?array
{
    $lat = filter_var($locationData['lat'] ?? null, FILTER_VALIDATE_FLOAT);
    $lng = filter_var($locationData['lng'] ?? null, FILTER_VALIDATE_FLOAT);

    if ($lat === false || $lng === false) {
        return null;
    }

    if ($lat < -90 || $lat > 90 || $lng < -180 || $lng > 180) {
        return null;
    }

    return ['lat' => $lat, 'lng' => $lng];
}

function parseIsoTimestamp(string $timestampRaw): ?string
{
    $normalizedTimestamp = str_replace('Z', '+00:00', $timestampRaw);
    $timestampObject = DateTimeImmutable::createFromFormat(DateTimeInterface::ATOM, $normalizedTimestamp)
        ?: DateTimeImmutable::createFromFormat('Y-m-d\\TH:i:s.uP', $normalizedTimestamp);

    if (!$timestampObject) {
        return null;
    }

    return $timestampObject->format(DateTimeInterface::ATOM);
}

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
    $location = parseLocation($data['location']);
}

$timestampRaw = trim((string)($data['timestamp'] ?? ''));
$timestamp = null;
if ($timestampRaw !== '') {
    $timestamp = parseIsoTimestamp($timestampRaw);
    if (!$timestamp) {
        http_response_code(400);
        echo json_encode([
            'status' => 'error',
            'message' => 'Invalid timestamp format.'
        ]);
        exit;
    }
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
