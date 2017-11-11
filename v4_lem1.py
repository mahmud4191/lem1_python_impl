import sys

filename =  sys.argv[1]

def main():
	cases=[]

	i = open(filename,'r')

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
	    x = line.split()
	    cases.append(x)
	
	#print "Got the cases as list of lists"
	#print cases

	n_cases = len(cases)
	n_cols = len(cases[0])
	print "Got number of rows and columns"
	print("Rows:",n_cases, "Columns:",n_cols)
	print "Got the headings"
	print headings

	atts = []
	for every_case in cases:	
	  att = []
	  for f in range(0, n_cols-1):
	   #print(every_case[f])
	   att.append(every_case[f])

	  atts.append(att)

	#print "Got the attributes as a list of lists"
	#print atts
	
	for every_case in atts:
	  for index, d in enumerate(every_case):
	    if(".." in every_case[index]):	
	      #print "found ranged data"	
	      split_data = every_case[index].split("..")	
	      #range_mid =  (float(split_data[0]) + float(split_data[1]))/2
	      #print split_data
	      every_case[index] = [float(split_data[0]), float(split_data[1])]	
	    else:	
	      every_case[index] = float(every_case[index])
	
	#print "Got the attributes in floats as a list of lists"
	print atts

	s = atts[0]
	d1 = s[0]
	d2 = s[1]
	print("Check float:",(d1+d2))

	i.close()

	f = open(filename,'r')

	Cols = []
	for r in range(n_cols):
	  Cols.append([])	

	for line in f:
	  line = line.strip()	
	  if ((line[0] == "<") or (line[0] == "[")):
	    print "============="
	  else:
	    for index in range(n_cols):
	      Cols[index].append(line.split()[index])	

	#print cases
	#print "======================="	
	#print Cols

	#Converting all attribute columns into float
	for every_list in Cols[:-1]:
	  for k in range(0, n_cases):
	    if(".." in every_list[k]):
	      #print every_list[k]	
	      split_col_data = every_list[k].split("..")	
	      every_list[k] = [float(split_col_data[0]), float(split_col_data[1])]
	    else:    
	      every_list[k] = float(every_list[k])

	print "Got the attribute columns in floats as a list of lists"
	print Cols

	print "Got the decision column"
	decisions = Cols[-1:]
	print decisions
		  
	#Constructing the conceptual variable sets
	list_of_concepts = []
	for d in decisions:
	  for dd in d:
	    if(dd not in list_of_concepts):
		list_of_concepts.append(dd)

	print "Got list of concepts:"
	print list_of_concepts	

	conceptual_vars = []
	for every_concept in list_of_concepts:
	  conceptual_vars.append([])
	  
	for cid, every_concept in enumerate(list_of_concepts):
	  #print every_concept
	  for every_d in decisions:
	    for ind, d in enumerate(every_d):
	      print ind, d, every_concept
	      if(d == every_concept):
		print "matched:",ind, "cid:",cid	
		conceptual_vars[cid].append(ind)
	
	print "Got the concpetual variablse is a list of lists:"
	print conceptual_vars
main()
