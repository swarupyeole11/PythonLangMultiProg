# Just to show that Python is not block scoped
x = -1
for x in range(7):
      
        print(x, ': for x inside loop')
print(x, ': x in outer')