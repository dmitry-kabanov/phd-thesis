# Demonstration of dependence of ZND solutions on activation energy

## Description of the experiment

The purpose of this experiment is to study ZND profiles under varying
activation energy.
The main asset in this experiment is a figure containing several ZND profiles.

Experiment consists of:

1.  Running of linear solver several times with final time equal zero
    and different values of activation energies.

2.  Plot ZND profiles on the same graph to demonstrate how the profiles depend
    on activation energy.

## How to conduct the experiment

1.  Change current working directory to the `./experiment` subdirectory.

2.  Run script:

        ./run.py

Simulation results are written to the `./experiment/_output` subdirectory.

## Reproducibility

The experiment is easily reproducible.
Computations take just several seconds on a multi-core machine.
