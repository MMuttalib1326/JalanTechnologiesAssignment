'''
The time complexity of this program is O(n2) as the rotate function is called each time till the position value is satisfied,
and in each rotate function there is another for loop which assigns the value inside a list to the next position.

The space complexity of this program in worst case is O(n) as the number of elements increase the amount of space increases.
The best space and time complexity will be for a single element O(1).
'''


#function to rotate the array in given direction
def rotate(A,n,d):
    if d==0:
        x = A[n-1]
        for i in range(n-1,0,-1):
            A[i] = A[i-1]
        A[0]=x
    elif d==1:
        x = A[0]
        for i in range(0,n-1):
            A[i] = A[i+1]
        A[n-1]=x
        
#driver logic
A = list()
N = int(input("Enter the size of array: "))
if (N<=0):
    print("Array length should be greater than 0")

print("Enter the elements of the array: ")
for i in range(N):
    k = int(input(""))
    A.append(k)
print("Array is: ",A)
P = int(input("Enter the position (>0 and <N): "))
if (P<=0 or P>N):
    print("Position should be >0 and <N")
D = int(input("Enter the direction (1:right || 0:left): "))
if (D>1 or D<0):
    print("Direction should be 1 or 0")

#logic for moving to the position
for i in range(0,P):
    rotate(A, N, D)
print(A)
