# Neutral stability curve

## Description of the experiment

The purpose of this experiment is to plot the neutral stability curve.
Publishable asset of this experiment is a picture with the curve.

Experiment consists of:

1.  Execution many simulations with varying heat :math:`q` and activation
	energy :math:`\theta`.

2.  Traversing the results of these simulations finding those that correspond
	to the growth rate closest to zero.

3.  Plotting those results on a curve as a discrete set of points.


## How to conduct the experiment

For all simulations we vary :math:`q` with :math:`\Delta q = 0.1` in range
from 0.4 to 6.0 and successively refine step :math:`\Delta \theta` for
:math:`\theta` to determine neutral stability.

1.  Prepare configuration files such that for each :math:`q` there are many
	values of :math:`\theta` with rough step :math:`\Delta \theta = 0.1`.

2.  Run the first set of simulations with configuration files prepared
	on stage 1.

3.  For each :math:`q` collect results in which two adjacent values of
	:math:`\theta` give negative and positive growth rates, respectively.

4.  Prepare configuration files such that for each :math:`q` there are many
	values of :math:`\theta` with fine step :math:`\Delta \theta = 0.01` in
	range defined on stage 3.

5.  Run the second set of simulations with configuration files prepared on
	stage 4.

6.  Find the results in which growth rate is close to zero.

## Reproducibility

The experiment is difficult to reproduce.

It requires manual work in preparation of the configuration files, because the
neighborhood of the neutral stability in parametric plane "activation energy-
heat release" is not known in advance.

However, it should be possible to implement an algorithm that implements fully
automatic search of the neutral stability boundary.
