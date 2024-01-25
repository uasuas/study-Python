import tkinter
root = tkinter.Tk()
root.title("画像表示")
cvs = tkinter.Canvas(width = 1080, height = 720)
# イメージのパスを指定
img = tkinter.PhotoImage(file = "image/chap3_illust.png")
# キャンパスに画像を表示
cvs.create_image(540, 360, image = img)
cvs.pack()
root.mainloop()