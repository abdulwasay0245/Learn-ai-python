import time

userinput = input("Write start to begin countdown...")
def countdown():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

    print("Liftoff!")

if userinput == "start":
    countdown()
else:
    print("Invalid input")
