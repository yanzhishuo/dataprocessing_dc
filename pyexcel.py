import xlrd
import openpyxl

def pyexcel(index,path):
    excel_list = list()
    data = xlrd.open_workbook(path)
    sheets = data.sheets()
    sheet_1_by_function=data.sheets()[0]
    sheet_1_by_index=data.sheet_by_index(0)
    sheet_1_by_name=data.sheet_by_name('Sheet2')
    n_of_rows=sheet_1_by_name.nrows
    for i in range(1,n_of_rows):
        cell_A=sheet_1_by_name.row(i)[index].value
        excel_list.append(cell_A)
    return excel_list

def readexcel(index,path):
    excel_list = list()
    data = xlrd.open_workbook(path)
    sheets = data.sheets()
    sheet_1_by_function=data.sheets()[0]
    sheet_1_by_index=data.sheet_by_index(0)
    sheet_1_by_name=data.sheet_by_name('Sheet1')
    n_of_rows=sheet_1_by_name.nrows
    for i in range(1,n_of_rows):
        cell_A=sheet_1_by_name.row(i)[index].value
        if cell_A:
            excel_list.append(cell_A)
    return excel_list

def reademptyexcel(index,path):
    excel_list = list()
    data = xlrd.open_workbook(path)
    sheets = data.sheets()
    sheet_1_by_function=data.sheets()[0]
    sheet_1_by_index=data.sheet_by_index(0)
    sheet_1_by_name=data.sheet_by_name('Sheet1')
    n_of_rows=sheet_1_by_name.nrows
    for i in range(1,n_of_rows):
        cell_A=sheet_1_by_name.row(i)[index].value
        excel_list.append(cell_A)
    return excel_list

def openexcel(index,path):
    excel_list = list()
    data = xlrd.open_workbook(path)
    wb = openpyxl.load_workbook(path)
    sheetname = wb.sheetnames[0]
    sheets = data.sheets()
    sheet_1_by_function=data.sheets()[0]
    sheet_1_by_index=data.sheet_by_index(0)
    sheet_1_by_name=data.sheet_by_name(sheetname)
    n_of_rows=sheet_1_by_name.nrows
    for i in range(0, n_of_rows):
        cell_A=sheet_1_by_name.row(i)[index].value
        if cell_A != '':
            excel_list.append(cell_A)
    return excel_list

if __name__ == "__main__":
    # print(readexcel(7,'/home/yzs/Downloads/data_require/final_new.xlsx'))
    # print(len(readexcel(7,'/home/yzs/Downloads/data_require/final_new.xlsx')))
    # data = xlrd.open_workbook('/home/yzs/Downloads/data_require/final_new.xlsx')
    # sheets = data.sheets()
    # sheet_1_by_function = data.sheets()[0]
    # sheet_1_by_index = data.sheet_by_index(0)
    # sheet_1_by_name = data.sheet_by_name('Sheet2')
    # sheet = data.get_sheet(0)
    print(openexcel(0, 'provincecc.xlsx'))

