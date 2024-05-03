albuns_list = ("a1", "a2","a3")
albuns_set = set(albuns_list)
list = ['rap','house','electronic music', 'rap']
list_set = set(list)
print(list_set)

set3 =albuns_set.union(list_set)
print(set3)
set3.issubset(list_set)