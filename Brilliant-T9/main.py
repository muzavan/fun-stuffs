# Problem : https://brilliant.org/problems/t9-titans/
# @muzavan, 28-03-2017

LIST_FILE = "dictionary.txt"

def get_t9_dict(wordlist):
	t9_dict = {} # number_sequences : list possible word

	for word in wordlist:
		num_seq = ""
		for ch in word:
			num_seq = num_seq + char_to_numpad(ch)

		if(not t9_dict.has_key(num_seq)):
			t9_dict[num_seq] = list()

		t9_dict[num_seq].append(word)

	return t9_dict

def char_to_numpad(character):
	base = 91
	char_ord = ord(character)
	if char_ord < 97 or char_ord >= 123:
		return str(1)
	
	if char_ord > 118 and char_ord < 123:
		return str(9)
	
	if char_ord > 114:
		char_ord = char_ord - 1

	return str((char_ord-base)//3)

def init():	
	with open(LIST_FILE) as listFile:
		wordlist = listFile.readlines()
	return [word.strip() for word in wordlist]

def main():	
	# get all t9 suggestion
	t9_dict = get_t9_dict(init())
	
	max_num_seq = list(sorted(t9_dict, key= lambda k: len(t9_dict[k]), reverse=True))[0]

	print(max_num_seq)
	for word in t9_dict[max_num_seq]:
		print(word)

main()