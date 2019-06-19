# coding:utf-8
import xlrd, csv
from Common import ConfigManage


def getdata_from_Excel(excelfile_Name, sheetName='Sheet1'):
    excelfile_path = ConfigManage.dataPath + excelfile_Name + ".xlsx"
    # excelfile_path = excelfile_Name
    book = xlrd.open_workbook(excelfile_path)
    table = book.sheet_by_name(sheetName)
    # 获取第一行作为key值
    keys = table.row_values(0)
    # 获取总行数
    rowNum = table.nrows
    # 获取总列数
    colNum = table.ncols
    if rowNum <= 1:
        print("总行数小于1")
    else:
        r = []
        j = 1
        for i in range(rowNum - 1):
            s = {}
            # 从第二行取对应values值
            values = table.row_values(j)
            for x in range(colNum):
                '''读excel数字类型默认读出来的是float,在把excel单元格设置为文本，或数字前加分号（'）'''
                s[keys[x]] = str(values[x])
            r.append(s)
            j += 1
        return r


def getdata_from_Csv(csvfile_Name):
    csvfile_path = ConfigManage.dataPath + csvfile_Name+'.csv'
    with open(csvfile_path, "r", encoding="gbk") as f:
        reader = csv.DictReader(f)
        column = [row for row in reader]
    return column


if __name__ == "__main__":
    filepath = "d:\\ddt.xlsx"
    sheetName = "Sheet1"
    print(getdata_from_Excel(filepath))

    # r = ReadFile()
    # dic = r.GetData_From_Csv('d:\\ddt2.csv')
    # for item in dic:
    #     print(item)

# # exlce基本操作方法如下
#
# # 打开exlce表格，参数是文件路径
# data = xlrd.open_workbook('test.xlsx')
#
# # table = data.sheets()[0]           #  通过索引顺序获取
# # table = data.sheet_by_index(0)     #  通过索引顺序获取
# table = data.sheet_by_name(u'Sheet1')  # 通过名称获取
#
# nrows = table.nrows  # 获取总行数
# ncols = table.ncols  # 获取总列数
#
# # 　获取一行或一列的值，参数是第几行
# print
# table.row_values(0)  # 获取第一行值
# print
# table.col_values(0)  # 获取第一列
