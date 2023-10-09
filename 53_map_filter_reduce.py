import functools 

dicty = { '3person' : [1,{'name':'ramesh'}] , '2person' : [2,{'name':'suresh'}] , '1person' : [3,{'name':'labhesh'}]}

lista = [1,2,3,4,5]

new_list_map = list(map(lambda x : x*x , lista))
new_list_filter  = list(filter(lambda x : x%2==0 , lista))
new_list_reduce = int(functools.reduce(lambda x, y : x+y, lista))

print(new_list_reduce)
