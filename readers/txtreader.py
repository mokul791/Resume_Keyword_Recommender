def get_txt(txt_file_name):
	file = open(txt_file_name, 'r')
	return file.read()


test_file = get_txt('../data_files/sample_feed.txt')

print(test_file)
