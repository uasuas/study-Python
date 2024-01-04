import tkinter
root = tkinter.Tk()
root.title("配列で色を定義")
cvs = tkinter.Canvas(width = 800, height = 600, bg = "black")
# 配列で色を定義
# rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# iを０〜６まで１ずつ増える
# for i in range(7):
	# X座標を計算して、Xに代入
	# X = i * 120
	# 四角を生成して色を入れていく
	# cvs.create_rectangle(X, 0, X+120, 160, fill=rainbow[i], width=0)

color = [
  ["brown", "red", "orange", "gold"],
  ["darkgreen", "green", "limegreen", "lime"],
  ["navy", "blue", "skyblue", "cyan"]
]

# ３行作成
for y in range(3):
    # ４列作成
    for x in range(4):
        X = x * 200
        Y = y * 200
        # 配列の行「y」列「x」を表す
        cvs.create_oval(X, Y, X+200, Y+200, fill=color[y][x])

cvs.pack()
root.mainloop()