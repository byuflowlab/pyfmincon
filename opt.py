from scipy.io import savemat, loadmat
import subprocess


class fmincon(object):

    def __init__(self, pathToMatlab, pathToPython):
        self.matlab = pathToMatlab
        self.python = pathToPython


    def run(self, x0, ub, lb, function, options={}, A=[], b=[], Aeq=[], beq=[],
            providegradients=False):

        # save data into mat file
        mdict = {}
        mdict['x0'] = x0
        mdict['ub'] = ub
        mdict['lb'] = lb
        mdict['options'] = options
        mdict['pyfunction'] = function
        mdict['A'] = A
        mdict['b'] = b
        mdict['Aeq'] = Aeq
        mdict['beq'] = beq
        mdict['providegradients'] = providegradients

        savemat('optimize.mat', mdict)

        # run fmincon
        command = "pyversion " + self.python + "; optimize; quit"
        subprocess.call([self.matlab, "-nosplash", "-nodesktop", "-nojvm", "-r", command])


        # load results from mat file
        results = loadmat('results.mat')
        xopt = results['xopt'][0]
        fopt = results['fopt'][0][0]
        exitflag = int(results['exitflag'][0][0])
        output = results['optoutput'][0][0]

        return xopt, fopt, exitflag, output
