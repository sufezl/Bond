# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:16:58 2020

@author: Github@FinTechNJU

Design Pattern: Adapter Pattern
"""
import pandas as pd
# ============================================================================== #
from Container import Bondbook
from Function import GetAttrs
from Adapter import GlobalFunctions
# ============================================================================== #
dfRaw, dfRaw2 = pd.DataFrame(), pd.DataFrame()
# 全局变量
# ============================================================================== #
class SetUp:
    @staticmethod
    def set_up(i, K_dict, time_list):
        '''初始化每一个债券
        Args:
            i: 表中位置，后续要改掉
            K_dict: dict, 行权价的时间字典
            time_list: list, 债券开始时间和结束时间列表
        '''
        # 从外部传入数据 TODO 改成函数，不要从文件中读取
        bond_price = dfRaw.iloc[:,i]
        bond_name = pd.DataFrame(dfRaw.iloc[:,i]).columns.tolist()[0]
        stock = dfRaw2.iloc[:,i]
        # 所有可转债
        bond1 = book.bond(bond_name)
        # 实例化一个可转债对象

        bond1.attr('C0').add_value(GetAttrs.get_C0(list1))
        # 设置债券到期价值C0的值

        bond1.attr('r').add_value(GetAttrs.get_r(bond1.attr('C0').value))
        # 设置可转债的收益率，单值数据

        bond1.attr('T').add_value(GetAttrs.get_T(time_list, stock))
        # 设置可转债的到期年限，序列数据

        bond1.attr('sigma').add_value(GetAttrs.get_sgima(stock))
        # 设置可转债的波动率，序列数据

        bond1.attr('K').add_value(GetAttrs.get_K(stock.index.values.tolist(), K_dict))
        # 设置期权的行权价K TODO 序列数据

        bond1.attr('C1').add_value(GetAttrs.get_C1(stock, bond1.attr('r').value, bond1.attr('K').value, bond1.attr('T').value, bond1.attr('sigma').value))
        # 设置期权价值C1 序列数据

        bond1.attr('C2').add_value(GetAttrs.get_C2(bond1.attr('C0').value, bond1.attr('T').value))
        # 设置期纯债价值C2 序列数据

        bond1.attr('Arbitrage').add_value(bond1.attr('C1').value + bond1.attr('C2').value - bond_price)
        # 设置可转债的套利属性

        bond1.attr('Bond_Value').add_value(GetAttrs.get_Bond_Value(bond1.attr('C1').value, bond1.attr('C2').value))
        # 设置可转债的价值

        bond1.attr('Value_Series').add_value(GetAttrs.get_Value_Series(bond1.attr('K').value, stock))
        # 设置可转债的转股价值

        bond1.attr('Premium_Rate').add_value(GetAttrs.get_Premium_Rate(bond_price, bond1.attr('Value_Series').value))
        # 设置可转债的转股溢价率

        bond1.attr('Stock_Price').add_value(stock)# 设置正股股价
        bond1.attr('Bond_Price').add_value(bond_price)# 设置可转债价格

# ============================================================================== #

if __name__=='__main__':
    # 主函数
    if (len(dfRaw)==0) or (len(dfRaw2)==0):
        dfRaw, dfRaw2 = GlobalFunctions.read_data()
    # 获得数据

    book = Bondbook()
    # 设置可转债的基本指标
    # 对于所有可转债

    list1=[0.4, 0.6, 1.0, 1.6, 2.0, 112.5] # 债券1的利息表
    # K1 = 37.97 # 债券1的行权价
    K1_dict = {
        '2019-02-15':37.97,
        '2019-05-31':22.28,
        '2020-05-22':22.22
         }
    # 债券1的行权价
    time_list = ['2019-02-15', '2025-02-15']
    # 债券1的开始时间和结束时间
    list2=[0.4, 0.6, 1.0, 1.6, 2.0, 112.5]
    K2 = 20.22 # 债券2的行权价
    # 对于每一个可转债

    SetUp.set_up(0, K1_dict, time_list)
    GlobalFunctions.show_info(book, 0)
    print("Function: __main__ ... Done!")

