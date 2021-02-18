myArray = [1,4,3,6,5,2,5,1]
def findDuplicates():
	i = 0
	w = 1
	x = ""
	dupl = False
	while(w<len(myArray)):
		if(myArray[w] == myArray[i]):
			dupl = True
			print( "duplicate is " + str(myArray[w]))

		if(w == len(myArray)-1):
			i = i + 1
			w = i
		w = w + 1

		
