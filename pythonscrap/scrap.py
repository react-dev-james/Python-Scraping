try:
    from urllib.request import urlopen as uReq
except ImportError:
    from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import xlwt
from datetime import datetime

my_url = 'https://www.frankana.de/de/sale/monatsangebot.html'
uClient = uReq(my_url)
page_html =  uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

productnames =  page_soup.findAll("h2",{"class":"product-name"})
parents =  page_soup.findAll("li",{"class":"item"})
productnamevals = []
productpricevals = []

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.col(0).width = 12000
ws.col(1).width = 12000
i = 1
j = 1
ws.write(0, 1, 'Budget', style1)
ws.write(0, 0, 'Name', style1)
for parent in parents:
    childs =  parent.find("span",{"class":"price"}).string
    ws.write(i, 1, childs, style1)
    i = i+1
for name in productnames:
    name = name.string
    ws.write(j, 0, name, style1)
    j = j + 1
# ws.write(0, 0, 1234.56, style0)
# ws.write(1, 0, datetime.now(), style1)
# ws.write(2, 0, 1)
# ws.write(2, 1, 1)
# ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save('example.xls')
# def output(filename, sheet, list1, list2, x, y, z):
#     book = xlwt.Workbook()
#     sh = book.add_sheet(sheet)
#
#     variables = [x, y, z]
#     x_desc = 'Display'
#     y_desc = 'Dominance'
#     z_desc = 'Test'
#     desc = [x_desc, y_desc, z_desc]
#
#     col1_name = 'Stimulus Time'
#     col2_name = 'Reaction Time'
#
#     # You may need to group the variables together
#     # for n, (v_desc, v) in enumerate(zip(desc, variables)):
#     for n, v_desc, v in enumerate(zip(desc, variables)):
#         sh.write(n, 0, v_desc)
#         sh.write(n, 1, v)
#
#     n += 1
#
#     sh.write(n, 0, col1_name)
#     sh.write(n, 1, col2_name)
#
#     for m, e1 in enumerate(list1, n + 1):
#         sh.write(m, 0, e1)
#
#     for m, e2 in enumerate(list2, n + 1):
#         sh.write(m, 1, e2)
#
#     book.save(filename)
