time = input("Enter a timestamp(like 24:00): ")
print(type(time))

h = int(time.split(":")[0])
if h <12:
    print("Good Morning")
elif h ==12:
    print("Good Noons")
elif h >12:
    print("Good Night")
