cube=lambda a:a**3
# Method 1
cube_list=[cube(i) for i in range(1,6)]
print(cube_list)
# Method 2
l1=[u for u in range(1,6)]
print(list(map(cube,l1)))