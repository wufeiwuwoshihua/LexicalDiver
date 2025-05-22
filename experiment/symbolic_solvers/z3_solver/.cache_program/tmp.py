from z3 import *

lockers_sort = IntSort()
children_sort, (Fred, Juan, Marc, Paul, Nita, Rachel, Trisha) = EnumSort('children', ['Fred', 'Juan', 'Marc', 'Paul', 'Nita', 'Rachel', 'Trisha'])
lockers = [1, 2, 3, 4, 5]
children = [Fred, Juan, Marc, Paul, Nita, Rachel, Trisha]
boys = [Fred, Juan, Marc, Paul]
girls = [Nita, Rachel, Trisha]
assigned = Function('assigned', children_sort, lockers_sort)

pre_conditions = []
pre_conditions.append(And([Or(Sum([assigned(c) == l for c in children]) == 1, Sum([assigned(c) == l for c in children]) == 2) for l in lockers]))
c = Const('c', children_sort)
pre_conditions.append(ForAll([c], Or([assigned(c) == l for l in lockers])))
b = Const('b', boys_sort)
g = Const('g', girls_sort)
pre_conditions.append(And([Implies(Sum([assigned(c) == l for c in children]) == 2, Exists([b, g], And(assigned(b) == l, assigned(g) == l))) for l in lockers]))
pre_conditions.append(Or([And(assigned(Juan) == l, Sum([assigned(c) == l for c in children]) == 2) for l in lockers]))
pre_conditions.append(And([Not(And(assigned(Rachel) == l, Sum([assigned(c) == l for c in children]) == 2)) for l in lockers]))
pre_conditions.append(Not(Abs(assigned(Nita) - assigned(Trisha)) == 1))
pre_conditions.append(assigned(Fred) == 3)
pre_conditions.append(assigned(Trisha) == 3)
pre_conditions.append(And(assigned(Marc) == 1, Sum([assigned(c) == 1 for c in children]) == 1))
c0 = Const('c0', children_sort)
pre_conditions.append(ForAll([c0], And(1 <= assigned(c0), assigned(c0) <= 5)))
pre_conditions.append(And([Or(Sum([assigned(c) == l for c in children]) == 1, Sum([assigned(c) == l for c in children]) == 2) for l in lockers]))
c = Const('c', children_sort)
pre_conditions.append(ForAll([c], Or([assigned(c) == l for l in lockers])))
b = Const('b', boys_sort)
g = Const('g', girls_sort)
pre_conditions.append(And([Implies(Sum([assigned(c) == l for c in children]) == 2, Exists([b, g], And(assigned(b) == l, assigned(g) == l))) for l in lockers]))
pre_conditions.append(Or([And(assigned(Juan) == l, Sum([assigned(c) == l for c in children]) == 2) for l in lockers]))
pre_conditions.append(And([Not(And(assigned(Rachel) == l, Sum([assigned(c) == l for c in children]) == 2)) for l in lockers]))
pre_conditions.append(Not(Abs(assigned(Nita) - assigned(Trisha)) == 1))
pre_conditions.append(assigned(Fred) == 3)
pre_conditions.append(assigned(Trisha) == 3)
pre_conditions.append(And(assigned(Marc) == 1, Sum([assigned(c) == 1 for c in children]) == 1))

def is_valid(option_constraints):
    solver = Solver()
    solver.add(pre_conditions)
    solver.add(Not(option_constraints))
    return solver.check() == unsat

def is_unsat(option_constraints):
    solver = Solver()
    solver.add(pre_conditions)
    solver.add(option_constraints)
    return solver.check() == unsat

def is_sat(option_constraints):
    solver = Solver()
    solver.add(pre_conditions)
    solver.add(option_constraints)
    return solver.check() == sat

def is_accurate_list(option_constraints):
    return is_valid(Or(option_constraints)) and all([is_sat(c) for c in option_constraints])

def is_exception(x):
    return not x


if is_valid(assigned(Juan) == 4): print('(A)')
if is_valid(assigned(Juan) == 5): print('(B)')
if is_valid(assigned(Paul) == 2): print('(C)')
if is_valid(assigned(Rachel) == 2): print('(D)')
if is_valid(assigned(Rachel) == 5): print('(E)')