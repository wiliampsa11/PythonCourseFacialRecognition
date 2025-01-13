#Introdución a listas

array=["futebol","pc",18.6,18,[6,7,10.4],True,False]
array.append(66)
array.insert(0,88)
array.extend([1,66, True, 100])



array2 = [200,250,"pc"]

array3 = array+array2
print(array.index("pc"))
print(array3.count("pc"))
array.remove("pc")
array.reverse()
print(array)
array.clear()
print(array)

array4 = [2,5,10,-1,-5, 3]

array4.sort()

print(array4)

array4.sort(reverse=True)
print(array4)
