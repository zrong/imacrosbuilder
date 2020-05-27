#!/usr/bin/env python3

#==========================
# zrong 2020-05-27
#==========================

import csv
from pathlib import Path

HEAD = 'VERSION BUILD=1005 RECORDER=CR\nFRAME F=3\n\n'
TPL = 'TAG POS=1 TYPE={TYPE} FORM=ID:proform ATTR=ID:{TITLE}{NUM} CONTENT={CONTENT}\n'

"""
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:xingming7 CONTENT=name1
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:shenfenzheng7 CONTENT=shenfen1
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:nianling7 CONTENT=34
TAG POS=1 TYPE=SELECT FORM=ID:proform ATTR=ID:xueli7 CONTENT=%本科
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:zhuanye7 CONTENT=zhanye1
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:cszy7 CONTENT=zhanye22
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:zhicheng7 CONTENT=zhicheng1
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:bumen7 CONTENT=bumen1
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:cdgz7 CONTENT=danren1
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:xingming8 CONTENT=name2
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:shenfenzheng8 CONTENT=shenfen2
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:nianling8 CONTENT=33
TAG POS=1 TYPE=SELECT FORM=ID:proform ATTR=ID:xueli8 CONTENT=%本科
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:zhuanye8 CONTENT=zhaunye2
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:cszy8 CONTENT=zhangye2
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:zhicheng8 CONTENT=zhieng2
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:bumen8 CONTENT=bumen2
TAG POS=1 TYPE=INPUT:TEXT FORM=ID:proform ATTR=ID:cdgz8 CONTENT=chengda2
"""

def read_csv(csvname, macroname):
    reader = None
    with open(csvname) as csvfile:
        reader = csv.DictReader(csvfile)
        # reader = csv.reader(csvfile)
        keys = None
        with open(macroname, 'w', encoding='utf8') as macrofile:
            macrofile.write(HEAD)
            for row in reader:
                if keys is None:
                    keys = list(row.keys())
                rowlines = []
                linemap = {'NUM': row['NUM']}
                for key in keys:
                    title = key.split(':')
                    if len(title) != 2:
                        continue
                    linemap['TITLE'] = title[0]
                    if title[1] == 'TEXT':
                        linemap['TYPE'] = 'INPUT:TEXT'
                        linemap['CONTENT'] = row[key]
                    else:
                        linemap['TYPE'] = title[1]
                        linemap['CONTENT'] = '%' + row[key]
                    macrofile.write(TPL.format_map(linemap))
    return reader


if __name__ == '__main__':
    reader = read_csv('Q3.csv', 'Q3.macro')
    reader = read_csv('Q2.csv', 'Q2.macro')
    reader = read_csv('Q1.csv', 'Q1.macro')

