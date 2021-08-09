print('start')
def checks_for_palindrom (x):
    #funkcja sprawdza czy słowo wysłane jako
    #argumen jet palindromem
    lenght=len(x)
    print(lenght)
    for i in range (lenght-1):
        print(x)
        if x[i]==x[(lenght-1) -i]:
            print(x[i],x[(lenght-1) -i])
            #return True
    #na razie spr tylko czy pierwsze litery sa takie same
    #nie działa na duze i małę litery
    #przecinki i spacje ? 

a='alicja'

checks_for_palindrom(a)