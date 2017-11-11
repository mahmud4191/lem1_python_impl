def main():
	f = file("test.txt")
	#f = file("austr.txt")
	data = []
	for line in f:
	  line = line.strip()
	  if ((line[0] == "<") or (line[0] == "[")):
	    print "ignore"
	  else:
	    row = line.split(' ')
	    row_length = len(row)
	    data = data + row

	print data
	n_cases = len(data)/row_length 
	n_attr = row_length - 1
	print ("No. of cases:", n_cases)
	print ("No. of attributes:", n_attr)

	#rows = []
	#cols = []
	#for index, d in enumerate(data):
	  	   		
	

main()
	
