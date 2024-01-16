# int 関数は与えられた引数を整数型に変換、input 関数はユーザーに対してプログラムへの入力を受け付ける
# input().split()とすることで、文字列を空白で分割しリスト化、map関数を使うことで文字列から整数に変換
A1, A2, A3 = map(int, input().split())
total = A1 + A2 + A3
print(total)