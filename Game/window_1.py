# tkinterモジュールを使う
import tkinter
# オブジェクトの作成
root = tkinter.Tk()
# ウィンドウの高さと幅を指定
# root.geometry("800x400")
# ウィンドウにつけるタイトル
root.title("タイトル")
# キャンパスの高さと幅を指定と背景色の指定
cvs = tkinter.Canvas(width = 800, height = 600, bg = "white")
# キャンパスに、左上を基準とした座標X＝580、Y＝380の、緑の、太さ5の線を引く
cvs.create_line(0, 0, 580, 380, fill = "green", width = 5)
cvs.create_line(0, 300, 800, 300, fill = "red")
cvs.create_line(400, 0, 400, 600, fill = "blue")
# キャンパスをウィンドウに配置
cvs.pack()
# ウィンドウの処理を実行
root.mainloop()