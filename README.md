# pyfmincon
A Python bridge to Matlab's fmincon (requires a Matlab license).

## Requirements:
- A license for Matlab and its optimization toolbox
- Install the [Matlab Engine for Python](http://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)

## Capabilities:
- fmincon only (none of the other optimizers)
- can pass any fmincon option
- can provide gradients or not
- can handle an arbitrary number of constraints
- handles separating objective and constraint calls while not wasting function calls

## Gotchas:
- As far as I can tell there is no way to pass a function handle from Python to Matlab. To get around this I am passing a string containing the module(package)-name.function-name to the callback function.  This is a little clunky.
- The module that contains the callback functions cannot contain any import statements in the global scope for some reason. I can see this being an issue. Probably there is some way to work around it, but I've not thought of a good solution yet.
- Matlab doesn't accept numpy arrays, so you have to either construct the matlab array in python using the matlab.engine package or pass a lists or lists of lists. I use the former where I can (e.g., in opt.py), and the latter when I'm forced to (in test.py) because of the limitation in the previous bullet.
- These are actually minor issues compared to the hoops I've jumped through in past python-fmincon bridge attempts. Hopefully function callbacks and numpy array support will be added in future versions of matlab.

