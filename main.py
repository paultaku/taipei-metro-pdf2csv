# -*- coding: utf-8 -*-
# pylint: disable=C0103, C0326, C0303, C0111

import pdfquery


# 文件行高
line_height = 50.9
# 乘車日期
date = (152.5, 708.71, 247.5, 718.71)  
# 進站
enter = (389.2, 708.41, 439.3, 718.41)
# 出站
leave = (283.9, 696.41, 439.3, 707.16)
# 收費金額
fee = (283.9, 684.41, 439.3, 700)

pdf = pdfquery.PDFQuery("./example.pdf")

dataModel = []

for index in range(0, 2):


    pdf.load(index)

    for x in range(0,13):
        row =  pdf.extract([
            ('with_formatter', 'text'),
            ('enter', 'LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (enter[0], enter[1] - x*50.9, enter[2], enter[3] - x * 50.9) ),
            ('leave', 'LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (leave[0], leave[1] - x*50.9, leave[2], leave[3] - x * 50.9) ),
            ('date', 'LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (date[0], date[1] - x*50.9, date[2], date[3] - x * 50.9) ),
            ('fee', 'LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (fee[0], fee[1] - x*50.9, fee[2], fee[3] - x * 50.9) )
        ])

        
        
        # 重新整理資料
        dataModel.append({
            "enter": row["enter"],
            "leave": row['leave'].strip().replace(" ", "").split(u"\uff1a")[1],
            "date": row["date"],
            "fee": int(row["fee"].strip().replace(" ", "").split(u"\uff1a")[1]),
        })

csv = open("./output.csv", "w") 

column_title_row = u"日期, 進站, 出站, 手續費\n".encode('big5')
csv.write(column_title_row)

for row in dataModel:
    row_data = u'%(date)s, %(enter)s, %(leave)s, %(fee)s\n' % row
    csv.write(row_data.encode('big5'))

