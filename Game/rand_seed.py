import random
# seedで値を設定することで生成されるランダム値が固定される
random.seed(0)
for i in range(20):
  r = random.randint(0, 99)
  # end=","とすることで横並びに,区切りで表示
  print(r, end=",")