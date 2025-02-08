<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Treasure Hunt Game</title>
</head>
<body>
    <h2>Interactive Treasure Hunt</h2>
    <form action="process.php" method="post">
        <label for="number">Enter a Number:</label>
        <input type="number" id="number" name="number" required>
        <br><br>
        <label for="text">Enter a Text:</label>
        <input type="text" id="text" name="text" required>
        <br><br>
        <button type="submit">Solve the Puzzle</button>
    </form>
</body>
</html>
