from __future__ import print_function
import numpy as np

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

    # convert to numpy array then list then to matlab type
    # these first conversions are necessary to allow both numpy and list style inputs
    x0 = matlab.double(np.array(x0).tolist())
    ub = matlab.double(np.array(ub).tolist())
    lb = matlab.double(np.array(lb).tolist())
    A = matlab.double(np.array(A).tolist())
    b = matlab.double(np.array(b).tolist())
    Aeq = matlab.double(np.array(Aeq).tolist())
    beq = matlab.double(np.array(beq).tolist())

    # run fmincon
    print('--- calling fmincon ---')
    [xopt, fopt, exitflag, output] = eng.optimize(x0, ub, lb, function,
        A, b, Aeq, beq, options, providegradients, nargout=4)

    xopt = xopt[0]  # convert nX1 matrix to array
    exitflag = int(exitflag)

    # close matlab engine
    eng.quit()

    return xopt, fopt, exitflag, output
