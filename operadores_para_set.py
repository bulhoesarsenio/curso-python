sets = {3,2,4}
sets_2 = {1,5,2,4}

# | uni os set

sets_3 = sets | sets_2

print(sets_3)

# & para verificar itens presentes em ambos sets

sets_4 = sets & sets_2
#if len(sets_4) == 0:
    
#    print('nada no set')

#else:
#    print(f'existem {len(sets_4)} iten(s) no set')
print(sets_4)

#- ^ deiferença entre os set da esquerda


sets_5 = sets - sets_2
sets_5 = sets_2 ^ sets

print(sets_5)

