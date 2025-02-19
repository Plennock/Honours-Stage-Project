import numpy as np
import qiskit
from qiskit_aer import Aer
from qiskit.circuit import QuantumCircuit
from qiskit import transpile
from qiskit.quantum_info import DensityMatrix
from qiskit.quantum_info import DensityMatrix

def trace_distance(rho, sigma):
    # Convert Qiskit DensityMatrix to numpy array if needed
    rho_matrix = rho.data if isinstance(rho, DensityMatrix) else np.array(rho)
    sigma_matrix = sigma.data if isinstance(sigma, DensityMatrix) else np.array(sigma)

    # Compute the difference matrix
    delta = rho_matrix - sigma_matrix

    # Find the eigenvalues of delta
    eigenvalues = np.linalg.eigvals(delta)

    # Calculate the trace distance
    trace_dist = np.sum(np.abs(eigenvalues)) / 2

    return trace_dist