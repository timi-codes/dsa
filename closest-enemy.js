function ClosestEnemyII(strArr) { 
    const rows = strArr.length;
    const columns = strArr[0].length
  
    //Step  1: Find player and enemy
    let playerPosition = {}
    let enemyPositions = []
    
    for(let i=0; i < rows; i++) {
      for(let j=0; j < columns; j++) {
        if(strArr[i][j] === '1') {
          playerPosition = { row: i, col: j }
        }
  
        if(strArr[i][j] === '2') {
          enemyPositions.push({ row: i, col: j })
        }
      }
    }
  
    let distance = 0
    for(let i=0; i < enemyPositions.length; i+=2) {
      let currentDistance = 0;
  
  
      //Step 2:  Find the shortest distance between row distance and wrap around distance from enemy
      if(Math.abs(playerPosition.row) - enemyPositions[i].row < rows/2) {
        currentDistance = Math.abs(playerPosition.row - enemyPositions[i].row)
      } else {
        //Use wrap around ditance if it's less than row distance 
        currentDistance = rows - Math.abs(playerPosition.row - enemyPositions[i].row)
      }
  
      //Use column distance if it's less than wrap around ditance
      //Step 3: Find the shortest distance between column distance and wrap around distance
      if(Math.abs(playerPosition.col) - enemyPositions[i].col < columns/2) {
        currentDistance += Math.abs(playerPosition.col - enemyPositions[i].col)
      } else {
        //Use wrap around ditance if it's less than row distance 
        currentDistance += columns - Math.abs(playerPosition.col - enemyPositions[i].col)
      }
  
      if(distance == 0 || currentDistance < distance) distance = currentDistance
  
  
    }
  
  
    return distance; 
  
  }
  
  // 0 0 0 0
  // 2 0 1 0
  // 0 0 0 0
  // 2 0 0 2
  
     
  // keep this function call here 
  console.log(ClosestEnemyII(readline()));