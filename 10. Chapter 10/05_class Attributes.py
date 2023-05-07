#CLASS ATTRIBUTES (works on all instances)
class Worker:
    company="Youtube"
Himank=Worker()
Siddharth=Worker()
Worker.company="Microsoft" # <== Class Attribute used
print(f"Himank works in {Himank.company}")
print(f"Siddharth works in {Siddharth.company}")