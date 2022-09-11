from bs4 import BeautifulSoup
import requests

# <head>
# </head>
#<body>
#   <table>
#       <thead>
#       <tr>
#       <th> </th>
#       </tr>
#       </thead>
#       <tbody>
#       <tr>
#       <td> </td>
#       </tr>
#       </tbody>
#       <tfoot>
#       <tr>
#       <td> </td>
#       </tr>
#       </tfoot>
#   </table>
#</body>


req = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
link = BeautifulSoup(req.text, 'html.parser') # html5lib
#print(link)

main = link.findAll('div', attrs={'id': 'contentDiv'})
# print(main)
header_list = []
dataset = []
for obj in main:
    for table_index in obj.find_all('table'):
        for table_trs in table_index.find_all('tr'):
            td_list = []
            if table_trs.find_all('th'):
                # header_list = [header_data.get_text() for header_data do table_trs.find_all('th')]
                for header_data in table_trs.find_all('th'):
                    header_list.append(header_data.text)
            for index, td in enumerate(table_trs.find_all('td')):
                if index == 0:
                    td_list.append(td.get_text())
                elif td.get_text() != '':
                    td_list.append(float(td.get_text().replace(',', '.')))
            dataset.append(td_list)
del dataset[0]

# print(header_list, 'header')
# print(dataset, 'body')

# df = pd.DataFrame(dataset, columns=header_list, index=range(1, 11))
# print(df)
# df.to_excel("CursBNR.xls", header=header_list, index=0)

df.to_excel('CursBNR.xls', header=header)



