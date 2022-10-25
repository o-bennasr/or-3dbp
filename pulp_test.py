from pulp import LpVariable, LpProblem, LpMinimize, value

def main():
    x = LpVariable("x", 0, 3)

    y = LpVariable("y", 0, 1)

    prob = LpProblem("myProblem", LpMinimize)

    prob += x + y <= 2

    prob += -4*x + y

    status = prob.solve()

    print(f"x= {value(x)}, y = {value(y)}")

if __name__=="__main__":
    main()
