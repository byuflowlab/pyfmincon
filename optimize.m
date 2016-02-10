function [] = optimize()

    % unpack mat file (can't just dump all into namespace b.c. of nested functions)
    S = load('optimize.mat');
    x0 = S.x0;
    ub = S.ub;
    lb = S.lb;
    options = S.options;
    pyfunction = S.pyfunction;
    A = S.A;
    b = S.b;
    Aeq = S.Aeq;
    beq = S.beq;
    providegradients = S.providegradients;

    % set options
    opt = optimoptions('fmincon');
    names = fieldnames(options);
    for i = 1:length(names)
        opt = optimoptions(opt, names{i}, options.(names{i}));
    end

    % check if gradients provided
    if providegradients
        opt = optimoptions(opt, 'GradObj', 'on', 'GradConstr', 'on');
    end

    % shared variables
    xcheck = 2*ub;
    cin = [];
    gcin = [];

    % run fmincon
    [xopt, fopt, exitflag, optoutput] = fmincon(@obj, x0, A, b, Aeq, beq, lb, ub, @con, opt);


    % ----- conversion functions from numpy to matlab ---------
    function [matrix] = matrixfromnumpy(array)
        data = double(py.array.array('d', py.numpy.nditer(array, pyargs('order', 'F'))));  % Add order='F' to get data in column-major order (as in Fortran 'F' and Matlab)
        data_size = cell2mat(cell(array.shape));
        matrix = reshape(data, data_size);  % No need for transpose, since we're retrieving the data in column major order
    end

    function [vector] = vectorfromnumpy(array)
        vector = double(py.array.array('d', array));
    end


    % ---------- Update objectives and constraints ------------------
    function [J, cin, gJ, gcin] = fupdate(x)
        eval(['output = py.', pyfunction, '(x);'])  % output is a cell array with {J, cin}
        xcheck = x;

        J = output{1};
        cin = vectorfromnumpy(output{2});

        if providegradients
            gJ = vectorfromnumpy(output{3});
            gcin = matrixfromnumpy(output{4});
        else
            gJ = [];
            gcin = [];
        end
    end


    % ---------- Objective Function ------------------
    function [J, gJ] = obj(x)
        [J, cin, gJ, gcin] = fupdate(x);
    end
    % -------------------------------------------------

    % ------------- Constraints ------------------------
    function [c, ceq, gc, geq] = con(x)
        if any(x ~= xcheck)
            [~, cin, ~, gcin] = fupdate(x);
        end
        c = cin;
        ceq = [];
        gc = gcin;
        geq = [];
    end
    % ------------------------

    % save results to file
    save results.mat xopt fopt exitflag optoutput;


end

