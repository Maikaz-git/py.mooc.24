# Write your solution here
lay = int(input('Layers: '))

def letterbox(n):
    if letterCount > 26:
         letterCount = 26

    boxWidth = letterCount * 2

    for y in range(boxWidth+1):
        for x in range(boxWidth+1):

            xDistanceFromCenter = abs(x-boxWidth//2)
            yDistanceFromCenter = abs(y-boxWidth//2)
            maxDistance = max(xDistanceFromCenter,yDistanceFromCenter)

            letter = chr(ord('A') + maxDistance
            print(letter), end = "")
        print()




letterbox(int(input("Kerrokset:")))



exit()



row = (lay*2)-1 

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

n_lst = []
        
for i in range(row):
    l = []
    for j in range(row):
        l.append("*")
    n_lst.append(l)


letter_1 = lst[lay-1]

low = 0
high = row-1 



for i in range(lay):

    for j in range(low,high+1):
        n_lst[i][j] = lst[lay-1-i]
    
    for j in range(low+1, high+1):
        n_lst[j][high] = lst[lay-1-i]

    for j in range(high, low-1, -1):
        n_lst[high][j] = lst[lay-1-i]
    
    for j in range(high-1, low, -1):
        n_lst[j][low] = lst[lay-1-i]
    
    low += 1
    high -= 1



# for el in n_lst:
#     print(el) 
   



for i in range(row):
    for j in range(row):
        print(n_lst[i][j].upper(), end="")
    print()   


