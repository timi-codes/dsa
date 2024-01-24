
function BitmapHole(strArr){
  
  let grid = []
  let positions = []
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
  
  
  //Step 3: Based on the positions check which are next to each other and are sequential.
  
  
  let count = 0;

  for(index=0; index < positions.length; index++) {
    const [row, column] = positions[index]
    
    grid[row][column] = "-"
    
    //Check Right
    if(grid[row][column] === grid[row][column + 1]){
      count = count + 1
      // grid[row][column + 1] = "-"
      
      console.log(`Print Grid \n`, grid)
    }
    
    //Check Left
    if(grid[row][column] === grid[row][column - 1]){
      count = count + 1
      // grid[row][column - 1] = "-"
      console.log(`Print Grid \n`, grid)
    }
    
    //Check Top
    if(grid[row - 1] && grid[row][column] === grid[row - 1][column]){
      count = count + 1
      // grid[row - 1][column] = "-"
        console.log(`Print Grid \n`, grid)
    }
    
    //Check Bottom
    if(grid[row + 1] && grid[row][column] === grid[row + 1][column]){
      count = count + 1
      // grid[row + 1][column] = "-"
        console.log(`Print Grid \n`, grid)
    }
  }
  
  console.log(count)

  
  return strArr;
}


const strArr1 = ["01111", "01101", "00011", "11110"]
const strArr2 = ["1011", "0010"]
const strArr3 = ["110", "000", "111"]


BitmapHole(strArr3)


