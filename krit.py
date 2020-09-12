class Metod:
    def __init__(self,name,hunger=0,boredom=0):
        self.name=name
        self.hunger=hunger
        self.boredom=boredom
    def turtule(self):
        print('Меня зовут', self.name)
    def __str__(self):
        ans='имя класса Metod\n'
        ans+='имя:'+self.name+'\n'
        return ans
def ache():
    c=Metod("Гоблин")
    c1=Metod('bobrik')
    print(c)
ache()
