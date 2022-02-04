import math
 
def gridSize(n):
     
    grid = []
    a = math.sqrt(n)

    while True:
        
        print("Trying again, not integer..")
        a = math.floor(a)
        n % a != 0
        if n % a != 0:
            a -= 1
        else: break
    b = n/a

    grid.append(int(b))
    grid.append(int(a))



    print(f'Highest two divisible factors are {int(b)} and {int(a)}')
    return grid
         

if __name__ == "__main__":
    gridSize()