print('введите стороны треугольника')  #почему'трЕугольник'если там ТРИ угла?
a=float(input('сторона a='))
b=float(input('сторона b='))
c=float(input('сторона c='))
if a<b+c and b<c+a and c<b+a: #если сторона т-ка большесуммы двух других сторон то такого т-ка не бывает
    print('можно построить')
    p=((a+b+c)*0.5)#полупериметор
    s=(p*(p-a)*(p-b)*(p-c))**(1/2) #'**(1./2)'-извечение корня без библиотек в python2 надо ставить '.'после 1
    print('S=',s,'чего-то в квадрате')
else:
    print('нельзя построить')

