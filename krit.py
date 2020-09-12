class Metod:
    total=0

    @staticmethod
    def status():
        print("Oбщее число гоблиняк", Metod.total)

    def __init__(self,name,hunger=0,boredom=0):
        self.name=name
        self.hunger=hunger
        self.boredom=boredom
        Metod.total+=1
    def turtule(self):
        print('Меня зовут', self.name)
    def __str__(self):
        ans='имя класса Metod\n'
        ans+='имя:'+self.name+'\n'
        return ans
def ache():
    print("Доступ к атрибуту класса Critter.total:", end=' ')
    print(Metod.total)
    print('Создание зверюшек.')
    c=Metod("Зверюшка 1")
    c1=Metod("Зверюшка 2")
    c2=Metod("Зверюшка 3")
    Metod.status()
    print('Доступ к атрибуту класса через обьект:', end='')
    print(c.total)
    print(c)
ache()
