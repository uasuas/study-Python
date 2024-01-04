import tkinter

# 0から始める
n = 0
# 関数を定義count
def count():
  # nをグローバル変数として扱う
  global n
  # カウントを増やしnに代入
  n = n + 1
  # 前回表示した数字を削除
  cvs.delete("all")
  cvs.create_text(200, 100, text=n, font=("System", 80))
  # 次の処理の呼び出しを（1000ミリ秒後, def countを呼び出し）
  root.after(1000, count)

root = tkinter.Tk()
root.title("リアルタイム処理")
cvs = tkinter.Canvas(width=400, height=200)
cvs.pack()
count()
root.mainloop()