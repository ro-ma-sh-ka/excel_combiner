import os
import pandas as pd
from openpyxl import load_workbook

dir_name = './выгрузка озон'
files = os.listdir(dir_name)
pattern_sheet = 'Шаблон для поставщика'

for file in files:
    excel_file = os.path.join(dir_name, file)
    workbook = pd.read_excel(excel_file, sheet_name=pattern_sheet, skiprows=[0, 2])
    print(workbook)
    print()
    print(workbook.columns.ravel())
    #
    # worksheet = workbook[pattern_sheet]
    # columns_list = []
    # current_row = 2
    # for col in worksheet.iter_cols(min_row=2):
    #     if col[0].value not in columns_list:
    #         columns_list.append(col[0].value)
    #         new_column = []
    #         for row in col:
    #             new_column.append(row.value)
    #         df[col[0].value] = new_column
    #
    # writer = pd.ExcelWriter('test.xlsx')
    # df.to_excel(writer)
    # writer.save()

# https://dfedorov.spb.ru/pandas/%D0%A2%D0%B8%D0%BF%D0%B8%D1%87%D0%BD%D1%8B%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B8%20Excel,%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B5%D0%BC%D0%BE%D0%BD%D1%81%D1%82%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%B2%20pandas.html
# df_base = pd.DataFrame()
#
# for file in files:
#     excel_file = os.path.join(dir_name, file)
#     df = pd.read_excel(excel_file, sheet_name=pattern_sheet)
#     df_base = df_base.reindex(columns=df.columns)
#     df_base = df_base.append(df, ignore_index=True)
#
#     writer = pd.ExcelWriter('test.xlsx')
#     df_base.to_excel(writer)
#     writer.save()
