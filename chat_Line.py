def read_file(file_name):
	lines = []
	with open(file_name, 'r', encoding = 'utf-8-sig') as f: # -sig為刪除存檔編碼資料之編碼方式
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None # 虛無, 用於不存在的部分
	allen_word_count = 0
	allen_sticker_count = 0
	allen_picture_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_picture_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_picture_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_picture_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen說了', allen_word_count, '個字')
	print('allen貼了', allen_sticker_count, '個貼圖')
	print('allen貼了', allen_picture_count, '張照片')

	print('allen說了', viki_word_count, '個字')
	print('allen貼了', viki_sticker_count, '個貼圖')
	print('allen貼了', viki_picture_count, '張照片')
	

def write_file(file_name, lines):
	with open(file_name, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)


main()