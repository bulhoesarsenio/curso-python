
import copy

dicinario_1 = {'nome': 'arsenio',
             'idade': '4'}

dicinario_2 = dicinario_1.copy()

dicinario_2 = copy.deepcopy(dicinario_1)


print(dicinario_1)  
print(dicinario_2)

