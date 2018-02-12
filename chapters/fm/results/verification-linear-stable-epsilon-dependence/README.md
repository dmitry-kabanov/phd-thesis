# Verification of linear solver for stable ZND solution: study of dependence on WENO epsilon parameter

## Description of the experiment

The purpose of this experiment is to study how character of the solution
changes when we take different values of WENO :math:`\epsilon` parameter.

Experiment consists of:

1.  Execution of the linear solver with all configuration parameters being
	equal exception one: `weno_eps`.

2.  Visual comparison of the graphs of detonation velocity versus time.

## How to conduct the experiment

1.  Change current working directory to the `./experiment` subdirectory.

2.  Run script that runs two simulation with different values of `weno_eps`:

		./run.py

The results of simulations are written to the subdirectory
`./experiment/_output`.

## Reproducibility

The experiment is easily reproducible using instructions from the previous
section.
Computations take about 10 seconds on a multi-core machine.
