myArray = [10,9,8,7,6,5,4,3,2,1,0]
def sortArray():
	i = 0
	w = 0
	while(i<len(myArray) and w<len(myArray)):
		if(myArray[i]>myArray[w]):
			x = myArray[i]
			myArray[i] = myArray[w]
			myArray[w] = x
			i = -1
		i = i+1
		w = i+1
	print("Array sorted least to greatest")
	print(myArray)

sortArray()
