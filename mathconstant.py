import inspect
import math

constants = [name for name, value in inspect.getmembers(math) if not inspect.isroutine(value) and not name.startswith('__')]

print(constants)