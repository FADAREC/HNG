<?php
declare(strict_types=1);

$start_time = microtime(true);

function respond(int $status_code, array $data): void {
    header('Content-Type: application/json');
    http_response_code($status_code);
    echo json_encode($data, JSON_UNESCAPED_SLASHES);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    header('Access-Control-Allow-Origin: *');
    header('Access-Control-Allow-Methods: GET, OPTIONS');
    header('Access-Control-Allow-Headers: Content-Type');
    http_response_code(204);
    exit;
}

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');

$requestUri = trim(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH), '/');
$scriptName = trim($_SERVER['SCRIPT_NAME'], '/');

if ($requestUri !== $scriptName) {
    respond(404, ["error" => "Route Not Found."]);
}

if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    respond(405, ["error" => "Method Not Allowed. Use GET request."]);
}

$nowUtc = (new DateTimeImmutable('now', new DateTimeZone('UTC')))->format(DATE_ATOM);
respond(200, [
    "email" => "fadarefolajimi67@gmail.com",
    "current_datetime" => $nowUtc,
    "github_url" => "https://github.com/FADAREC/HNG"
]);

$executionTime = round((microtime(true) - $start_time) * 1000, 2);
error_log("[INFO] API executed in {$executionTime} ms");
?>
