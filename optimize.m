function [xopt, fopt, exitflag] = optimize(x0, ub, lb, funcname, ...
    A, b, Aeq, beq, opt_struct, gradients)

    % set options
    options = optimoptions('fmincon');
    names = fieldnames(opt_struct);
    for i = 1:length(names)
        options = optimoptions(options, names{i}, opt_struct.(names{i}));
    end

    % check if gradients provided
    if gradients
        options = optimoptions(options, 'GradObj', 'on', 'GradConstr', 'on');
    end

    % shared variables
    xcheck = 2*ub;
    cin = [];
    gcin = [];

    % run fmincon
    [xopt, fopt, exitflag] = fmincon(@obj, x0, A, b, Aeq, beq, lb, ub, @con, options);


    % ---------- Update objectives and constraints ------------------
    function [J, cin, gJ, gcin] = fupdate(x)
        eval(['output = py.', funcname, '(x);'])  % output is a cell array with {J, cin}
        xcheck = x;
        J = output{1};
        cin = cellfun(@double, cell(output{2}));  % convert from py.list to cell to matlab array

        if gradients
            gJ = cellfun(@double, cell(output{3}));
            gcin = [];
            for row = output{4}  % need to convert list of lists to matrix
                gcin = [gcin; cellfun(@double, cell(row{1}))];
            end
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
            [J, cin, gJ, gcin] = fupdate(x);
        end
        c = cin;
        ceq = [];
        gc = gcin;
        geq = [];
    end
    % ------------------------------------------------


end
