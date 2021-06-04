# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/03_utils.ipynb (unless otherwise specified).

__all__ = ['is_exact_simulation', 'sym_from_triu', 'statevector_basis', 'hamming_distance']

# Cell
import numpy as np
from qiskit.utils import QuantumInstance

# Cell
def is_exact_simulation(
    quantum_instance: QuantumInstance
) -> bool:
    "Determines whether the quantum instance is to perform a noiseless exact simulation."
    sim = quantum_instance.is_simulator
    noise_qi = len(quantum_instance.noise_config) == 0
    noise_backend = quantum_instance.backend.options.noise_model is None
    return sim and noise_qi and noise_backend

def sym_from_triu(
    x: np.ndarray,
    n: int
) -> np.ndarray:
    "Creates an `n x n` symmetric matrix from the upper triangular data `x`."
    sym = np.zeros((n, n))
    sym[np.triu_indices(n)] = x
    sym += np.triu(sym, 1).T
    return sym

def statevector_basis(
    n: int
) -> np.ndarray:
    "Creates a statevector basis with the binary encodings from 0 to `n`."
    v = np.arange(2**n)
    return (v[:, None] & (1 << np.arange(n)) > 0).astype(int)

def hamming_distance(
    x: np.ndarray,
    y: np.ndarray
) -> np.ndarray:
    "Hamming distance between arrays `x` and `y`."
    return np.count_nonzero(x != y)