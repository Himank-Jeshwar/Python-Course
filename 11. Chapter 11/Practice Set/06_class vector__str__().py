class Vector:
    def __init__(self,vec_list):
        self.vec_list=vec_list
    def __str__(self):
        return (f"{self.vec_list[0]}i + {self.vec_list[1]}j + {self.vec_list[2]}k")
dim=Vector([7,8,10])
print(dim)        