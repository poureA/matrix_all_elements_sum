class Overall(object) :
    '''class docstring'''
    def __init__(self,two_d_array) :
        self.m = two_d_array
    def overall(self)->(int,float) :
        '''return sum of all elements of the matrix\nreturn :\ninteger or float'''
        res = 0
        c = 0
        for i in self.m :
            for j in i :
                c+=j
            res += c
            c = 0
        return res
arr = list()
carrier = []
row = int(input('number of row :'))
col = int(input('number of column :'))
for i in range(row) :
    for j in range(col):
        carrier.append(int(input('number :')))
    arr.append(carrier)
    carrier = []
import numpy as np
arr = np.array(arr)
sample = Overall(arr)
print(sample.overall())
exit = input('enter any key to exit :')
