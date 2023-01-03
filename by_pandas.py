import os
import pandas as pd


def create_file_list(dir_name):
    file_list = os.listdir(dir_name)
    return file_list


def combine(work_dir, files, pattern_sheet):
    combiner = pd.DataFrame()
    for file in files:
        excel_file = os.path.join(work_dir, file)
        workbook = pd.read_excel(excel_file, sheet_name=pattern_sheet, skiprows=[0, 2])
        combiner = pd.concat([combiner, workbook], sort=False, axis=0)
    return combiner


def write_to_excel(result_file, pattern_sheet, combiner):
    with pd.ExcelWriter(result_file) as writer:
        combiner.to_excel(writer, sheet_name=pattern_sheet)


# dir_name = './выгрузка озон_small'
# files = os.listdir(dir_name)
# pattern_sheet = 'Шаблон для поставщика'
# result_file = os.path.join(dir_name, '_combiner_result.xlsx')
#
# combiner = combine(dir_name, files, pattern_sheet)
# write_to_excel(result_file, pattern_sheet, combiner)
