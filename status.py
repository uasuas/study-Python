import tkinter
root = tkinter.Tk()
root.title("ステータスの作成")
cvs = tkinter.Canvas(width = 960, height = 640)
img = tkinter.PhotoImage(file="image/character1.png")
cvs.create_image(480, 320, image=img)
cvs.create_rectangle(540, 60, 900, 580, fill="black", outline="white", width=3)
ability = ["HP", "腕力", "防御力", "知力", "精神力", "素早さ"]
value = ["1200", "800", "320", "1900", "1000", "780"]
for i in range(6):
  # 80pxずつずらして表示していく
  y = 120+80*i
  # （描画する位置、、abilityのテキストを、フォントの種類とサイズ指定）
  cvs.create_text(660, y, text=ability[i], font=("Times New Roman", 20), fill="white")
  # （描画する位置、、valueのテキストを、フォントの種類とサイズ指定）
  cvs.create_text(800, y, text=value[i], font=("Times New Roman", 24), fill="white")

cvs.pack()
root.mainloop()