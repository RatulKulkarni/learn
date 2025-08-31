def f():
    print("Hello")
    def g():
        print("Hello from g")
    return g

abc = f()
gdb = f()

print(abc)
print(gdb)

# Output - 
# Hello
# Hello
# <function f.<locals>.g at 0x000002844A048AE0>
# <function f.<locals>.g at 0x000002844A049940>

'''
Why different addresses?

Because each call to f() defines a new function object for g.
Even though the code of g is the same, Python treats them as separate function objects (freshly created closures). That’s why abc and gdb don’t point to the same memory address.
'''

"""
And also their is a concept of closures as well in Python
"""