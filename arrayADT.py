class MyArray:
    myarray = []
    def __init__(self, total_size, used_size):
        self.t_size = total_size
        self.used_size = used_size
  
    def setVal(self):
        for i in range(self.used_size):
            n = input(f"Enter The Value at {i}: ")
            self.myarray[i] = n
            i += 1
        print(self.myarray)
m = MyArray(10, 5)
m.setVal()
