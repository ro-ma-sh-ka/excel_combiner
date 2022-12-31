import os
import pandas as pd

dir_name = './выгрузка озон'
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

# file1 = "2022-12-27 (Don't use) Аксессуары для клюшки.xlsx"
# wb1 = read_excel(dir_name, file1, pattern_sheet)
# print(wb1)
# file2 = "2022-12-27 SUP-доска.xlsx"
# wb2 = read_excel(dir_name, file2, pattern_sheet)
# print(wb2)
#
# combiner = pd.concat([wb1, wb2], sort=False, axis=0)

writer = pd.ExcelWriter('test.xlsx')
combiner.to_excel(writer)
writer.save()
