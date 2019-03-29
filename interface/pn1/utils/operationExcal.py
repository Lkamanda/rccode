import xlrd
from xlutils.copy import copy
from pn1.utils.public import *


class OperationExcal:
    def getExcal(self):
        db = xlrd.open_workbook(data_dir(data='data', fileName='data.xls'))
        # 获取excal第一个sheet
        sheet = db.sheet_by_index(0)
        return sheet

    def get_rows(self):
        '''获取excal的行数'''
        return self.getExcal().nrows

opera = OperationExcal()
print(opera.get_rows())





