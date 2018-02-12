import numpy as np
import matplotlib.pyplot as plt

from scipy import optimize


def hugoniot(p, v, lamda):
    e = internal_energy(p, v, lamda)
    ea = internal_energy(pa, va, 0)

    return e - ea - 0.5 * (p + pa) * (va - v)


def internal_energy(p, v, lamda):
    return p * v / (gamma - 1) - lamda * Q


def find_p(v, lamda):
    return optimize.newton(hugoniot, 1.0, args=(v, lamda))


def compute_detonation_speed():
    q = Q * (gamma**2 - 1) / 2.0
    ca = np.sqrt(gamma * pa * va)
    dcj = np.sqrt(q) + np.sqrt(ca**2 + q)

    return dcj

pa = 1.0
va = 1.0
rhoa = 1.0 / va

gamma = 1.4
Q = 2.4

v_set = np.linspace(0.3, 1.0, num=100, endpoint=True)
p_set = []

# Find equilibrium Hugoniot.
for v in v_set:
    p = find_p(v, 1.0)
    p_set.append(p)

# Find shock Hugoniot.
v_hugoniot_shock = np.linspace((gamma-1)/(gamma+1), va, num=100, endpoint=True)
p_hugoniot_shock = []
for v in v_set:
    p = find_p(v, 0.0)
    p_hugoniot_shock.append(p)

# Find CJ Rayleigh line.
v_rayleigh_cj = np.array([0.3, va])
p_rayleight_cj = []

dcj = compute_detonation_speed()
d = dcj

for v in v_rayleigh_cj:
    p = pa + rhoa**2 * d**2 * (va - v)
    p_rayleight_cj.append(p)

# Find overdriven Rayleigh line.
v_rayleigh_over = np.array([0.3, va])
p_rayleight_over = []

f = 2.0
d = np.sqrt(f) * dcj

for v in v_rayleigh_over:
    p = pa + rhoa**2 * d**2 * (va - v)
    p_rayleight_over.append(p)

plt.plot(v_set, p_set, '-')
plt.plot(v_hugoniot_shock, p_hugoniot_shock, '--')
plt.plot(v_rayleigh_cj, p_rayleight_cj, '-')
plt.plot(v_rayleigh_over, p_rayleight_over, '-')
plt.xlim((0.0, va+0.2))
plt.show()
