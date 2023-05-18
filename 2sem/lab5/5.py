#класс с тремя стеками и одним массивом
class trial_stack:
    def __init__(self):
        #сам массив
        self.stacks = []
        #координата, куда будет добавлен следующий элемент первого стека
        self.i1 = 0
        # координата, куда будет добавлен следующий элемент вторго стека
        self.i2 = 0
        # координата, куда будет добавлен следующий элемент третьего стека
        self.i3 = 0
    #функция добавления элемента в первый стек
    def add_first(self,n):
        self.stacks.insert(self.i1,n)
        self.i1 += 1
        self.i2 += 1
        self.i3 += 1
    #функция удаления элемента из первого стека
    def delete_first(self):
        if self.i1 >= 1:
            #т.к. стек, то удаляется последний
            d = self.stacks.pop(self.i1-1)
            self.i1 -= 1
            self.i2 -= 1
            self.i3 -= 1
            print('This item was deleted from first stack:',d)
    #вывод первого стека
    def print_first(self):
        print('First stack:', self.stacks[:self.i1])
    # функция добавления элемента во второй стек
    def add_second(self,n):
        self.stacks.insert(self.i2,n)
        self.i2 += 1
        self.i3 += 1
    #функция удаления элемента из второго стека
    def delete_second(self):
        if self.i2-self.i1 >= 1:
            d = self.stacks.pop(self.i2-1)
            self.i2 -= 1
            self.i3 -= 1
            print('This item was deleted from second stack:', d)
    #вывод второго стека
    def print_second(self):
        print('Second stack:', self.stacks[self.i1:self.i2])
    # функция добавления элемента в третий стек
    def add_third(self,n):
        self.stacks.insert(self.i3,n)
        self.i3 += 1
    # функция удаления элемента из третьего стека
    def delete_third(self):
        if self.i3-self.i2 >= 1:
            d = self.stacks.pop(self.i3-1)
            self.i3 -= 1
            print('This item was deleted from third stack:', d)
    #вывод третьего стека
    def print_third(self):
        print('Third stack:', self.stacks[self.i2:self.i3])

stacks = trial_stack()

stacks.add_first(1)
stacks.add_second(10)
stacks.add_third(100)

stacks.add_first(2)
stacks.add_second(3)
stacks.add_third(4)

stacks.delete_first()
#stacks.delete_second()
#stacks.delete_third()

stacks.print_first()
stacks.print_second()
stacks.print_third()
