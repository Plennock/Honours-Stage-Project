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

def quantum_relative_entropy(rho1, rho2, epsilon=1e-12, strict=True):
    
    # Convert from DensityMatrix object if necessary
    try:
        from qiskit.quantum_info import DensityMatrix
        if isinstance(rho1, DensityMatrix):
            rho1 = rho1.data
        if isinstance(rho2, DensityMatrix):
            rho2 = rho2.data
    except ImportError:
        pass  # If qiskit not installed, assume inputs are NumPy arrays

    # Ensure density matrices have the same shape
    if rho1.shape != rho2.shape:
        raise ValueError("The two density matrices must have the same shape.")
    
    # Ensure density matrices have trace 1 
    trace_rho1 = np.trace(rho1)
    trace_rho2 = np.trace(rho2)

    if not np.isclose(trace_rho1, 1, atol=epsilon) or not np.isclose(trace_rho2, 1, atol=epsilon):
        if strict:
            raise ValueError("Both rho1 and rho2 must have trace approximately equal to 1.")
        else:
            warnings.warn("Density matrices' trace deviates from 1; normalizing.")
            rho1 /= trace_rho1
            rho2 /= trace_rho2
    
    # Ensure positive semidefiniteness
    if np.any(np.linalg.eigvalsh(rho1) < -epsilon) or np.any(np.linalg.eigvalsh(rho2) < -epsilon):
        if strict:
            raise ValueError("Both rho1 and rho2 must be positive semidefinite.")
        else:
            warnings.warn("Density matrices are not strictly positive semidefinite; clipping eigenvalues.")
            rho1 = (rho1 + rho1.T.conj()) / 2  # Ensure hermitian
            rho2 = (rho2 + rho2.T.conj()) / 2
            eigenvalues1, eigenvectors1 = np.linalg.eigh(rho1)
            eigenvalues2, eigenvectors2 = np.linalg.eigh(rho2)
            rho1 = eigenvectors1 @ np.diag(np.clip(eigenvalues1, epsilon, None)) @ eigenvectors1.T.conj()
            rho2 = eigenvectors2 @ np.diag(np.clip(eigenvalues2, epsilon, None)) @ eigenvectors2.T.conj()

    # find eigenvalues and eigenvectors
    eigenvalues1, eigenvectors1 = np.linalg.eigh(rho1)
    eigenvalues2, eigenvectors2 = np.linalg.eigh(rho2)

    # get log matrices robustly
    log_rho1 = eigenvectors1 @ np.diag(np.where(eigenvalues1 > epsilon, np.log(eigenvalues1), np.log(epsilon))) @ eigenvectors1.T.conj()
    log_rho2 = eigenvectors2 @ np.diag(np.where(eigenvalues2 > epsilon, np.log(eigenvalues2), np.log(epsilon))) @ eigenvectors2.T.conj()

    # Compute quantum relative entropy
    relative_entropy = np.real(np.trace(rho1 @ (log_rho1 - log_rho2)))

    return relative_entropy
def plot_qnn_entropy(true_probs, pred_probs, epsilon=1e-12): 
    relative_entropies = []
    discrepancies = np.abs(true_probs - pred_probs)
    
    for true_p, pred_p in zip(true_probs, pred_probs):
        true_rho = np.array([[true_p, 0], [0, 1 - true_p]])
        pred_rho = np.array([[pred_p, 0], [0, 1 - pred_p]])
        relative_entropies.append(quantum_relative_entropy(true_rho, pred_rho))
    
    mean_entropy = np.mean(relative_entropies)
    adaptive_threshold = 1.5 * mean_entropy
    unsafe_indices = [i for i, re in enumerate(relative_entropies) if re > adaptive_threshold]
    
    plt.figure(figsize=(12, 6))
    plt.plot(true_probs, relative_entropies, label="Quantum Relative Entropy", color='purple', linewidth=2)
    plt.plot(true_probs, discrepancies, label="Prediction Discrepancy (|True - Pred|)", color='orange', linestyle='--', linewidth=2)
    
    plt.scatter([true_probs[i] for i in unsafe_indices], [relative_entropies[i] for i in unsafe_indices], 
                color='red', label=f"Unsafe Predictions (Relative Entropy > {adaptive_threshold:.2f})", zorder=5)
    
    max_entropy_idx = np.argmax(relative_entropies)
    plt.annotate(f"Max Relative Entropy\nTrue Prob = {true_probs[max_entropy_idx]:.2f}",
                 xy=(true_probs[max_entropy_idx], relative_entropies[max_entropy_idx]),
                 xytext=(true_probs[max_entropy_idx] + 0.05, relative_entropies[max_entropy_idx] + 0.05),
                 arrowprops=dict(facecolor='black', arrowstyle="->"), fontsize=10)
    
    plt.xlabel("True Probability")
    plt.ylabel("Metric Value")
    plt.title("QNN Safety Monitoring with Quantum Relative Entropy")
    plt.axhline(adaptive_threshold, color='red', linestyle='--', label=f"Unsafe Threshold ({adaptive_threshold:.2f})")
    plt.legend()
    plt.grid(True)
    plt.show()
