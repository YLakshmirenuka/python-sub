a=int(input("enter maximum star : "))
for i in range(0, a):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(a, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

Output:

    "D:\python practice\venv\Scripts\python.exe" "D:/python practice/pattern using nested for loop.py"
enter maximum star : 5
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


Process finished with exit code 0
