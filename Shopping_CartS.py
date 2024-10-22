class addition:
    num = 0
    def add(self):
        self.num += 1
        return self.num
addit = addition()
addit.add()
addit.add()
addit.add()
addit.add()
print(addit.__dict__)
