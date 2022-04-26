def get_summ(one, two, delimiter='&'):
    phrase = f'{one}{delimiter}{two}'
    return(phrase)

a = get_summ('Learn', 'Python')
b = get_summ('Привет', 'Алсу', delimiter=',')
print(a, b)
print(a.upper())
