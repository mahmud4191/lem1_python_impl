def main():
	cases=[]

	i = open("test.txt",'r')

	for line in i:
	  line = line.strip()	
	  if (line[0] == "<"):
	    print "============="
	  elif (line[0] == "["):
	    line = line.strip('[')
	    line = line.strip(']')
	    line = line.strip(' ')
	    line = line.strip(' ')
            headings = line.split(' ')	    
	  else:	
	    x = line.split(' ')
	    cases.append(x)
	
	n_cases = len(cases)
	n_cols = len(cases[0])
	print("Rows:",n_cases, "Columns:",n_cols)
	print headings

	atts = []
	for every_case in cases:	
	  att = []
	  for f in range(0, n_cols-1):
	   #print(every_case[f])
	   att.append(every_case[f])

	  atts.append(att)

	#print atts
	
	for every_case in atts:
	  for index, d in enumerate(every_case):
	    every_case[index] = float(every_case[index])
	
	s = atts[0]
	d1 = s[0]
	d2 = s[1]
	print(d1+d2)
	print atts	

	i.close()

	f = open("test.txt",'r')

	Cols = []
	for r in range(n_cols):
	  Cols.append([])	

	for line in f:
	  line = line.strip()	
	  if ((line[0] == "<") or (line[0] == "[")):
	    print "============="
	  else:
	    for index in range(n_cols):
	      Cols[index].append(line.split(' ')[index])	

	#print cases
	#print "======================="	
	#print Cols

	for every_list in Cols[:-1]:
	  for k in range(0, n_cases):
	    every_list[k] = float(every_list[k])
		   
main()
