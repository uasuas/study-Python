import tkinter

FNT = ("Times New Roman", 60)
COLOR = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# キーを押された時に呼び出す関数設定
def pkey(e):
  # kに押されたキーのシンボルを代入
  k = e.keysym
  # 押されたキーが1~7にある時に対応する処理を設定
  if "1"<=k and k<="7":
    # cに押されたキーを整数にして-1して代入（配列が0スタートのための処理）
    c = int(k)-1
    cvs.delete("all")
    # 背景を押されたキーに応じたCOLORにする
    cvs["bg"] = COLOR[c]
    # テキスト内容をCOLORに定義した文字列にし色を白に設定
    cvs.create_text(300, 150, text=COLOR[c], fill="white", font=FNT)

root = tkinter.Tk()
root.title("1~7キーを押そう")
root.bind("<Key>", pkey)
cvs = tkinter.Canvas(width=600, height=300)
cvs.pack()
root.mainloop()