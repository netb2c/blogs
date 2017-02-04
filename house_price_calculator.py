#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Date:2016-12-30
#Autor:netb2c
#
#
''''
square = float(raw_input('请输入房屋面积：'))
price = float(raw_input('请输入房价：'))
down_payment = 0.2
totle = square * price * down_payment

'''

square = float(raw_input('请输入房屋面积：'))
price = float(raw_input('请输入房价：'))
#rate =
down_payment_rate_input = float(raw_input('请输入首付比例：'))
down_payment_rate = down_payment_rate_input/100
instalment_years = float(raw_input('请输入分期年数：'))
instalment_years_month = instalment_years * 12
#monthly_payment
interest_rate = 0.049
interest_rate_monthly = 0.049/12
totle_price = square * price
down_payment = square * price * down_payment_rate
totle_loan = totle_price - down_payment
monthly_payment = (totle_loan * interest_rate_monthly *(1 + interest_rate_monthly) ** instalment_years_month )/((1 + interest_rate_monthly) ** instalment_years_month -1)
totle_interest = monthly_payment * instalment_years_month - totle_loan

tottle_repayment = totle_loan + totle_interest

residual_repayment = (totle_loan * interest_rate_monthly *(1 + interest_rate_monthly) ** instalment_years_month )/((1 + interest_rate_monthly) ** instalment_years_month -1)

print '房屋面积：',square
print '当前房价：',price
print '计算结果如下：'
print '房屋总价：', totle_price
print '首付金额：',down_payment
print '总贷款金额：',totle_loan
print '贷款总利息：',totle_interest
print '还款总金额：',tottle_repayment
print '月供：',monthly_payment

