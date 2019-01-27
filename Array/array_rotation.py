'''
Q: Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
URL: https://www.geeksforgeeks.org/array-rotation/
'''

def rotate(arr, rot):
    rotated_array = []
    rot = rot % len(arr)

    for i in range(0, len(arr)):
        rotated_array.append(arr[(i+rot)%len(arr)])

    return rotated_array


def main():
    n = int(input("Enter size of array\n"))
    d = int(input("Enter the number of rotations to be performed\n"))
    arr = []
    print("Enter {size} elements".format(size=n))
    for i in range(0, n):
        a = int(input())
        arr.append(a)

    result = rotate(arr, d)

    print(result)

main()
