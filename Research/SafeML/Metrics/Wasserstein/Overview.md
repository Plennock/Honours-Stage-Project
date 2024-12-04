# Wasserstein Distance Metric

The Wasserstein distance, also known as the Earth Mover’s Distance (EMD), is a measure of the distance between two probability distributions. It is grounded in the theory of optimal transport and is widely used in statistics, machine learning, and data science for comparing distributions.

## Definition

Given two probability distributions \( P \) and \( Q \) with respective cumulative distribution functions (CDFs) \( F(x) \) and \( G(x) \), the Wasserstein distance of order 1 (denoted \( W_1 \)) in one dimension is:

\[
W_1(P, Q) = \int_{-\infty}^\infty \left| F(x) - G(x) \right| dx
\]

For higher-dimensional cases, the Wasserstein distance is defined as the minimum cost of transporting probability mass to transform \( P \) into \( Q \):

\[
W_p(P, Q) = \left( \inf_{\gamma \in \Gamma(P, Q)} \int_{\mathbb{R}^d \times \mathbb{R}^d} \|x - y\|^p d\gamma(x, y) \right)^{1/p}
\]

Where:
- \( p \) is the order of the Wasserstein distance.
- \( \|x - y\| \) is the distance between points \( x \) and \( y \).
- \( \Gamma(P, Q) \) is the set of all joint distributions (transport plans) with marginals \( P \) and \( Q \).

For \( p = 1 \), the distance corresponds to the minimum cost of moving "earth" from one distribution to another.

## Properties

1. **Interpretation**:
   - \( W_p = 0 \): Indicates identical distributions.
   - Larger \( W_p \): Greater dissimilarity between the distributions.
2. **Flexibility**: Can handle continuous, discrete, or empirical distributions.
3. **Order Dependence**: The value of \( p \) determines sensitivity to large differences (e.g., \( W_2 \) emphasizes outliers more than \( W_1 \)).

## Applications

- **Image Processing**: Compares histograms of pixel intensities.
- **Machine Learning**: Evaluates the similarity between generative model outputs (e.g., GANs).
- **Economics**: Analyzes transportation and allocation problems.
- **Statistics**: Measures the dissimilarity between empirical distributions.

## Intuition

The Wasserstein distance considers both the amount of probability mass to be moved and the distance it needs to travel, making it a natural way to quantify differences between distributions.

## Formula for Discrete Distributions

Given two discrete distributions \( P = \{(x_i, p_i)\} \) and \( Q = \{(y_j, q_j)\} \), the Wasserstein distance can be computed as:

\[
W_1(P, Q) = \sum_{i, j} \gamma_{ij} \|x_i - y_j\|
\]

Where \( \gamma_{ij} \) is the optimal transport plan, determined by solving an optimization problem.

## Visualization of Wasserstein Distance

P: | * * * Q: * * * * Transport: Move mass (*) from P to Q with minimal cost.


## References

- [Wasserstein Metric (Wikipedia)](https://en.wikipedia.org/wiki/Wasserstein_metric)
- Statistical libraries with Wasserstein implementations: Python's `scipy.stats.wasserstein_distance`, PyTorch, TensorFlow.
