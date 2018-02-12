# Nonlinear solver

## Description of the experiment

The purpose of the experiment is to demonstrate nonlinear dynamics that can be
captured by nonlinear solver. First simulation shows period-1 limit cycle while
second simulation shows period-2 limit cycle.

Experiment consists of:

1.  Execution of the nonlinear solver with two all configuration parameters
    being the same except one: activation energy.

2.  Visual comparison of two graphs of detonation velocity versus time.

## How to conduct the experiment

1.  Change current working directory to the `./experiment` subdirectory.

2.  Run script:

        ./run.sh

The results of stable simulation are written to the subdirectory
`./experiment/_output/q-1.7-theta-2.50`.
The results of stable simulation are written to the subdirectory
`./experiment/_output/q-1.7-theta-2.54`.

## Postprocessing

Postprocessing consists of plotting detonation velocity time series for both
simulations.

## Reproducibility

The experiment is easily reproducible.
Each simulation takes about 4000 seconds.
