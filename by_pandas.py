import os
import pandas as pd

dir_name = './выгрузка озон_half2'
files = os.listdir(dir_name)
pattern_sheet = 'Шаблон для поставщика'


def read_excel(dir_name, file, pattern_sheet):
    excel_file = os.path.join(dir_name, file)
    workbook = pd.read_excel(excel_file, sheet_name=pattern_sheet, skiprows=[0, 2])
    return workbook


combiner = pd.DataFrame()
for file in files:
    wb = read_excel(dir_name, file, pattern_sheet)
    combiner = pd.concat([combiner, wb], sort=False, axis=0)

writer = pd.ExcelWriter('test_half2.xlsx')
combiner.to_excel(writer)
writer.save()
writer.close()
