def horizontal(l,words,v=0):
	h_l = []
	for i in words:
		length = len(i)
		for j in range(len(l)):
			for k in range(len(l)-length+1):
				n_word = ''.join(l[j][k:k+length])
				if n_word == i:
					if v == 1:
						h_l.append('word found: "{0}" starts at:({1},{2}) ends at:({3},{4})'.format(i,k+1,j+1,k+length,j+1))
					if v == 0:
						h_l.append('word found: "{0}" starts at:({1},{2}) ends at:({3},{4})'.format(i,j+1,k+1,j+1,k+length))
	return h_l

def diagonal(l,words):
	dictt = {}
	d_l = []
	for i in range(len(l)-1,-(len(l)),-1):
		s =''
		for j in range(len(l)):
			for k in range(len(l)):
				if j-k == i:
					s = s+l[j][k]
		dictt[i] = s 
	for word in words:
		for i in list(dictt.keys()):
			if word in dictt[i]:
				start_pos = dictt[i].find(word)
				end_pos = start_pos + len(word) -1
				if i > 0:
					start_let_x = i + start_pos 
					start_let_y = start_let_x - i 
					end_let_x = i + end_pos 
					end_let_y = end_let_x - i
					d_l.append('word found "{0}" in position ({1},{2}) ends at ({3},{4})'.format(word,start_let_x+1,start_let_y+1,end_let_x+1,end_let_y+1))
				if i < 0:
					start_let_y = start_pos - i
					start_let_x = i + start_let_y
					end_let_y = end_pos - i 
					end_let_x = i + end_let_y 
					d_l.append('word found "{0}" in position ({1},{2}) ends at ({3},{4})'.format(word,start_let_x+1,start_let_y+1,end_let_x+1,end_let_y+1))
				if i == 0:
					start_let_x = i + start_pos  
					start_let_y = i + start_let_x 
					end_let_x = i + end_pos 
					end_let_y = i + end_let_x 
					d_l.append('word found "{0}" in position ({1},{2}) ends at ({3},{4})'.format(word,start_let_x+1,start_let_y+1,end_let_x+1,end_let_y+1))
	return d_l
no_of_rows = input('Enter no of row')
l = []
for i in range(int(no_of_rows)):
	line = input().split()
	l.append(line)
words = input("Enter the words separated by space").split()
print("Words in Horizontal:")
print('\n'.join(horizontal(l,words)))
transpose = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
print("Words in Vertical")
print('\n'.join(horizontal(transpose,words,1)))
print('Words in Diagonal')
print('\n'.join(diagonal(l,words)))
