def hanoi(num, A, B, C):
	global step
	if num == 1 :
		print("Step:", step + 1, "Move disk number", num, "from", A, "plot to", C, "plot.")
		step = step + 1
	else :
		hanoi(num - 1, A, C, B)
		print("Step:", step + 1, "Move disk number", num, "from", A, "plot to", C, "plot.")
		step = step + 1
		hanoi(num - 1, B, A, C)


global step
print("Input the height of your hanoi tower")
num = input()
step = 0
hanoi(int(num), 'A', 'B', 'C')