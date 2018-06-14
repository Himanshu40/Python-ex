catsname=[]
while True:
    names=input('Enter cat name:- ')
    if names == '':
        break
    catsname = catsname + [names]
print('The cats names are :- ')
for name in catsname:
    print(' '+name)
'howdy' in ['hello','howdy']
size, color, disposition = catsname
size, color = color, size
catsname.index('hello')
catsname.append('moose')
catsname.insert(1, 'chicken')
catsname.remove('moose')
catsname.sort()
catsname.sort(reverse=True)
print(catsname)
print('Four score and seven ' + \
'years ago...')
