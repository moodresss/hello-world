a=int(input())
from beautifultable import BeautifulTable


h0=["умножить на"]
h1=[1,a]
h2=[2,a*2]
h3=[3,a*3]
h4=[4,a*4]
h5=[5,a*5]

h0.append("результат")

table = BeautifulTable()
table.column_headers = h0
table.append_row(h1)
table.append_row(h2)
table.append_row(h3)
table.append_row(h4)
table.append_row(h5)
print(table)
