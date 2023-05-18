def check(field):
        #проверка вертикальных линий
        for i in range(len(field[0])):
                c_x = 0
                c_o = 0
                for j in range(len(field)):
                        if field[i][j] == 'X':
                                c_x+=1
                        else:
                                c_o+=1
                if c_x == 3:
                        return 'X'
                elif c_o == 3:
                        return '0'
        #проверка горизонтальных линий
        for i in range(len(field)):
                c_x = 0
                c_o = 0
                for j in range(len(field[0])):
                        if field[i][j] == 'X':
                                c_x += 1
                        else:
                                c_o += 1
                if c_x == 3:
                        return 'X'
                elif c_o == 3:
                        return '0'
        #проверка первой диагонали
        c_x = 0
        c_o = 0
        for i in range(len(field)):
                if field[i][i] == 'X':
                        c_x += 1
                else:
                        c_o += 1
                if c_x == 3:
                        return 'X'
                elif c_o == 3:
                        return '0'
        #проверка второй диагонали
        c_x = 0
        c_o = 0
        for i in range(len(field)):
                j = len(field[0]) - 1 - i
                if field[i][j] == 'X':
                        c_x += 1
                else:
                        c_o += 1
                if c_x == 3:
                        return 'X'
                elif c_o == 3:
                        return '0'
        return 'draw'
field = [['0','0','X'],
        ['0','X','X'],
        ['X','0','X']]
res = check(field)
if res == 'X':
        print('X won')
elif res == '0':
        print('0 won')
else:
        print('draw')
