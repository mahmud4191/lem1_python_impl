def main():
	cases=[]

	i = open("test.txt",'r')

	for line in i:
	  line = line.strip()	
	  if (line[0] == "<"):
	    print "============="
	  elif (line[0] == "["):
            print "here"	    
	  else:	
	    x = line.split(' ')
	    cases.append(x)

	n_cases = len(cases)
	n_cols = len(cases[0])
	print("Rows:",n_cases, "Columns:",n_cols)

	for rows in cases:
	  print rows
	
	i.close()

	f = open("test.txt",'r')

	Yvals = []
	for r in range(n_cols):
	  Yvals.append([])	

	for line in f:
	  line = line.strip()	
	  if ((line[0] == "<") or (line[0] == "[")):
	    print "============="
	  else:
	    for index in range(n_cols):
	      Yvals[index].append(line.split(' ')[index])	

	for every_list in Yvals:
	  print every_list

main()
