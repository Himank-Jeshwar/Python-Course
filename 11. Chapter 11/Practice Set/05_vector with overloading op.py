# EXPECTED OUTPUT :=

# Addition output => 7 k0 + 20 k1
# Multiplication output => 10 k0 + 96 k1

class Vector:
    def __init__(self,vec_list):
        self.vec_list=vec_list
    def __str__(self):
        answer=""
        index_No=0
        for num in self.vec_list:
            answer+=(f" {num} k{index_No} +")
            index_No=index_No+1
        return answer[:-1]
    def __add__(self,vec2):
        new_vec=[]
        for num in range(len(self.vec_list)):
            new_vec.append(self.vec_list[num] + vec2.vec_list[num])
        return Vector(new_vec)  

    def __mul__(self,vec2):
        new_vec=[]
        for num in range(len(self.vec_list)):
            new_vec.append(self.vec_list[num]*vec2.vec_list[num])
        return Vector(new_vec)    
v1=Vector([2,8])
v2=Vector([5,12])
print(f"Addition output = {v1+v2}")            
print(f"Multiplication output = {v1*v2}")