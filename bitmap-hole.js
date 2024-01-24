
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
    
    //Step 3: Based on the positions check which are next to each other and are sequential.
    
    
    
    for(k=0; k<positions.length; k++) {
      const [row, column] = positions[k];
        
        //column=k
      //if()
        
      
      
      
    }
  
    
    return strArr;
  }
  
  
  const strArr1 = ["01111", "01101", "00011", "11110"]
  
  BitmapHole(strArr1)
  
  
  