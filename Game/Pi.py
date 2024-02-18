import tkinter
import random

root = tkinter.Tk()
cvs = tkinter.Canvas(width=600, height=600, bg="black")
cvs.pack()
# 円周率を代入する変数。
pi = 0
# 円内の点をカウントする為の変数。
c = 0
for i in range(1, 5001):
  x = random.randint(-300, 300)
  y = random.randint(-300, 300)
  col = "red"
  # 点 (x,y) が原点からの距離の2乗が 300の2乗以下であるかどうかを調べ、原点から点 (x,y) までの距離が 300 以下であるかを調べる。
  if x*x+y*y <= 300*300:
    c += 1
    col = "cyan"
  # +300しているのは原点が左上のため、x（右に300）y（下に300）移動させている。
  cvs.create_rectangle(x+300, y+300, x+302, y+302, fill=col, width=0)
  cvs.update()
  pi = 4*c/i
  root.title("円周率 " + str(pi))

root.mainloop()
