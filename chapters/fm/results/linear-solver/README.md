# Linear solver

## Description of the experiment

The purpose of the experiment is to demonstrate two different types of
solutions that can be obtained with linear solver: stable and unstable
solutions.

Experiment consists of:

1.  Execution of the linear solver with two all configuration parameters being
    the same except one: activation energy.

2.  Visual comparison of two graphs of detonation velocity versus time.

## How to conduct the experiment

1.  Change current working directory to the `./experiment` subdirectory.

2.  Run script:

        ./run.py

The results of stable simulation are written to the subdirectory
`./experiment/_output/result-stable`.
The results of stable simulation are written to the subdirectory
`./experiment/_output/result-unstable`.

## Reproducibility

The experiment is easily reproducible.
Computations take about 30 seconds on a two-core machine.
