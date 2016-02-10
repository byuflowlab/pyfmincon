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

## Gotchas:
- As far as I can tell there is no way to pass a function handle from Python to Matlab. To get around this I am passing a string containing the module(package)-name.function-name to the callback function.  This is a little clunky, but it works.