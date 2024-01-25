import tkinter
import math

x1 = 200
y1 = 200
r1 = 60
x2 = 500
y2 = 300
r2 = 120

def pkey(e):
  global x1, y1
  # 上下左右のキーが押された際の処理を設定（移動）
  if e.keysym=="Up" : y1 -= 10
  if e.keysym=="Down" : y1 += 10
  if e.keysym=="Left" : x1 -= 10
  if e.keysym=="Right" : x1 += 10
  # mathモジュールで使用できるsqrt()にて2点間の距離の計算をする
  d = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
  # 接触時に色を変えるため接触前の色をredに定義
  col = "red"
  # 2点間の距離が半径の合計値以下なら接触と判定し色をピンクに変更
  if d<=r1+r2: col = "pink"
  # （移動）が反映された際の移動前の円を削除する
  cvs.delete("RED_CIRCLE")
  # 座標からx（左右）に60のサイズ、y（上下）に60のサイズの円を書く（色はcolを参照して決まる、移動前の円を削除するためのtagを設置）
  # x1-r1, y1-r1で左上の座標、x1+r1, y1+r1で右下の座標を示す
  cvs.create_oval(x1-r1, y1-r1, x1+r1, y1+r1, fill=col, outline="white", tag="RED_CIRCLE")

root = tkinter.Tk()
root.title("円によるヒットチェック")
root.bind("<Key>", pkey)
cvs = tkinter.Canvas(width=800, height=600, bg="black")
cvs.pack()
cvs.create_oval(x1-r1, y1-r1, x1+r1, y1+r1, fill="red", outline="white", tag="RED_CIRCLE")
cvs.create_oval(x2-r2, y2-r2, x2+r2, y2+r2, fill="blue", outline="white")
root.mainloop()