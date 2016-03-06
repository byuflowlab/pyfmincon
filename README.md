# pyfmincon
A direct Python bridge to Matlab's fmincon.  No file i/o, sockets, or other hacks.

- opt.py and optimize.m are the required files.
- example.py is a working example.

## Requirements:
- A license for Matlab and its optimization toolbox
- Install the [Matlab Engine for Python](http://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)

## Capabilities:
- can pass any fmincon option
- can provide gradients or not
- can handle an arbitrary number of inequality constraints (equality constraints not yet enabled but could be)
- handles separating objective and constraint calls automatically while not wasting function calls

## Multiple Versions of Python
- If after installing the matlab engine you still have trouble importing ,then you may have multiple versions of Python and it's pulling the wrong library. You may need to set DYLD\_FALLBACK\_LIBRARY\_PATH as described [here](http://www.mathworks.com/matlabcentral/answers/233539-error-importing-matlab-engine-into-python).
- You may also need to set the version of Python you want to use in Matlab with [pyversion](http://www.mathworks.com/help/matlab/ref/pyversion.html).  Alternatively, the script lets you pass this argument in directly (with setpython).