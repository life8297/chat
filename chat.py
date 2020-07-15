def read_file(file_name):
	lines = []
	with open(file_name, 'r', encoding = 'utf-8-sig') as f: # -sig為刪除存檔編碼資料之編碼方式
		for line in f:
			lines.append(line.strip())
	return(lines)

def convert(lines):
	new = []
	person = None # 虛無, 用於不存在的部分
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return(new)

def write_file(file_name, lines):
	with open(file_name, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()