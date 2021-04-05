import openpyxl
import glob
import os
import sys

# ////////////////////////////////////////////

def scanDirFiles(dir, ext):
    """
        指定パスのディレクトリに含まれる指定拡張子のファイルをリスト形式で返却する
    """
    if os.path.exists(dir):
        file_list = glob.glob(dir + "*" + ext)
        # while '*$*' in file_list:file_list.remove('*$*')
        for i in range(len(file_list)):
            if '~$' in file_list[i]:
                print(">> del from list:" + file_list[i])
                file_list[i] = ""
        if '' in file_list:
            file_list.remove('')
        return file_list
    else:
        return None

def readFile(file):
    """
        指定のファイルを読み込み、リスト形式で返却する
    """
    if os.path.isfile(file):
        try:
            fp = open(file, 'r')
            matting_list = list()
            for data in fp:
                matting_list.append(data.rstrip('\n'))
            return matting_list
        except Exception as e:
            print("error: {0}".format(e))
            return None
        finally:
            fp.close()
    else:
        return None

# ////////////////////////////////////////////