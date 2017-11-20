import sys
import numpy

filename =  sys.argv[1]

def check_subset(X, Y):
    for x in X:
      for y in Y:
        flag = False
        if (set(x) <= set(y)):
          flag = True
          break
      if(flag == False):
        break
    return flag

def partition(A_set):
        P = []

        for i, d in enumerate(A_set):
            M = []
            NM = []
            for j in range(0, len(A_set)):
                if(A_set[i] == A_set[j]):
                    M.append(j+1) 
                else:
                    NM.append(j)
            if M not in P:
                P.append(M)

        return P    

def get_subset(set_of_cases, n):
        d_Cases_new = []
        for case in set_of_cases:
            temp = list(case)
            temp.pop(n)
            d_Cases_new.append(temp)

        return d_Cases_new       

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
	      split_data = every_case[index].split("..")	
	      every_case[index] = [float(split_data[0]), float(split_data[1])]	
	    else:	
	      every_case[index] = float(every_case[index])
	
	print "Got the attributes in floats as a list of lists"
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

	d_star = []
	for every_concept in list_of_concepts:
	  d_star.append([])
	  
	for cid, every_concept in enumerate(list_of_concepts):
	  for every_d in decisions:
	    for ind, d in enumerate(every_d):
	      #print ind, d, every_concept
	      if(d == every_concept):
		#print "matched:",ind, "cid:",cid	
		d_star[cid].append(ind+1)
	
	print "Got d_star as a list of lists:"
	print d_star

	#d_star[0] = 
	#d_star[0].append(2)
	#print d_star[0]

	cutpoints = [[]]
	for idx, col in enumerate(Cols[:-1]):
	  for d in range(0,n_cases-1):
	    interval = col[d+1] - col[d]	  
	    #print interval
	    if(interval != 0):
	      cutpoint = (col[d+1] + col[d])/2	
	      cutpoints[idx].append(cutpoint)
	      cutpoints.append([])

	#print cutpoints

	cutpoints = [x for x in cutpoints if x != []]

        #print "Got the cutpoints as a list of lists"

        # Discretize the Cols
        d_Cols = Cols
        for idx, cp in enumerate(cutpoints):
            bins =  cutpoints[idx]
            d_Cols[idx] = numpy.digitize(Cols[idx], bins)

        d_Cases = []
        for k in range(0, n_cases):
          d_Case = []
          for i in range(0,n_cols-1):
            d_Case.append(d_Cols[i][k])
          d_Cases.append(d_Case)  

        print "Got the cols discretized"
        print d_Cols

        print "Got the cases discretized"
        print d_Cases

        A_star = partition(d_Cases)

        print "Got A*"
        print A_star

        Check_Subset = check_subset(A_star, d_star) 
        print "Checking consistency"
        print 'A* <= {d}* = ', Check_Subset


        #print "Creating a global set of decisions"
        global_set_d = []
        for n in range(0, n_cases):
            global_set_d.append(n+1)

        #print global_set_d

        conceptual_vars = [[]]*len(list_of_concepts)
	#Got to work on each conceptual var to create full sets
        for c, concept in enumerate(list_of_concepts):
            conceptual_vars[c] = [d_star[c] , list(set(global_set_d) - set(d_star[c]))]

        print 'Got the conceptual variables:'
        for c in conceptual_vars:
            print c


        #Creating partitions by excluding each attribute one by one    
        #subset_0 = get_subset(d_Cases, 0)
        #p0 = partition(subset_0)
        #cs = check_subset(p0, conceptual_vars[0])
        #print p0,'<', conceptual_vars[0], cs

        #if(cs == True):
        #    subset_1 = get_subset(subset_0, 0)
        #    p1 = partition(subset_1)
        #    cs1 = check_subset(p1, conceptual_vars[0])
        #    print p1, '<', conceptual_vars[0], cs1
        #    if(cs1 == False):
        #        subset_2 = get_subset(subset_0, 1)
        #        p2 = partition(subset_2)
        #        cs2 = check_subset(p2, conceptual_vars[0])
        #        print p2, '<', conceptual_vars[0], cs2

        sub = []
        P = []
        cs = []
        for i in range(0, n_cols-1):
            sub.append([])
            P.append([])
            cs.append([])

        for j in range(0, len(conceptual_vars)):
         print '==============================', list_of_concepts[j]
         pop_n = 0
         for i in range(0, n_cols-1):
            if(i == 0):
                glob = list(d_Cases)
            else:
                glob = list(next_glob)

            sub[i] = get_subset(glob, pop_n)
            print 'Iter',i,'::','Created subset:',sub[i]

            P[i] = partition(sub[i])
            print 'Iter',i,'::','Created partition:',P[i]

            cs[i] = check_subset(P[i], conceptual_vars[j])
            print P[i],'<', conceptual_vars[j],'=', cs[i]

            if(cs[i] == True):
                next_glob = list(sub[i])        
                pop_n = 0

                t_sub = zip(*sub[i])
                glob_cov = []
                idxes = []
                for t in t_sub:
                  for index, c in enumerate(d_Cols[:-1]):
                    if(list(c) == list(t)):
                        #print 'Global covering for',list_of_concepts[j],'=', headings[index]
                        glob_cov.append(headings[index])
                        idxes.append(index)
                        
                print 'Global covering for concept',list_of_concepts[j],'=',glob_cov         
                #print 'Indexes', idxes
                print 'Creating a rule set for concept',list_of_concepts[j]
                #print 'Concept var',conceptual_vars[j][0]

                for v in conceptual_vars[j][0]:
                    #print sub[i][v-1],'->','( Decision,',list_of_concepts[j],')'
                    rule = []
                    for x in range(0, len(sub[i][v-1])):
                        r =  [glob_cov[x], sub[i][v-1][x]]
                        rule.append(r)
                    print list(rule),'->','( Decision,',list_of_concepts[j],')'
            else:
                next_glob = list(glob)
                pop_n = pop_n + 1
            

        #t_sub = zip(*sub[0])

        #for t in t_sub:
        #  for index, c in enumerate(d_Cols[:-1]):
        #      if(list(c) == list(t)):
        #          print 'Global covering for',list_of_concepts[j],'=', headings[index] 


        
main()
