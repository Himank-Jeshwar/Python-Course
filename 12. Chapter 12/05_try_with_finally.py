try:
    a=int(input("Enter a number = "))
    a=int(a)
except Exception as f:
    print(f)
    exit()
finally:
    print("Program Finished !")   