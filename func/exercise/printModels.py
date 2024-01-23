unprintedDesign = ['phone case', 'robot pendant', 'dodecahedron']
completedModels = []

# while unprintedDesign:
#     currDesign = unprintedDesign.pop()
#     print(f'Printing model: ' , currDesign)
#     completedModels.append(currDesign)

# print("\n The following models have been printed:")
# for md in completedModels:
#     print("printed Model: " , md)



### Viet lai duoi dang func:
def printModels(unprintedDesign, completedModels=[]):
    while unprintedDesign:
        currDesign = unprintedDesign.pop()
        print(f'Printing model: ' , currDesign)
        completedModels.append(currDesign)
    
    return completedModels

def showCompletedModels(models):
    print("\n The following models have been printed:::")
    for model in models:
        print("printed Model: " , model)

copyList = unprintedDesign[:] ## prevent func from modifying unprintedDesign
result = printModels(copyList)
showCompletedModels(result)
