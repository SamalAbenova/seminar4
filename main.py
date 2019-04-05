from mytree import MyTree

def heapsort (t):
	r = []
	while t.length() != 0:
		r.append(t.delete())
	return r[::-1] 

d = MyTree()
with open("words_1.txt","r") as f:
    lines = f.readlines()
    for word in lines:
        d.insert(word[:-1])
        
    a = heapsort(d)
    
for i in a:
	print(a)    





