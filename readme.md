# 画像ファイルのサイズ縮小

カレント配下の以下ファイルについて、
画像サイズを縮小したファイル（ファイル名に_aftが付きます）を作成します。

'*.JPG', '*.jpg', '*.JPEG', '*jpeg'

## オプション

引数に*d*を指定すると元ファイルを削除します。

## 実行例

```
$ ls -l | awk '{print $9 " " $5}'
 
9.JPG 354082
readme.md 0
resize.py 707

$ python3 resize.py d
9.JPG -> 9_aft.JPG
--
Delete original file.
done.

$ ls -l | awk '{print $9 " " $5}'
 
9_aft.JPG 90838
readme.md 0
resize.py 707
```