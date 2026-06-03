#Generator

#yield - for generators' work

def getNums():# Without generator
    return[1,2,3]

print("default nums", getNums())

#With generator
def get_yield_nums():
    yield 1
    yield 2
    yield 3

print("----get_yield_nums----")
for item in get_yield_nums():
    print(item, end="\t")

def counter_yield(n):
    i=0
    while i<=n:
        yield i
        i+=2

print()
for item in counter_yield(7):
    print(item, end='\t')
