from __future__ import print_function

print('--- starting matlab engine ---')
import matlab.engine


def fmincon(x0, ub, lb, function, options={}, A=[], b=[], Aeq=[], beq=[],
        providegradients=False, setpython=None):

    # check if setpython has a path (e.g., /usr/bin/python)
    start_options = '-nodesktop -nojvm'
    if setpython is not None:
        start_options += ' -r pyversion ' + setpython

    # start matlab engine
    eng = matlab.engine.start_matlab(start_options)

    # convert arrays to matlab type
    x0 = matlab.double(x0)  # must be list.  if numpy array call .tolist()
    ub = matlab.double(ub)
    lb = matlab.double(lb)
    A = matlab.double(A)
    b = matlab.double(b)
    Aeq = matlab.double(Aeq)
    beq = matlab.double(beq)

    # run fmincon
    print('--- calling fmincon ---')
    [xopt, fopt, exitflag, output] = eng.optimize(x0, ub, lb, function,
        A, b, Aeq, beq, options, providegradients, nargout=4)

    xopt = xopt[0]  # convert nX1 matrix to array
    exitflag = int(exitflag)

    # close matlab engine
    eng.quit()

    return xopt, fopt, exitflag, output
