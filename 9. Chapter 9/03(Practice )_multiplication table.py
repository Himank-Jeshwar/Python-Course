for num1 in range(2,21): 
    with open(f"Multiplication table of {num1}.txt","w") as table:
        for num2 in range(1,11):
            table.write(f"{num1} X {num2} = {num1*num2}")
            if num2 != 10:
                table.write("\n") 