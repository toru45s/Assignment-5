<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = $_POST['number'];
    $text = $_POST['text'];

    // Execute Python script and pass user input
    $command = escapeshellcmd("python3 process.py " . escapeshellarg($number) . " " . escapeshellarg($text));
    exec($command, $output);

    echo "<h2>Results:</h2>";

    foreach ($output as $o) {
        echo "<pre>$o</pre>";
    }
}
?>