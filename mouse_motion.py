import tkinter

FNT = ("Times New Room", 40)
# マウスを動かした際に呼び出す関数
def move(e):
  cvs.delete("all")
  # 取得したマウスの座標を文字列として表示する箱の作成
  s = "({}, {})".format(e.x, e.y)
  cvs.create_text(400, 200, text=s, font=FNT)

root = tkinter.Tk()
root.title("マウスポインタの座標")
# bindでイベントを取得、（<マウスポインタを動かした際>、 moveを呼び出す）
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=800, height=400)
cvs.pack()
root.mainloop()