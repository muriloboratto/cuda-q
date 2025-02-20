import cudaq
import numpy as np
from typing import List

cudaq.set_target("nvidia")

# Here we input the values of [f(0), f(1)] which allows us to represent constant or balanced functions.
fx = [0, 1]

# Let us now code up the circuit shown above following the state Psi after each step.
qubit_count = 2

@cudaq.kernel
def kernel(fx: List[int]):
    qubit_0 = cudaq.qubit()
    qubit_1 = cudaq.qubit()

    # Psi 0
    x(qubit_1)

    # Psi 1
    h(qubit_0)
    h(qubit_1)

    # Psi 2 - oracle
    if fx[0] == 1:
        x.ctrl(qubit_0, qubit_1)
        x(qubit_1)

    if fx[1] == 1:
        x.ctrl(qubit_0, qubit_1)

    # Psi 3
    h(qubit_0)

    # Measure the qubit to yield if the function is constant or balanced.
    mz(qubit_0)

print(cudaq.draw(kernel, fx))

result = cudaq.sample(kernel, fx, shots_count=1)

if np.array(result)[0] == '0':
    print('The function is constant.')
elif np.array(result)[0] == '1':
    print('The function is balanced.')
