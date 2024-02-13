grid=[  [0,0,0,0],
        [0,1,1,1],
        [0,0,0,0],
        [1,1,1,0],
        [0,0,0,0]]
r=len(grid)
c=len(grid[0])
dict={}
def getPath(r,c,grid,dict):
    if(r<0 or c<0 or grid[r][c]!=0):
        return False
    if(r==0 and c==0):
        return True 
    if((r-1,c) in dict or (r,c-1) in dict or getPath(r-1,c,grid,dict) or getPath(r,c-1,grid,dict)):
        dict[(r,c)]=0
        return True
    return False

getPath(r-1,c-1,grid,dict)
print(dict)