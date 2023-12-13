# LinearSearch
def LinearSearch():
    for i in range(len(student_list)):
        if key == student_list[i]:
            print("The Student was present at Training program!! at position", i+1)
            break
    else:
        print("The student was Absent in Training Program")
# Binary_search


def Binary_search():

    low = 0
    high = len(student_list)-1

    Found = False
    while low <= high and not Found:
        mid = (low+high)//2  # gives integer no.
        if key == student_list[mid]:
            Found = True
        elif key > student_list[mid]:
            low = mid+1
        else:
            high = mid-1
    if Found == True:
        print("The student was  present in Training Program!!! at position", mid+1)
    else:
        print("The student was  Absent in Training Program!!!")

# for Sorting


def SelectionSort():

    # Outer for loop is used larger iterations of indexes
    for i in range(0, len(student_list)-1):
        minIndex = i

        # Inner for loop is used for comparison in each larger iteration
        for j in range(i+1, len(student_list)):
            if (student_list[j] < student_list[minIndex]):
                minIndex = j

        if (minIndex != i):
            student_list[i], student_list[minIndex] = student_list[minIndex], student_list[i]

    print("The Sorted list is:", student_list)
# Fibonacci search


def fibonacci_search():
    F = []
    f0 = 0
    f1 = 1
    f2 = 1
    F.append(f0)
    F.append(f1)
    F.append(f2)
    while (f2 < len(student_list)):
        f0 = f1
        f1 = f2
        f2 = f0+f1
        F.append(f2)
    print("Required Fibonacci series is: ", F)

    offset = -1
    k = len(F)
    while (f2 > 1 and k >= 0):
        index = min(offset+F[k-2], n-1)
        if (key > student_list[index]):
            k = k-1
            offset = index
        elif (key < student_list[index]):
            k = k-2
        elif (key == student_list[index]):
            print(
                key, " Roll number was present for the program and found at position: ", index+1)
            return index
    else:
        print(key, " Roll number was absent")


def Sentinel_search():
    key = int(input("Enter the roll number of student to check his/her presence: "))
    for i in range(len(student_list)-1):
        if (student_list[i] == key):
            print(key, " Roll number was present for the program found at: ", i)
            break
    else:
        temp = 0
        temp = student_list[n-1]
        student_list[n-1] = key
        print(key, " Roll number was replaced with last roll number ")
        print("Roll number list after replacing last roll number: ", student_list)
        student_list[n-1] = temp


n = int(input("Enter the no of Students in class:"))
global student_list, key
student_list = []
print("Enter the Roll No. of students:")
for i in range(n):

    roll_no = int(input())
    student_list.append(roll_no)
print(student_list)

while (1):
    search = print(
        " 1.linear search\n 2.Binary search \n 3.Fibonacci Search \n 4.Sentinel Search \n 0.Exit")
    option = int(input("Enter your Choice:"))
    if (option == 1):
        key = int(input("Enter the Roll No. you want to search:"))
        LinearSearch()
    elif (option == 2):
        key = int(input("Enter the Roll No. you want to search:"))
        SelectionSort()
        Binary_search()
    elif (option == 3):
        key = int(input("Enter the Roll No. you want to search:"))
        SelectionSort()
        fibonacci_search()
    elif (option == 4):
        key = int(input("Enter the Roll No. you want to search:"))
        Sentinel_search()
    elif (option == 0):
        print("Exited!!")
        break
