print('start')
def checks_for_palindrom (x):
    #funkcja sprawdza czy słowo wysłane jako
    #argumen jet palindromem
    lenght=len(x)
   # print(f'Testowane słowo {x} posiada  {lenght} liter')
    for i in range (lenght-1):
        if x[i]!=x[(lenght-1) -i]:
            print(f' słowo {x} nie jest palindormem')
            return False
    print(f'\n==>> słowo  {x}  jest  palindromem !!')       
    return True
            #return True
    #na razie spr tylko czy pierwsze litery sa takie same
    #nie działa na duze i małę litery
    #przecinki i spacje ? 

a='alicja'
b='laddy'
c='kajak'
d='abccba'
test=checks_for_palindrom(a)
test=checks_for_palindrom(b)
test=checks_for_palindrom(c)
test=checks_for_palindrom(d)