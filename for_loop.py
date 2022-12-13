'''
DATE:11TH DEC 2022
DAY: SUNDAY
TOPIC: FOR LOOP
AUTHOR: RAMA BHARGAVI
'''
a= 1,2,3
print(*a) #1 2 3
for i  in a:
    print(i,end=' ') #1 2 3
for i in range(5):
    print(i) # 1 2 3 4 (vertically)   
n=int(input('enter the value of n:'))
for i in range(1,n+1):
    print(i,end=" ")    # 1 2 3 4 5
