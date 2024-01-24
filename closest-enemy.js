function closestEnemy(matrix) {
    const rows = matrix.length;
    const cols = matrix[0].length;

    // Find the position of the player (1)
    let playerPos;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (matrix[i][j] === '1') {
                playerPos = { row: i, col: j };
                break;
            }
        }
    }
  
  // 0 0 0 0
  // 1 0 0 0
  // 0 0 0 2
  // 0 0 0 2

    // Initialize the minimum distance to a large value
    let minDistance = Infinity;

    // Iterate through the matrix to find the closest enemy (2)
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (matrix[i][j] === '2') {
                const enemyPos = { row: i, col: j };

                // Calculate the distance considering wrapping around
                const distance = Math.min(
                    Math.abs(playerPos.row - enemyPos.row),
                    rows - Math.abs(playerPos.row - enemyPos.row)
                ) +
                Math.min(
                    Math.abs(playerPos.col - enemyPos.col),
                    cols - Math.abs(playerPos.col - enemyPos.col)
                );

                // Update the minimum distance if the current enemy is closer
                minDistance = Math.min(minDistance, distance);
            }
        }
    }

    return minDistance;
}

// Example usage:
const strArr1 = ["0000", "1000", "0002", "0002"];
const strArr2 = ["000", "100", "200"];
const strArr3 = ["0000", "2010", "0000", "2002" ];
const result = closestEnemy(strArr3);
console.log(result);