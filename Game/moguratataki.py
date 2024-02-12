import tkinter
import random

FNT = ("System", 40)
holes = [0, 0, 0, 0, 0]
scene = "タイトル"
score = 0
time = 0
key = ""
count = 0

# 押されたキーの情報をグローバル変数keyに格納。
def pkey(e):
  global key
  key = e.keysym

def main():
  global scene, score, time, key, count
  cvs.delete("all")
  for i in range(5):
    # i番目の穴のX座標を計算して代入し穴の画像を均等に配置。
    x = 200*i+100
    # tkinter.PhotoImage(file="image/hole.png")がゲームスタート前は[0, 0, 0, 0, 0]で展開する。
    cvs.create_image(x, 160, image=img[holes[i]])
    # 穴の画像に番号をふる。
    cvs.create_text(x, 280, text=i+1, font=FNT, fill="yellow")
    # hitした際に穴の画像に置き換える処理。
    if holes[i] == 2:
      holes[i] = 0
  cvs.create_text(200, 30, text="SCORE "+str(score), font=FNT, fill="white")
  cvs.create_text(800, 30, text="TIME "+str(time), font=FNT, fill="yellow")

  if scene == "タイトル":
    cvs.create_text(500, 100, text="Mogura Tataki Game", font=FNT, fill="pink")
    cvs.create_text(500, 200, text="[S]tart", font=FNT, fill="cyan")
    if key == "s":
      scene = "ゲーム"
      score = 0
      time = 100

  # ゲーム内の処理。
  if scene == "ゲーム":
    # 画像をランダムにtkinter.PhotoImage(file="image/mole.png")に切り替える。
    r = random.randint(0, 4)
    holes[r] = 1
    # プレイヤーが押したキーが文字列として "1" 以上かつ "5" 以下であるかを確認。
    if "1"<=key and key<="5":
      # int() 関数を使ってこの文字列を整数に変換し、1を引くことで、0〜4の範囲のインデックスに変換。
      m = int(key)-1
      # ハンマーの画像を表示する位置決め。
      x = m*200+100
      cvs.create_image(x, 60, image=ham)
      # 押されたキーの位置と配列内の値（モグラが出ている１）が一致しているかを確認。
      if holes[m] == 1:
        # 叩かれた（２）ステータスに変更。
        holes[m] = 2
        score = score + 100
        count += 1
      elif holes[m] == 0:
        score = score - 100
    # 20体ヒットごとにtimeボーナス10を追加。
    if count >= 1 and count % 20 == 0:
      time += 10
      cvs.create_text(500, 30, text="Time +10", font=FNT, fill="blue")
    time = time - 1
    if time == 0:
      scene = "ゲームオーバー"
  
  if scene == "ゲームオーバー":
    cvs.create_text(500, 100, text="GAME END", font=FNT, fill="red")
    cvs.create_text(500, 200, text="[R]eplay", font=FNT, fill="lime")
    if key == "r":
      scene = "ゲーム"
      score = 0
      time = 100

  key = ""
  root.after(330, main)
  
root = tkinter.Tk()
root.title("モグラ叩きゲーム")
root.resizable(False, False)
root.bind("<Key>", pkey)
cvs = tkinter.Canvas(width=1000, height=320)
cvs.pack()
img = [
  tkinter.PhotoImage(file="image/hole.png"),
  tkinter.PhotoImage(file="image/mole.png"),
  tkinter.PhotoImage(file="image/hit.png")
]
ham = tkinter.PhotoImage(file="image/hammer.png")
main()
root.mainloop()