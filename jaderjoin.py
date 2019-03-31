from fileOperationBase import CreateFileBase
import os
import time
import openpyxl as excel
import pandas as pd

from datetime import datetime
from openpyxl.styles.borders import Border, Side
from openpyxl.styles.borders import Border, Side
from openpyxl.utils import get_column_letter

class ReadJader(CreateFileBase):


    def mainExecute(self):
        
        reacs=pd.read_csv(filepath_or_buffer=self.sourceFilePath+'/reac.csv',dtype='str',encoding='shift-jisx0213')
        drugs=pd.read_csv(filepath_or_buffer=self.sourceFilePath+'/drug.csv',dtype='str',encoding='shift-jisx0213')

        drugsa=drugs.query('医薬品の関与!="併用薬"')
        drugs2=drugsa.drop_duplicates(subset=['識別番号','報告回数','医薬品（一般名）'])
        reacs2=reacs.drop_duplicates(subset=['識別番号','報告回数','有害事象'])

        # カラムの情報
        columinfo=['識別番号','報告回数','医薬品（一般名）','有害事象']
        columinfoCount=['識別番号','報告回数','医薬品（一般名）','有害事象','転帰']

        reaccase1=pd.merge(drugs2,reacs2,on=['識別番号','報告回数'])
        reaccount1=pd.merge(drugs2,reacs,on=['識別番号','報告回数'])

        reaccase=reaccase1.loc[:,columinfo]
        reaccount=reaccount1.loc[:,columinfoCount]
        caseCountPath='output/caseCount.csv'
        super().addResultPath(caseCountPath)
        reaccase.to_csv(caseCountPath,encoding='shift_jisx0213')

        countPath='output/count.csv'
        super().addResultPath(countPath)
        reaccount.to_csv(countPath,encoding='shift_jisx0213')



# メイン処理
if __name__=="__main__":
        readjader=ReadJader()
        readjader.init()
        readjader.mainExecute()

