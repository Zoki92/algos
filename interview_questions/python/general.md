## 1. What will be the output of the code below? Explain your answer.

```python
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3
```

How would you modify the definition of extendList to produce the presumably desired behavior?

The output of the above code will be:

list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']

Many will mistakenly expect list1 to be equal to [10] and list3 to be equal to ['a'], thinking that the list argument will be set to its default value of [] each time extendList is called.

However, what actually happens is that the new default list is created only once when the function is defined, and that same list is then used subsequently whenever extendList is invoked without a list argument being specified. This is because expressions in default arguments are calculated when the function is defined, not when it’s called.

list1 and list3 are therefore operating on the same default list, whereas list2 is operating on a separate list that it created (by passing its own empty list as the value for the list parameter).

The definition of the extendList function could be modified as follows, though, to always begin a new list when no list argument is specified, which is more likely to have been the desired behavior:

```python
def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list
```

list1 = [10]
list2 = [123]
list3 = ['a']

## 2. What will be the output of the code below? Explain your answer.

```python
def multipliers():
  return [lambda x : i * x for i in range(4)]

print [m(2) for m in multipliers()]
```

How would you modify the definition of multipliers to produce the presumably desired behavior?

The output of the above code will be [6, 6, 6, 6] (not [0, 2, 4, 6]).

The reason for this is that Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called. So as a result, when any of the functions returned by multipliers() are called, the value of i is looked up in the surrounding scope at that time. By then, regardless of which of the returned functions is called, the for loop has completed and i is left with its final value of 3. Therefore, every returned function multiplies the value it is passed by 3, so since a value of 2 is passed in the above code, they all return a value of 6 (i.e., 3 x 2).

(Incidentally, as pointed out in The Hitchhiker’s Guide to Python, there is a somewhat widespread misconception that this has something to do with lambdas, which is not the case. Functions created with a lambda expression are in no way special and the same behavior is exhibited by functions created using an ordinary def.)

Below are a few examples of ways to circumvent this issue.

One solution would be use a Python generator as follows:

```python
def multipliers():
  for i in range(4): yield lambda x : i * x
```

Another solution is to create a closure that binds immediately to its arguments by using a default argument. For example:

```python
def multipliers():
  return [lambda x, i=i : i * x for i in range(4)]
```

Or alternatively, you can use the functools.partial function:

```python
from functools import partial
from operator import mul

def multipliers():
  return [partial(mul, i) for i in range(4)]
```

Finally, the easiest fix may be to simply replace the return value’s [] with ():

```python
def multipliers():
  return (lambda x : i * x for i in range(4))
```

## 3. What will be the output of the code below? Explain your answer.

```python
class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x


```

The output of the above code will be:

1 1 1
1 2 1
3 2 3

What confuses or surprises many about this is that the last line of output is 3 2 3 rather than 3 2 1. Why does changing the value of Parent.x also change the value of Child2.x, but at the same time not change the value of Child1.x?

The key to the answer is that, in Python, class variables are internally handled as dictionaries. If a variable name is not found in the dictionary of the current class, the class hierarchy (i.e., its parent classes) are searched until the referenced variable name is found (if the referenced variable name is not found in the class itself or anywhere in its hierarchy, an AttributeError occurs).

Therefore, setting x = 1 in the Parent class makes the class variable x (with a value of 1) referenceable in that class and any of its children. That’s why the first print statement outputs 1 1 1.

Subsequently, if any of its child classes overrides that value (for example, when we execute the statement Child1.x = 2), then the value is changed in that child only. That’s why the second print statement outputs 1 2 1.

Finally, if the value is then changed in the Parent (for example, when we execute the statement Parent.x = 3), that change is reflected also by any children that have not yet overridden the value (which in this case would be Child2). That’s why the third print statement outputs 3 2 3.

## 4. What will be the output of the code below in Python 2? Explain your answer.

```python
def div1(x,y):
    print "%s/%s = %s" % (x, y, x/y)

def div2(x,y):
    print "%s//%s = %s" % (x, y, x//y)

div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)
```

Also, how would the answer differ in Python 3 (assuming, of course, that the above print statements were converted to Python 3 syntax)?

In Python 2, the output of the above code will be:

5/2 = 2
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0

By default, Python 2 automatically performs integer arithmetic if both operands are integers. As a result, 5/2 yields 2, while 5./2 yields 2.5.

Also note that the “double-slash” (//) operator will always perform integer division, regardless of the operand types. That’s why 5.0//2.0 yields 2.0 even in Python 2.

Python 3, however, does not have this behavior; i.e., it does not perform integer arithmetic if both operands are integers. Therefore, in Python 3, the output will be as follows:

5/2 = 2.5
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0

## 5. What will be the output of the code below?

list = ['a', 'b', 'c', 'd', 'e']
print list[10:]

The above code will output [], and will not result in an IndexError.

As one would expect, attempting to access a member of a list using an index that exceeds the number of members (e.g., attempting to access list[10] in the list above) results in an IndexError. However, attempting to access a slice of a list at a starting index that exceeds the number of members in the list will not result in an IndexError and will simply return an empty list.

What makes this a particularly nasty gotcha is that it can lead to bugs that are really hard to track down since no error is raised at runtime.

## 6. Consider the following code snippet:

```python
1. list = [ [ ] ] * 5
2. list  # output?
3. list[0].append(10)
4. list  # output?
5. list[1].append(20)
6. list  # output?
7. list.append(30)
8. list  # output?
```

What will be the ouput of lines 2, 4, 6, and 8? Explain your answer.

The output will be as follows:

[[], [], [], [], []]
[[10], [10], [10], [10], [10]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
Here’s why:

The first line of output is presumably intuitive and easy to understand; i.e., list = [ [ ] ] \* 5 simply creates a list of 5 lists.

However, the key thing to understand here is that the statement list = [ [ ] ] \* 5 does NOT create a list containing 5 distinct lists; rather, it creates a a list of 5 references to the same list. With this understanding, we can better understand the rest of the output.

list[0].append(10) appends 10 to the first list. But since all 5 lists refer to the same list, the output is: [[10], [10], [10], [10], [10]].

Similarly, list[1].append(20) appends 20 to the second list. But again, since all 5 lists refer to the same list, the output is now: [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]].

In contrast, list.append(30) is appending an entirely new element to the “outer” list, which therefore yields the output: [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30].

## 7. Given a list of N numbers, use a single list comprehension to produce a new list that only contains those values that are:

(a) even numbers, and
(b) from elements in the original list that had even indices

For example, if list[2] contains a value that is even, that value should be included in the new list, since it is also at an even index (i.e., 2) in the original list. However, if list[3] contains an even number, that number should not be included in the new list since it is at an odd index (i.e., 3) in the original list.

A simple solution to this problem would be as follows

```python
[x for x in list[::2] if x%2 == 0]
```

For example, given the following list:
0 1 2 3 4 5 6 7 8
list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
the list comprehension [x for x in list[::2] if x%2 == 0] will evaluate to:

[10, 18, 78]

The expression works by first taking the numbers that are at the even indices, and then filtering out all the odd numbers.

## 8. Given the following subclass of dictionary:

Will the code below work? Why or why not?

```python
class DefaultDict(dict):
  def __missing__(self, key):
    return []


d = DefaultDict()
d['florp'] = 127
```

Actually, the code shown will work with the standard dictionary object in python 2 or 3—that is normal behavior. Subclassing dict is unnecessary. However, the subclass still won’t work with the code shown because **missing** returns a value but does not change the dict itself:

```python
d = DefaultDict()
print d
{}
print d['foo']
[]
print d
{}

```

So it will “work,” in the sense that it won’t produce any error, but doesn’t do what it seems to be intended to do.

Here is a **missing**-based method that will update the dictionary, as well as return a value:

```python
class DefaultDict(dict):
    def __missing__(self, key):
        newval = []
        self[key] = newval
        return newval

```

## 9. How would you unit-test the following code?

```python
async def logs(cont, name):
    conn = aiohttp.UnixConnector(path="/var/run/docker.sock")
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(f"http://xx/containers/{cont}/logs?follow=1&stdout=1") as resp:
            async for line in resp.content:
                print(name, line)
```

A good answer would suggest a specific async mock library and async test case approach, including an ephemeral event loop that’s guaranteed to terminate (i.e. with a max number of steps before timeout.)

A great answer would point out that synchronisation problems are fundamentally the same in synchronous and asynchronous code, the difference being preemption granularity.

A beautiful answer would take into account that the above code only has one flow (easy) compared to some other code where flows are mixed (e.g. merging two streams into one, sorting, etc). For example, consider following upgrade to the given code:

```python
keep_running = True

async def logs(cont, name):
    conn = aiohttp.UnixConnector(path="/var/run/docker.sock")
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(f"http://xx/containers/{cont}/logs?follow=1&stdout=1") as resp:
            async for line in resp.content:
                if not keep_running:
                    break
                print(name, line)
```

Here, any of the async statements could have a side-effect of changing the global keep_running.

## 10. How do you list the functions in a module?

Use the dir() method to list the functions in a module.

For example:

```python
import some_module
print dir(some_module)
```

## 11. Write a function that prints the least integer that is not present in a given list and cannot be represented by the summation of the sub-elements of the list.

E.g. For a = [1,2,5,7] the least integer not represented by the list or a slice of the list is 4, and if a = [1,2,2,5,7] then the least non-representable integer is 18.

```python
import  itertools
sum_list = []
stuff = [1, 2, 5, 7]
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        sum_list.append(sum(subset))

new_list = list(set(sum_list))
new_list.sort()
for each in range(0,new_list[-1]+2):
    if each not in new_list:
        print(each)
        break
```
