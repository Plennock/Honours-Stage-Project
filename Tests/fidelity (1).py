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
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm, logm
import warnings
from qiskit.quantum_info import DensityMatrix

# Fidelity
def fidelity(rho1, rho2, epsilon=1e-12, strict=True):
    try:
        from qiskit.quantum_info import DensityMatrix
        if isinstance(rho1, DensityMatrix):
            rho1 = rho1.data
        if isinstance(rho2, DensityMatrix):
            rho2 = rho2.data
    except ImportError:
        pass

    if rho1.shape != rho2.shape:
        raise ValueError("The two density matrices must have the same shape.")

    trace_rho1 = np.trace(rho1)
    trace_rho2 = np.trace(rho2)

    if not np.isclose(trace_rho1, 1, atol=epsilon) or not np.isclose(trace_rho2, 1, atol=epsilon):
        if strict:
            raise ValueError("Both rho1 and rho2 must have trace approximately equal to 1.")
        else:
            warnings.warn("Density matrices' trace deviates from 1; normalizing.")
            rho1 /= trace_rho1
            rho2 /= trace_rho2

    if np.any(np.linalg.eigvalsh(rho1) < -epsilon) or np.any(np.linalg.eigvalsh(rho2) < -epsilon):
        if strict:
            raise ValueError("Both rho1 and rho2 must be positive semidefinite.")
        else:
            warnings.warn("Density matrices are not strictly positive semidefinite; clipping eigenvalues.")
            rho1 = (rho1 + rho1.T.conj()) / 2
            rho2 = (rho2 + rho2.T.conj()) / 2
            eigenvalues1, eigenvectors1 = np.linalg.eigh(rho1)
            eigenvalues2, eigenvectors2 = np.linalg.eigh(rho2)
            rho1 = eigenvectors1 @ np.diag(np.clip(eigenvalues1, epsilon, None)) @ eigenvectors1.T.conj()
            rho2 = eigenvectors2 @ np.diag(np.clip(eigenvalues2, epsilon, None)) @ eigenvectors2.T.conj()

    sqrt_rho1 = sqrtm(rho1)
    inner_term = sqrtm(sqrt_rho1 @ rho2 @ sqrt_rho1)
    fidelity_value = np.real(np.trace(inner_term)) ** 2

    return fidelity_value

def plot_qnn_fidelity(true_probs, pred_probs, epsilon=1e-12):

    fidelities = []
    discrepancies = np.abs(true_probs - pred_probs)

    for true_p, pred_p in zip(true_probs, pred_probs):
        true_rho = np.array([[true_p, 0], [0, 1 - true_p]])
        pred_rho = np.array([[pred_p, 0], [0, 1 - pred_p]])
        fidelities.append(fidelity(true_rho, pred_rho))

    mean_fidelity = np.mean(fidelities)
    adaptive_threshold = mean_fidelity - 0.5 * (1 - mean_fidelity)
    unsafe_indices = [i for i, f in enumerate(fidelities) if f < adaptive_threshold]

    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(true_probs, fidelities, label="Fidelity", color='green', linewidth=2)
    ax1.scatter([true_probs[i] for i in unsafe_indices], [fidelities[i] for i in unsafe_indices],
                color='red', label=f"Unsafe Predictions (Fidelity < {adaptive_threshold:.2f})", zorder=5)
    ax1.axhline(adaptive_threshold, color='red', linestyle='--', label=f"Unsafe Threshold ({adaptive_threshold:.2f})")
    ax1.set_xlabel("True Probability")
    ax1.set_ylabel("Fidelity", color='green')
    ax1.tick_params(axis='y', labelcolor='green')

    ax2 = ax1.twinx()
    ax2.plot(true_probs, discrepancies, label="Prediction Discrepancy (|True - Pred|)", color='orange', linestyle='--', linewidth=2)
    ax2.set_ylabel("Prediction Discrepancy", color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    plt.title("QNN Safety Monitoring with Fidelity and Discrepancy")
    fig.tight_layout()
    plt.show()
