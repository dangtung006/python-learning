# create a dict
mydict = { 'name' : 'Tung dang', 'age' : 31, 'city' : 'hn', 'intro' : 'I am a developer' }
myInfor = dict(name='Tung dang', content="Programing Channel")
print(mydict)
print(myInfor)

### access item in dict:
name = mydict['name']
print(name)
checkName = 'name' in mydict

if checkName == True:
    print("key name exist")
try:
    print(mydict['gender'])
except KeyError as err:
    print("There is an errKey: " , err )

### add and change item (key-value) pairs:
## add new key :
mydict['email'] = 'tungdang@gmail.com'

### change value of key:
mydict['city']  = 'TN'
print(mydict)

### delete a key :
del mydict['intro']
print("Poped value: " + mydict.pop('city'))
mydict.popitem() ### remove the last item of dict
print(mydict)

############### Loop through in dict########
## loop over key:
for key in mydict:
    print("Loop over key : ", key, mydict[key])
## loop over value:
for value in mydict.values():
    print("Loop over value: ", value)
### loop over pairs(key - value)
for key, value in mydict.items():
    print(f'Key: {key} ---- value:{value}')