from collections import namedtuple

Point = namedtuple('Point',['x','y'])
P=Point(1,2)

print(P)
print(P.x)
print(P.y)

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)
