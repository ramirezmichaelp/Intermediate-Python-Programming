#michael Ramirez
from Stack import Stack


def solveMaze(maze, startX, startY):
    x,y=startX,startY
    flag=False
    count=1
    maze[x][y]=count
    s=Stack()
    s.push([x,y])
    count=count+1

    ################
    while not s.isEmpty():
        x=s.peek()[0]
        y=s.peek()[1]

    
        if maze[x][y]=="G": #base case
            flag=True
            s.items=[]
            
        elif((maze[x-1][y]==" " or maze[x-1][y]=="G") ):
            s.push( [x-1,y] )
            if (maze[x-1][y]==" "):
                maze[x-1][y]=count
                count=count+1

            
        elif((maze[x][y+1]==" " or maze[x][y+1]=="G" ) ):
            s.push( [x,y+1] )
            if maze[x][y+1]==" ":
                maze[x][y+1]=count
                count=count+1
            
        elif((maze[x+1][y]==" "or  maze[x+1][y]=="G")):
            s.push( [x+1,y] )
            if (maze[x+1][y]==" "):
                maze[x+1][y]=count
                count=count+1
            
        elif((maze[x][y-1]==" " or maze[x][y-1]=="G")):
            s.push( [x,y-1] )
            if(maze[x][y-1]==" "):
               maze[x][y-1]=count
               count=count+1
        
        else:
            s.pop()
        
    
        
    return flag
