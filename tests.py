from Solver import solve

assert(solve("a", 1) == 1)
assert(solve("aaaaa",3) == 1)
assert(solve("espresso", 5) == 820)
assert(solve("sausage", 5) == 690)
assert(solve("missssppi", 9) == 3780)
assert(solve("mississippi", 11) == 34650)