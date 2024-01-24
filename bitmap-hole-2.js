
function BitmapHoles(strArr) { 

    //[[0,0], [1, 0], [1, 3], [2, 0], [2, 1], [2, 2], [3, 4]]
  
    let count = 0;
    let checker = false;
    let grid = [];
    let positions = [];
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
    
      for (var c=0; c < positions.length; c++){
          checker = false;
          for (var k=c+1; k < positions.length; k++){
              if (
                (positions[k][0] === positions[c][0]+1 && positions[k][1] === positions[c][1]) || 
                (positions[k][0] === positions[c][0] && positions[k][1] === positions[c][1]+1)
              ){
                  checker = true;
              }
          }
          if (checker === false){
              count += 1;
          }
      }
      return count;
    
    }
    
    const strArr1 = ["01111", "01101", "00011", "11110"]
    const strArr2 = ["1011", "0010"]
    const strArr3 = ["110", "000", "111"]
    console.log(BitmapHoles(strArr1)); //result 3