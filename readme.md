# 使い方
## 導入
* pythonをインストール(3.7で確認)
* 以下のコマンドでライブラリのインストールを行う
```
pip install numpy
pip install pandas
```

## 使い方

1. データを[こちら](https://www.pmda.go.jp/safety/info-services/drugs/adr-info/suspected-adr/0003.html)から取得
1. `data/drug.csv`に医薬品の情報(drugXXXXXX.csvをリネームする)を格納する。
1. `data/reac.csv`に有害事象の情報(reacXXXXXX.csvをリネームする)を格納する。
1. 実行すると`output`下に出力される。
    1. `caseCount.csv` は医薬品、有害事象の組み合わせで症例単位でまとめたもの例数計上用に重複を削除している。
    1. `count.csv` は医薬品、有害事象の組み合わせで症例単位でまとめたもの件数を数えるために重複もそのままにしてある。

## ユニットテスト

1. テスト用のデータは`test`下の同じ構成に配置している。
1. 現在の状態でテスト結果は一致するようにしている変更があった時には結果ファイルを必要に応じて修正を行う


## ソースの説明

* `CreateFileBase`を継承したクラス内で処理を行うことで単体テストの結果比較を容易にしている。
* `FileTestBase`は`unittest.TestCase` を継承しているのでこのクラスで比較処理は行うようにして呼び出し元はあくまでテスト対象の実行、結果の受け渡しのみを行う
* 今回はエクセルの対象は作っていないがcsvと同じ要領でエクセルの比較もできる