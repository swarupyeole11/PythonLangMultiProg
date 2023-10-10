#Generators offer several benefts ovr other typos of
# ‘sequences, such as lists, tuples, and sets. One of the main |
# benefits of generators s tht they allow you to generate
# the valuos on-the-fly, rather than having to create and
# store the entire sequence in memory. This makes
# generators a powerful tool for working with argo or
# ‘complex data sets, as you can genarate the values as you
# oad thom, rather than having to stro them alin
# memory at once. |
# PE
# means that the values are generated only when they are
# requested. This allows you to generate the values na
# more efficient and mamory-iendly manner, as you don |
# have to generate al the values up front. |

# # # yield in python 
# In Python, you can create a generator by using the yield
# statementin a function. The yield statement returns a.
# Value from the generator and suspends the execution of
# the function until the next value is requested. 

def my_generator():
    for i in range(500):
        #complex computation
        yield i


gen = my_generator()

#Now you can values one by one or you can call values in loop the values in generator are created on the fly 

print(next(gen))
print(next(gen))

for i in gen :
    print(i)