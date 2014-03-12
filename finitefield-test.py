from test import test
from finitefield import *
from polynomial import *
from modp import *

def p(L, q):
   f = IntegersModP(q)
   Polynomial = polynomialsOver(f).factory
   return Polynomial(L)

test(True, isIrreducible(p([0,1], 2), 2))
test(False, isIrreducible(p([1,0,1], 2), 2))
test(True, isIrreducible(p([1,0,1], 3), 3))

test(False, isIrreducible(p([1,0,0,1], 5), 5))
test(False, isIrreducible(p([1,0,0,1], 7), 7))
test(False, isIrreducible(p([1,0,0,1], 11), 11))


test(True, isIrreducible(p([-2, 0, 1], 13), 13))
