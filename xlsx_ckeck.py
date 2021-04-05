import openpyxl
import sys
import lib

# # ////////////////////////////////////////////

print("<< preprocessing >>")

args = sys.argv
if len(args) != 3:
    print(">>arguments error <pattern file> <scan directory path>")
    sys.exit( )

file = args[1]
path = args[2]

# ////////////////////////////////////////////

pattern_list = lib.readFile(file)
if pattern_list is None:
    print(">>readFile() returns None.")
    sys.exit( )
else:
    print("# 検索ワード")
    print(pattern_list)
    print("\n")

file_list = lib.scanDirFiles(path, "*.xlsx")
if file_list is None:
    print(">>scanDirFiles() returns None.")
    sys.exit( )
else:
    print("# 対象ファイル")
    print(file_list)
    print("\n")

loop = True
while loop:
    key = input("start program [Y/N]: ")
    if key == 'Y':
        print("<< start program >>")
        loop = False
        for i_file in file_list:
            print ("# " + i_file)
            book = openpyxl.load_workbook(i_file, data_only=True)
            for sheetname in book.sheetnames:
                print (sheetname + " :")
                wb = book[sheetname]
                row_cnt = 0
                for row in wb.rows:
                    row_cnt = row_cnt + 1
                    for cell in row:
                        if isinstance(cell.value, str):
                            for ptn in pattern_list:
                                if ptn in cell.value.replace('\n', ''):
                                    pos = "%3s 行目[%s]" % (str(row_cnt), ptn)
                                    msg = "%-15s \t>> %s ... " % (pos, cell.value[0:20].replace('\n',''))
                                    print (msg)
            print ("")
            book.close
    elif key == 'N':
        loop = False

# ////////////////////////////////////////////

print("<< end program >>")
