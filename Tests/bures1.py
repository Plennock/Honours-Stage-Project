import qiskit
from qiskit_aer import Aer
from qiskit.circuit import QuantumCircuit
from qiskit import transpile
from qiskit.quantum_info import Statevector, partial_trace, DensityMatrix
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from qiskit.circuit.library import RealAmplitudes
from scipy.linalg import logm
import numpy as np
import matplotlib.pyplot as plt
import warnings
from scipy.linalg import sqrtm

def bures_distance(rho1, rho2, epsilon=1e-12, strict=True):
    def to_density_matrix(state):
        state = np.asarray(state)
        if state.ndim == 1:
            state = np.outer(state, state.conj())
        elif state.ndim != 2 or state.shape[0] != state.shape[1]:
            raise ValueError("Input must be a state vector (1D) or a square density matrix (2D).")
        return state

    rho1 = to_density_matrix(rho1)
    rho2 = to_density_matrix(rho2)

    # Ensure density matrices have the same shape
    if rho1.shape != rho2.shape:
        raise ValueError("The two density matrices must have the same shape.")

    # Normalize the states
    trace_rho1 = np.trace(rho1)
    trace_rho2 = np.trace(rho2)

    if np.abs(trace_rho1) < epsilon or np.abs(trace_rho2) < epsilon:
        raise ValueError("One or both states have trace zero, which is not valid.")

    rho1 /= trace_rho1
    rho2 /= trace_rho2

    # Ensure positive semidefiniteness
    if np.any(np.linalg.eigvalsh(rho1) < -epsilon) or np.any(np.linalg.eigvalsh(rho2) < -epsilon):
        if strict:
            raise ValueError("Both rho1 and rho2 must be positive semidefinite.")
        else:
            warnings.warn("Density matrices are not strictly positive semidefinite; clipping eigenvalues.")
            rho1 = (rho1 + rho1.T.conj()) / 2  # Hermitian
            rho2 = (rho2 + rho2.T.conj()) / 2
            eigenvalues1, eigenvectors1 = np.linalg.eigh(rho1)
            eigenvalues2, eigenvectors2 = np.linalg.eigh(rho2)
            rho1 = eigenvectors1 @ np.diag(np.clip(eigenvalues1, epsilon, None)) @ eigenvectors1.T.conj()
            rho2 = eigenvectors2 @ np.diag(np.clip(eigenvalues2, epsilon, None)) @ eigenvectors2.T.conj()

    #fidelity
    sqrt_rho1 = sqrtm(rho1) 
    intermediate_matrix = sqrt_rho1 @ rho2 @ sqrt_rho1
    sqrt_intermediate = sqrtm(intermediate_matrix)
    fidelity = (np.trace(sqrt_intermediate))**2

    # Compute Bures distance
    bures_dist = np.sqrt(2 - 2 * np.sqrt(fidelity))

    return bures_dist