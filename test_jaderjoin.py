from testUtils import FileTestBase
from jaderjoin import ReadJader
import sys, os
import pandas as pd
import numpy as np
import unittest

class CreateTestSheetTemplateTestSuite(FileTestBase):


    def testJaderCsvCompare001(self):
        readJader=ReadJader()
        # テスト用として実行する
        readJader.init(mode=1,filePath='test/data/001')
        readJader.mainExecute()
        resultFilePaths=readJader.getResultPaths()
        expectFilePath1='test/output/001/caseCount.csv'
        expectFilePath2='test/output/001/count.csv'
        super().csvFileCompare(resultFilePaths[0],expectFilePath1)
        super().csvFileCompare(resultFilePaths[1],expectFilePath2)

 

if __name__ == '__main__':
    unittest.main()