class C2dVector:
    def __init__(self,k,j):
        self.kcap=k
        self.jcap=j
    def __str__(self):
        return (f"2D Vector of j and k = {self.kcap + self.jcap}")        
class C3dVector(C2dVector):
    def __init__(self, k,j,i):
        super().__init__(k,j)
        self.icap=i
    def __str__(self):
        return(f"3D Vector of i,j and k = {self.kcap+self.jcap+self.icap}")    
C2d=C2dVector(12,20)
C3d=C3dVector(12,45,20)
print(C2d)
print(C3d)