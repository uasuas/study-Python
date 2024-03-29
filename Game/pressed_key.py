import tkinter

FNT = ("Times New Roman", 30)
def pkey(e):
  cvs.delete("all")
  # keycodeの値の表示
  cvs.create_text(200, 50, text="コード="+str(e.keycode), font=FNT)
  # keysymの値を表示
  cvs.create_text(200, 150, text="シンボル="+e.keysym, font=FNT)

root = tkinter.Tk()
root.title("キーの値")
root.bind("<Key>", pkey)
cvs = tkinter.Canvas(width=400, height=200)
cvs.pack()
root.mainloop()