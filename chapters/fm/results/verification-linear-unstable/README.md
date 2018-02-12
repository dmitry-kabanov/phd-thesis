# Verification of the linear solver in the case of unstable ZND solution

## Description of the experiment

The purpose of the experiment is to demonstrate that the linear solver is
fifth-order accurate.
We use the problem with unstable ZND solution to study the convergence of the
solver.
We run computations on a sequence of grids and compute the observed order of
accuracy.
Solver is verified if the observed order of accuracy is five.

The main artifact of this experiment is the file `convergence-data.tex`---a
table in LaTeX format that summarizes what errors and orders of accuracy were
obtained.

## How to conduct the experiment

1.  Change current working directory to the `./experiment` subdirectory.

2.  To generate simulation results on different grids, run command:

		./run_convergence_study.py run

3.  To compute discretization errors and observed orders of accuracy, run
	command:

		./run_convergence_study.py compute

The output files are written in the subdirectory `./experiment/_output`.

## Reproducibility

The experiment is easily reproducible.
Computations take about 3--4 minutes on a multi-core machine.
