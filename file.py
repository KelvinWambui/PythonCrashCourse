#create file

myfile=open('mytext.txt','w')

#get some info

print('name of file',myfile.name)
print('mode of file',myfile.mode)
print('is closed of file',myfile.closed)

# write to the file

myfile.write('i love python programming')
myfile.write('and javascript')
myfile.close()

# read from file

myf=open('mytext.txt','r+')
text=myf.read(60)
print(text)
myf.close()