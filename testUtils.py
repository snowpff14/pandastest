import pandas as pd
import numpy as np
import unittest


# ファイルの比較テスト用
class FileTestBase(unittest.TestCase):

    # CSVファイルの比較用
    def csvFileCompare(self,actualFilePath,expectFilePath):
        actualDataSets = pd.read_csv(actualFilePath,dtype='str',encoding='shift_jisx0213')
        expectDataSets = pd.read_csv(expectFilePath,dtype='str',encoding='shift_jisx0213')

        actualDataArray=np.asarray(actualDataSets)
        expectDataArray=np.asarray(expectDataSets)
        self.bothNumpyArrayEqual(actualDataArray,expectDataArray)

    # エクセルファイルの比較用
    def excelFileCompare(self,actualFilePath,expectFilePath,sheetName):
        actualDataSets = pd.read_excel(actualFilePath,dtype='str',sheet_name=sheetName)
        expectDataSets = pd.read_excel(expectFilePath,dtype='str',sheet_name=sheetName)

        actualDataArray=np.asarray(actualDataSets)
        expectDataArray=np.asarray(expectDataSets)
        self.bothNumpyArrayEqual(actualDataArray,expectDataArray)


    # pandasのDataFrameをnumpyのArrayに変換したものを比較する
    def bothNumpyArrayEqual(self,actualData,expectData):
        for index,expect in enumerate(expectData):
            self.assertEqual(expect.tolist(),actualData[index].tolist())

