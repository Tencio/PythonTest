#A set is like a list but ignoresthe repeated values

Set_Example= {1,2,3,4,4,4}

print(Set_Example)

#Challenge! Create a method where you receive a list with repeated elements and return it back without repeated elements

def clearlist(initial):
    initial=set(initial)
    initial=list(initial)
    initial.sort()
    return initial

print(clearlist(["a", "a", "a", "a", "b", "b", "c", "c", "c", "c", "d", "d", "d", "e", "e"]))

