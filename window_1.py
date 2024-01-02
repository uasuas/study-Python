# tkinterモジュールを使う
import tkinter
# オブジェクトの作成
root = tkinter.Tk()
# ウィンドウの高さと幅を指定
# root.geometry("800x400")
# ウィンドウにつけるタイトル
root.title("タイトル")
# キャンパスの高さと幅を指定と背景色の指定
cvs = tkinter.Canvas(width = 600, height = 400, bg = "black")
# キャンパスに、左上を基準とした座標X＝580、Y＝380の、赤の、太さ5の線を引く
cvs.create_line(0, 0, 580, 380, fill = "red", width = 5)
# キャンパスをウィンドウに配置
cvs.pack()
# ウィンドウの処理を実行
root.mainloop()