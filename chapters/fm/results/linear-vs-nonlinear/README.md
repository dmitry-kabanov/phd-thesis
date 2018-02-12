# Comparison of linear and nonlinear solvers

## Description of the experiment

The purpose of the experiment is to verify linear solver.
Verification is done by comparing the results of the simulations by linear and
nonlinear solvers.
When the amplitude of the perturbation of the ZND detonation velocity is small,
both solvers should give approximately the same results.

Experiment consists of:

1.  Execution of linear and nonlinear solvers with the same parameters.

2.  Visual comparison of the detonation-velocity-versus-time graphs for both
    solvers.

## How to conduct the experiment

1.  Change current working directory to the `./experiment` subdirectory.

2.  Run script:

        ./run.py

The results of the linear solver are written in the directory
`./experiment/_output/result-linear`.
The results of the nonlinear solver are written in the directory
`./experiment/_output/result-nonlinear`.

## Reproducibility

The experiment is easily reproducible.
Computations take about 50 seconds on a two-core machine.
