from docx import Document
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

file_list = lib.scanDirFiles(path, "*.docx")
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
            fp = open(i_file, 'rb')
            document = Document(fp)
            fp.close()
            cnt = 0
            for stm in document.paragraphs:
                # print(stm.text)
                cnt = cnt +1
                for ptn in pattern_list:
                    # print(ptn)
                    if ptn in stm.text:
                        pos = "%3s 段落目[%s]" % (str(cnt), ptn)
                        msg = "%-15s \t>> %s ... " % (pos, stm.text[0:20])
                        print(msg)
            print("")
    elif key == 'N':
        loop = False

# ////////////////////////////////////////////

print("<< end program >>")
