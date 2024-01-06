import tkinter
# 円の初期の位置を指定
mx = 400
my = 300
# 位置を移動するための関数を定義
def move(e):
  global mx, my
  mx = e.x
  my = e.y

cx = 400
cy = 300
cr = 50
# 移動条件の関数を定義
def main():
  global cx, cy
  # カーソルの位置から見て、円が下ならcyから5引く
  if cy>my:
    cy -= 1
  else:
    cy += 1
  # カーソルの位置から見て、円が下ならcxから5引く
  if cx>mx:
    cx -= 1
  else:
    cx += 1
  # 移動まえの円を削除
  cvs.delete("all")
  # 削除後新たに上記のifの結果を反映した円を生成
  cvs.create_oval(cx-cr, cy-cr, cx+cr, cy+cr, fill="blue", outline="cyan")
  # 1ミリ秒後にmainを再度実行
  root.after(1, main)

root = tkinter.Tk()
root.title("ポインタを追いかける円")
root.resizable(False, False)
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=800, height=600, bg="black")
cvs.pack()
main()
root.mainloop()