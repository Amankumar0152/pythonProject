for i in range(10): #range(stop)
    print(i)

for i in range (2, 10): #range(start, stop)
    print(i)

for i in range (2, 101, 2): #range(start, stop, step)
    print(i)

for i in range(1, 101, 2):
    print(i)

# #Questions 1
for i in range(1, 101):
    print(i)

#Question 2
for i in range(100, 0, -1):
    print(i)

#Question 3
n = (int(input("Enter a number for table: ")))
for i in range(1, 11):
    print(n * i)

#if you want to leave loop without any statement, not have to use then use pass
for i in range(5):
    pass

print("Some useful work")