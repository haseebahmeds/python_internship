'''a={1,5,7,8,3}
print(a.add(9))
print(a)
print(a.pop(),a)
print(a.discard(2),a)
print(a.remove(9),a)'''





a={2,3,4,5}
b={4,7,8}
'''print(a.union(b),a,b) #return union with a and b sets
print(a|b)   #just provide union
print(a.update(b),a,b)   #doesnt return anything changes 'a' '''

'''print(a.intersection(b),a,b)
print(a&b)
print(a.intersection_update(b),a,b)


print(a.difference(b),a,b)
print(a-b)
print(a.difference_update(b),a,b)'''


'''print(a.symmetric_difference(b),a,b)
print(a^b)
print(a.symmetric_difference_update(b),a,b)'''



'''a={2,3,4,5}
b={4,3}
print(a>=b)
print(a>b)
print(a.issuperset(b))'''




'''a={2,3,4,5}
b={4,3}
print(a<=b)
print(a<b)
print(a.issubset(b))'''


a={2,3,4,5}
b={4,3}
 
print(a.isdisjoint(b))