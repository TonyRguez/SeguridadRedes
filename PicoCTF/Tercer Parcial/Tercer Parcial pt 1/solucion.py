SQUARE_SIZE = 6
def generate_square(alphabet):
	assert len(alphabet) == pow(SQUARE_SIZE, 2) #can be ignored here
	matrix = []
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0: #i%6==0
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)
	return matrix

def get_index(letter, matrix):
	for row in range(SQUARE_SIZE):
		for col in range(SQUARE_SIZE):
			if matrix[row][col] == letter:
				return (row, col)
	print("letter not found in matrix.")
	exit()

def decrypt_pair(pair, matrix):
	#print("pair=",pair)
	p1 = get_index(pair[0], matrix) #(row,col)
	p2 = get_index(pair[1], matrix) #(row,col)

	if p1[0] == p2[0]: #same row
		return matrix[p1[0]][(p1[1] - 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] - 1)  % SQUARE_SIZE]
	elif p1[1] == p2[1]: #same col
		return matrix[(p1[0] - 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] - 1)  % SQUARE_SIZE][p2[1]]
	else: #neither
		return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]

def decrypt_string(s, matrix):
	result = ""
	for i in range(0, len(s), 2):
		print("now i=",i)
		result += decrypt_pair(s[i:i + 2], matrix)
	return result

alphabet = "lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9"
m = generate_square(alphabet) #key table
enc_msg="1x5hqlod8x7oa88h0de1b5r6xja5sd"
msg=decrypt_string(enc_msg,m)
print(msg)
