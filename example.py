def func(x):

    f = (x[0] - 3)**2 + (x[1] - 2)**2
    c = [10 - x[0]*x[1]]

    gf = [2*(x[0]-3), 2*(x[1]-2)]
    gc = [[-x[1]],  [-x[0]]]

    return f, c, gf, gc


if __name__ == '__main__':

    from opt import fmincon

    function = 'test.func'
    # gradfunction = 'test.grad'

    x0 = [0.0, 0.0]
    ub = [10.0, 10.0]
    lb = [-10.0, -10.0]

    options = {'Algorithm': 'interior-point', 'AlwaysHonorConstraints': 'bounds',
        'display': 'iter-detailed', 'MaxIter': 500, 'MaxFunEvals': 10000,
        'TolCon': 1e-6, 'TolFun': 1e-6, 'FinDiffType': 'forward',
        'Diagnostics': 'on'}
    # algorithms: 'interior-point', 'sqp', 'active-set', 'trust-region-reflective'

    providegradients = True

    xopt, fopt, exitflag = fmincon(x0, ub, lb, function, options,
        providegradients=providegradients)

    print xopt
    print fopt
    print exitflag
