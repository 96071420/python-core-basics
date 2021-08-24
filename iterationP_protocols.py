from typing import Iterable, Iterator


Iterable = ['spring','summer', 'Autum', 'winter']
Iterator = iter(Iterable)
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))

# next(Iterator)
# Traceback (most recent call last):
# file "<stdin>", line 1, in <module>
