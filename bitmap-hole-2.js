function findContinousRegion(grid, row, column){
    // const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]] // UP, DOWN, LEFT, RIGHT directions
  
    const stack = [[row, column]]
  
    //Check for neighbouring zeros
    while(stack.length > 0){
      const [currentI, currentJ] = stack.pop()
  
      if(
        currentI >=0 && 
        currentI < grid.length && 
        currentJ >= 0 && 
        currentJ < grid[0].length &&
        grid[currentI][currentJ] === "0"
      ){
        grid[currentI][currentJ] = '1'
  
        stack.push([currentI - 1 , currentJ])
        stack.push([currentI + 1, currentJ])
        stack.push([currentI, currentJ - 1])
        stack.push([currentI, currentJ + 1])
  
      }
    }
  
  
    // for(let dir = 0; dir < dirs.length; dir++){
    //   const [dr, dc] = dirs[dir]
    //   findContinousRegion(grid, row + dr, column + dc)
    // }
    // findContinousRegion(grid, )
    // findContinousRegion(grid, row + 1, column)
    // findContinousRegion(grid, row, column - 1)
    // findContinousRegion(grid, row , column + 1)
  
  } 
  
  
  
  function BitmapHoles(strArr) { 
  
  
    //Step 1: Convert string array to 3D grid
    const grid = []
    const positions = []
  
    for(let i = 0; i < strArr.length; i++){
      const binaryArray = strArr[i].split("");
      grid.push(binaryArray)
  
      for(let j = 0; j < grid[i].length; j++){
        if(grid[i][j] === "0") positions.push([i, j]) 
      }
    }
  
  
    // Step 2: Determine/Record the row and column position of 0's
    // for(let j = 0; j < grid.length; j++){
  
    // }
  
  
  
  
    // Step 3: Contigous region=>Determine where there's rows or columns match of 0's in any of the four directions - up, down, left or right
    let regionCount = 0;
    for(let positionIndex = 0; positionIndex < positions.length; positionIndex++){
      const [row, column] = positions[positionIndex]
  
      if(grid[row][column] === "0"){
        regionCount = regionCount + 1
        findContinousRegion(grid, row, column)
      }
    }
  
    return regionCount;
  
  }
     
  // keep this function call here 
  /*
  0 1 1 1 1
  0 1 1 0 1
  0 0 0 1 1
  1 1 1 1 0
  */
  
  /*
  1 0 1 1
  0 0 1 0
  */
  console.log(BitmapHoles(readline()));