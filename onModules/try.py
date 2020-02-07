# import whole module
import fibo

# import individual function defs
from fibo import fib

fib(200)

x = fibo.fib2(100)
print(x)

fibo.__name__
