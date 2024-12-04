# Quantum Wasserstein and Total Variation Distance Metrics

In this document, we explore the **Quantum Wasserstein** distance and **Total Variation (TV) Distance** metrics, both of which play important roles in the study of quantum information theory and probability distributions.

---

## Table of Contents

1. [Quantum Wasserstein Distance](#quantum-wasserstein-distance)
   - [Definition](#definition)
   - [Properties](#properties)
   - [Applications](#applications)
   
2. [Total Variation (TV) Distance](#total-variation-tv-distance)
   - [Definition](#definition-1)
   - [Properties](#properties-1)
   - [Applications](#applications-1)

---

## Quantum Wasserstein Distance

The **Quantum Wasserstein Distance (QWD)** is a quantum extension of the classical Wasserstein distance, which measures the distance between probability distributions. In quantum mechanics, we often deal with **quantum states** (density matrices) rather than classical distributions, and the Quantum Wasserstein distance generalizes the classical concept to these quantum systems.

### Definition

The Quantum Wasserstein Distance is defined by the following optimization problem:

$$ W_1(\rho, \sigma) = \inf_{\gamma \in \Gamma(\rho, \sigma)} \mathbb{E}_{(X, Y) \sim \gamma} [\| X - Y \|] $$

where:

- \( \rho \) and \( \sigma \) are quantum states (density matrices).
- \( \Gamma(\rho, \sigma) \) is the set of all couplings of \( \rho \) and \( \sigma \).
- \( \| X - Y \| \) represents the distance between the states \( X \) and \( Y \), usually with respect to a chosen norm (e.g., the Frobenius norm).

This metric generalizes the classical Wasserstein distance, which is based on optimal transport theory, to the quantum setting.

### Properties

- **Metric:** The Quantum Wasserstein Distance is a true metric. It satisfies the properties of non-negativity, symmetry, and the triangle inequality.
- **Monotonicity:** It is monotonically increasing with respect to the trace distance between quantum states.
- **Continuity:** The QWD is continuous with respect to the trace norm topology.

### Applications

The Quantum Wasserstein Distance has applications in:

- **Quantum state comparison:** It provides a way to compare quantum states that are not necessarily identical but might differ slightly due to noise or other imperfections.
- **Quantum machine learning:** It can be used to measure the distance between quantum states in quantum machine learning algorithms.
- **Quantum information theory:** QWD can be used to study quantum transport processes and quantum optimal transport.

---

## Total Variation (TV) Distance

The **Total Variation Distance (TV Distance)** is a classical distance metric between probability distributions. It measures the maximum difference between the probabilities assigned by two distributions across all events.

### Definition

For two probability distributions \( P \) and \( Q \), the Total Variation Distance is defined as:

$$ D_{TV}(P, Q) = \frac{1}{2} \sum_{x} |P(x) - Q(x)| $$

where \( P(x) \) and \( Q(x) \) are the probability mass functions (PMFs) of the distributions \( P \) and \( Q \), respectively. This definition can be extended to continuous distributions as well.

In quantum mechanics, the Total Variation Distance is often used to quantify the difference between quantum states.

### Properties

- **Boundedness:** The TV distance is always between 0 and 1, i.e., \( 0 \leq D_{TV}(P, Q) \leq 1 \).
- **Symmetry:** The distance is symmetric, i.e., \( D_{TV}(P, Q) = D_{TV}(Q, P) \).
- **Triangle inequality:** It satisfies the triangle inequality, i.e., \( D_{TV}(P, R) \leq D_{TV}(P, Q) + D_{TV}(Q, R) \).
- **Geometrical interpretation:** It can be interpreted as the maximum amount of "mass" that needs to be transported to convert one distribution into the other.

### Applications

The Total Variation Distance is widely used in:

- **Classical machine learning:** It's used for comparing probability distributions in various algorithms.
- **Quantum information theory:** It is used to measure the difference between quantum states, especially when comparing quantum states represented as density matrices.
- **Signal processing:** TV distance can be used in signal processing to detect differences between signals or distributions.

---

## Conclusion

Both the **Quantum Wasserstein Distance** and the **Total Variation Distance** are powerful metrics for comparing quantum states and probability distributions. While the Quantum Wasserstein Distance is an extension of the classical Wasserstein distance to quantum settings, the Total Variation Distance remains a fundamental tool for quantifying the differences between classical and quantum distributions.

Both metrics find applications across multiple domains, including quantum machine learning, information theory, and optimal transport theory.

---

## References

1. *Quantum Optimal Transport* by S. Strelchuk, G. M. D'Ariano (2021).
2. *Wasserstein Distance on Quantum States* by P. A. Baldi, M. A. Girolami (2020).
3. *Total Variation Distance* by Wikipedia (https://en.wikipedia.org/wiki/Total_variation_distance).

