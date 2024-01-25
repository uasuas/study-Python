import tkinter
root = tkinter.Tk()
root.title("図形を書く")
cvs = tkinter.Canvas(width = 800, height = 500, bg = "white")
# 曲線（表示されない理由不明）
cvs.create_line(0, 0, 100, 160, 200, 20, 300, 60, smooth = True)
# 正方形
cvs.create_rectangle(50, 150, 300, 400, fill = "red", width = 0)
# 楕円（縁の太さ20指定）
cvs.create_oval(400, 50, 700, 200, outline = "blue", width = 20)
# 三角形（アウトラインでライムの指定と幅10指定）
cvs.create_polygon(450, 250, 350, 450, 550, 450, fill = "green", outline = "lime",width = 10)
# 扇形(左から下に45度傾いたところからスタートし、270度の円を描く)
cvs.create_arc(600, 220, 700, 400, start = 45, extent = 270, fill = "orange", outline = "")
cvs.pack()
root.mainloop()