import xlrd
from xlutils.copy import copy
from interface.pn1.utils.public import *
from interface.pn1.utils.excal_data import *


class OperationExcal:

    def getExcal(self):
        db = xlrd.open_workbook(data_dir(data='data', fileName='data1.xlsx'))
        # 获取excal第一个sheet
        sheet = db.sheet_by_index(0)
        return sheet

    def get_rows(self):
        """获取excal的行数"""
        return self.getExcal().nrows

    def get_row_cell(self, row, col):
        """
        获取单元格内容
        :param row: 行
        :param col: 列
        :return: 内容
        """""
        return self.getExcal().cell_value(row, col)

    def get_caseID(self, row):
        """获取测试ID"""
        return self.get_row_cell(row, getCaseID())

    def get_url(self, row):
        """获取请求地址"""
        # 行不确定,列确定
        return self.get_row_cell(row, getUrl())

    def get_request_data(self, row):
        """获取请求参数"""
        return self.get_row_cell(row, get_request_data())

    def get_except(self, row):
        """获取期望结果"""
        return self.get_row_cell(row, getExcept())

    def get_result(self, row):
        """获取实际结果"""
        return self.get_row_cell(row, getResult())


if __name__ == '__main__':
    opera = OperationExcal()
    print(opera.get_except(1))





