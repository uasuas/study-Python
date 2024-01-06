import tkinter
# 円の初期の位置を指定
mx = 400
my = 300
# 位置を移動するための関数を定義
def move(e):
  global mx, my
  mx = e.x
  my = e.y
# 下記の関数で使用するための、円の初期位置と半径を指定
cx = 400
cy = 300
cr = 50
# 移動条件の関数を定義
def main():
  global cx, cy
  # カーソルの位置から見て、円が上ならcyから1引く（円のY座標を1ピクセル上に移動）
  if cy>my:
    cy -= 1
  # カーソルの位置から見て、円が下ならcyから1足す（円のY座標を1ピクセル下に移動）
  else:
    cy += 1
  # カーソルの位置から見て、円が左ならcxから1引く（円のX座標を1ピクセル上に移動）
  if cx>mx:
    cx -= 1
  # カーソルの位置から見て、円が右ならcxから1足す（円のX座標を1ピクセル下に移動）
  else:
    cx += 1
  # 移動前の円を削除
  cvs.delete("all")
  # 削除後新たに上記のifの結果を反映した円を生成
  cvs.create_oval(cx-cr, cy-cr, cx+cr, cy+cr, fill="blue", outline="cyan")
  # 1ミリ秒後にmainを再度実行
  root.after(1, main)

root = tkinter.Tk()
root.title("ポインタを追いかける円")
# 引数にFalseを指定することで、ウィンドウの幅と高さの両方向でのサイズ変更を無効化
root.resizable(False, False)
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=800, height=600, bg="black")
cvs.pack()
main()
root.mainloop()