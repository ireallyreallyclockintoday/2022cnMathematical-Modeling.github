

# Copyright 2022, Gurobi Optimization, LLC

# This example formulates and solves the following simple MIP model:
#  maximize
#        x +   y + 2 z
#  subject to
#        x + 2 y + 3 z <= 4
#        x +   y       >= 1
#        x, y, z INTEGER

import gurobipy as gp
from gurobipy import GRB

try:

    # Create a new model
    m = gp.Model("mip1")

    # Create variables
    x1 = m.addVar(vtype=GRB.INTEGER, name="x1")
    x2 = m.addVar(vtype=GRB.INTEGER, name="x2")
    x3 = m.addVar(vtype=GRB.INTEGER, name="x3")
    x4 = m.addVar(vtype=GRB.INTEGER, name="x4")
    x5 = m.addVar(vtype=GRB.INTEGER, name="x5")
    x6 = m.addVar(vtype=GRB.INTEGER, name="x6")
    x7 = m.addVar(vtype=GRB.INTEGER, name="x7")
    # z = m.addVar(vtype=GRB.INTEGER, name="z")

    # Set objective
    m.setObjective(x1+x2+x3+x4+x5+x6+x7, GRB.MINIMIZE)

    # Add constraint: x + 2 y + 3 z <= 4
    m.addConstr(x1 + 2 * x2 + x7 >=100, "c0")

    # Add constraint: x + y >= 1
    m.addConstr(3*x3 +2*x4+x5+x7 >= 100, "c1")
    m.addConstr(4*x1 +x2+2*x4+4*x5+6*x6+x7 >= 100, "c2")
    # Optimize model
    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % m.ObjVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')
