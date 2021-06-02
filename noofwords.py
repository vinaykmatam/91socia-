filename = "91social.txt"
fp = open(filename,'r')
read_file = fp.read()
word = read_file.replace(','," ")
result = word.split()
print(len(result))


