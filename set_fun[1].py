set={1,2,3,4,5,6}
for t in set:
    print(t)
print( 23 not in set)
print( 4 in set)
set =frozenset(set)
print(set)
set.add(23)#cannot add /edit in frozenset
print(set)