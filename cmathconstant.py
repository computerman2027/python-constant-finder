import inspect
import cmath

constants = [name for name, value in inspect.getmembers(cmath) if not inspect.isroutine(value) and not name.startswith('__')]

print(constants)
print(type(constants))