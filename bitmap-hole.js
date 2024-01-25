function BitmapHole(strArr){
  
  let grid = []
  let positions = []
  let directions=[[1, 0], [-1, 0], [0, 1], [0, -1]]
  
  // Step 1: Convert strArr to a grid matrix 
    for(let i=0; i<strArr.length; i++){
      grid.push(strArr[i].split(""))
      
      // Step 2: Find the positions of 0's
      for(let j=0; j<grid[i].length; j++){
        if(grid[i][j] === "0"){
          positions.push([i, j])
        }
      }
    }
  console.log(`Print Grid \n`, grid)
  console.log(`Print Positions of 0's \n`, positions)
  
  //Step 3: Group by rows
  
  
  //Step 3: Based on the positions check which are adjacent
  function findContinousRegion(row, column){
    if ((row < 0 || row >= grid.length) || (column < 0 || column >= grid[0].length) || (grid[row][column] === '1')) return;
    
    //visited position of 0's
    grid[row][column] = '1';

    // for(let dir=0; dir<directions.length; dir++){
    //   findContinousRegion(row + dir, column + dir)
    // }
    
    findContinousRegion(row - 1, column) //UP
    findContinousRegion(row + 1, column) //DOWN
    findContinousRegion(row, column - 1) //LEFT
    findContinousRegion(row, column + 1) ////RIGHT
  }
  
  
  let count = 0;

  for(index=0; index < positions.length; index++) {
    const [row, column] = positions[index]
    
    if(grid[row][column] === '0'){
        count = count + 1
        findContinousRegion(row, column)
    }
  }
  
  console.log(count)

  
  return count
}