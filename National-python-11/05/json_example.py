import json
x = '{"name": "John", "age": 30, "city": "New York"}'
y = json.loads(x)
# print(type(y))
print(y['name'])
a = {"name": "John", "age": 30, "city": "New York"}
print(type(a))
b = json.dumps(a)
print(type(b))

