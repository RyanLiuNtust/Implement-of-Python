#/usr/bin/python
import os, sys, xlwt, xlrd

def getSomeExt(filename):
    if filename.endswith(('.xls')): return True
    else: return False
def copyExcel(filename, iniCol, iniRow):
    workbook = xlrd.open_workbook(filename)
    for iniRow in range(0):
        sheet = workbook.sheet_by_index(iniRow)
        data = [sheet.cell_value(iniRow, iniCol) for iniCol in range(sheet.ncols)]
        print data
        #workExl = xlwt.Workbook()
        #sheet = workbook.add_sheet('addSheet')
        #for index, value in enumerate(data):
        #    sheet.write(iniRow, index, value)
    #workbook.save('./mergy.xls')
def nevigateExl(filename):
    wb = xlrd.open_workbook(filename)
    s = wb.sheet_by_index(0)
    print 'Sheet:',s.name
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print ','.join(str(i) for i in values)
    print 

def mergyExcel(filename,value,rows,cols):
    wb = xlrd.open_workbook(filename)
    wtb = xlwt.Workbook()
    sheet = wtb.add_sheet('new1')
    s = wb.sheet_by_index(0)
    rows.append(s.nrows)
    cols.append(s.ncols)
    print rows
    for row in range(s.nrows):
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
            sheet.write(row,col,s.cell(row,col).value)
    wtb.save('mergy.xls')
def writeExl(value):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('new1')
    sheet.write(0,1,'test text')
    wb.save('test.xls')
def printExl(value,rows,cols):
    for i in range(3):
        for row in range(rows[i]):
            for col in range(cols[i]):
                print values[row*cols[0]+col]
path = "./"
dirs = os.listdir(path)
values = []
cols = []
rows = []
for file in dirs:
    if(getSomeExt(file)): 
        print file
        mergyExcel(file,values,cols,rows)
printExl(values,cols,rows)
print values
       # writeExl(values);
       # nevigateExl(file)
