from lap.Workcalculator import Workcalculator
from Excelwriter import Excelwriter as Write
import pandas as pd
wc = Workcalculator(file='datas/Work1.xlsx',sheet='i', weights=250, trees=200)

weightss = [9800, 9875, 9870, 9789]

def excel_writer(file_name, data):
        with pd.ExcelWriter(f'{file_name}.xlsx') as writer:
            data.to_excel(writer, sheet_name='Salary')


print(excel_writer(file_name='salary', data=wc.Normal_case(weightss)))