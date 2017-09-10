#Basic Quick Find and quick union(eager approach) operation


a=int(raw_input())
li=[0]    #created an array of objects.
li=[0]*a
for i in range(0,a):
	li[i]=i
print li
def is_connect(b,c):
	if(li[b]==li[c]):
		print "%d and %d are connected"%(b,c)
		return 1
		
	else:
		print "%d and %d are not connected"%(b,c)
		return 0

def union(b,c):
	result=is_connect(b,c)
	print result
	if(result==0):
		bid=li[b]
		cid=li[c]
		print bid
		print cid
		print type(cid)
		for i in range(0,a):
			if(li[i]==bid):
				li[i]=cid
				print li[i]					
	print li	
	print "union successfull"
	if(result==1):
		print "union unsuccessfull"
	return 
	
n=1
while(n!=0):
	print "Enter nodes to be joined:"
	b,c=raw_input().split()
	b=int(b)
	#print b
	#print type(b)
	#print c
	c=int(c)
	'''
	if((b>=a) or (c>=a)):
		print "out of index,enter value less than %a"%(a)
		goto label1
	'''
	union(b,c)
	print li
	#is_connect(b,c)
	print "Do you want to do more union operations?(Y/N)"
	value=raw_input()
	if(value=="Y"):
		n=1
	else:
		n=0

