# Filter Syntax: list(filter(function,l))
greater_than_5=lambda num:num>5
less_than_5=lambda num:num<5
l1=[3,2,5,6,8,32,12,9]
print(f"Greater than 5 => {list(filter(greater_than_5,l1))}")
print(f"Less than 5 => {list(filter(less_than_5,l1))}")