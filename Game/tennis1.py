import tkinter

WIDTH = 960
HEIGHT = 720
ball_x = int(WIDTH/2)
ball_y = int(HEIGHT/5)
bar_x = WIDTH/2
bar_y = HEIGHT-80

def main():
  cvs.create_image(WIDTH/2, HEIGHT/2, image=bg)
  cvs.create_oval(ball_x-10, ball_y-10, ball_x+10, ball_y+10, fill="red")
  cvs.create_rectangle(bar_x-50, bar_y-5, bar_x+50, bar_y+5, fill="blue")

root = tkinter.Tk()
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="image/bg_tennis.png")
main()
root.mainloop()