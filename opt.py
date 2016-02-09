import matlab.engine

def fmincon(x0, ub, lb, function, options={}, A=[], b=[], Aeq=[], beq=[],
    providegradients=False):

    # start matlab engine
    eng = matlab.engine.start_matlab()

    # convert arrays to matlab type
    x0 = matlab.double(x0)  # must be list.  if numpy array call .tolist()
    ub = matlab.double(ub)
    lb = matlab.double(lb)
    A = matlab.double(A)
    b = matlab.double(b)
    Aeq = matlab.double(Aeq)
    beq = matlab.double(beq)

    # run fmincon
    [xopt, fopt, exitflag] = eng.optimize(x0, ub, lb, function,
        A, b, Aeq, beq, options, providegradients, nargout=3)

    xopt = xopt[0]  # convert nX1 matrix to array

    # close matlab engine
    eng.quit()

    return xopt, fopt, exitflag
