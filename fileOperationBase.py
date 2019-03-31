from utils.logger import LoggerObj
from openpyxl.styles.borders import Border, Side

class CreateFileBase():

    # 出力結果を格納するパス
    sourceFilePath=''
    resultFilePath=[]
    # テスト用かどうかの呼び分けを行う mode=1のときテスト用 
    def init(self,mode=0,filePath='data'):
        if mode==0:
            self.sourceFilePath=filePath
        elif mode==1:
            # テスト時はこちら 何か処理を分けるときに使う
            self.sourceFilePath=filePath
        else: 
            log = LoggerObj()
            log.error('mode不正')

    # 出力結果のディレクトリを格納単体テストの時にこのパスを受け取って比較を行う
    def addResultPath(self,filePath):
        self.resultFilePath.append(filePath)
    
    # 出力結果が入っているパスを返す
    def getResultPaths(self):
        return self.resultFilePath

    # 黒い罫線を返すエクセルのセルに黒で罫線を引きたいときに使用する
    def blackBorderLine(self):
        border = Border(top=Side(style='thin', color='000000'), 
                        bottom=Side(style='thin', color='000000'), 
                        left=Side(style='thin', color='000000'),
                        right=Side(style='thin', color='000000')
                        )
        
        return border

    # エクセルに出力するときタイトルも併せて出力を行う
    def createSheetTitle(self,sheet,titles,rowPostion=1):
        for index,title in enumerate(titles):
            sheet.cell(row=rowPostion,column=index+1,value=title)
        return sheet

# メイン処理
if __name__=="__main__":
    print('CreateFileBase')