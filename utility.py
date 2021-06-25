import re
import pandas as pd

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def htmlTable2df(raw_html):
    row = re.compile('<tr>(.*?)</tr>')
    row_ls = re.findall(row,raw_html)
    cell = re.compile('t.*?>(.*?)</t')
    table_ls = [re.findall(cell,c) for c in row_ls]
    company_df = pd.DataFrame(table_ls[1:],columns = table_ls[0])
    return company_df

def htmlGetData(raw_html):
    data = re.compile('<td.*?>(.*?)</td>')
    data_ls = re.findall(data,raw_html)
    return data_ls
