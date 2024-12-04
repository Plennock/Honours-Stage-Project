# Kuiper Distance Metric

The Kuiper distance is a statistical measure used to compare two cumulative distribution functions (CDFs) or to test the goodness-of-fit between a sample distribution and a theoretical distribution. It is closely related to the Kolmogorov-Smirnov (KS) distance but is particularly sensitive to differences in the tails of the distributions.

## Definition

For two cumulative distribution functions \( F(x) \) and \( G(x) \), the Kuiper distance \( V \) is defined as:

\[
V = \sup_x \left( F(x) - G(x) \right) + \sup_x \left( G(x) - F(x) \right)
\]

Where:
- \( \sup_x \) denotes the supremum (maximum) over all values of \( x \).
- \( F(x) \) and \( G(x) \) can represent empirical or theoretical CDFs.

The Kuiper distance is the sum of the largest positive and negative deviations between the two CDFs.

## Properties

1. **Symmetry**: Unlike the Kolmogorov-Smirnov distance, the Kuiper distance is symmetric in how it treats positive and negative deviations.
2. **Sensitivity to Tails**: It gives equal weight to differences in the tails and the center of the distributions.
3. **Goodness-of-Fit**: Like the KS distance, it is used in hypothesis tests to determine whether two distributions differ significantly.

## Applications

- **Goodness-of-Fit Testing**: Evaluates how well a sample matches a theoretical distribution.
- **Comparing Distributions**: Assesses the similarity of two empirical distributions, especially when tail differences are important.
- **Astronomy and Physics**: Frequently used in fields where data may have significant tail behavior.

## Intuition

The Kuiper distance measures the extent to which two cumulative distribution functions deviate from each other. Unlike the KS distance, it takes into account both the largest upward and downward deviations, making it more sensitive to tail differences.

## Formula for Empirical Data

For a sample of size \( n \) with ordered values \( x_{(1)}, x_{(2)}, \dots, x_{(n)} \) and a theoretical CDF \( F(x) \), the empirical CDF \( F_n(x) \) is:

\[
F_n(x) = \frac{\text{Number of observations } \leq x}{n}
\]

The Kuiper distance is computed as:

\[
V = \max_{1 \leq i \leq n} \left( F_n(x_{(i)}) - F(x_{(i)}) \right) + \max_{1 \leq i \leq n} \left( F(x_{(i)}) - F_n(x_{(i)}) \right)
\]


## References

- [Kuiper's Test (Wikipedia)](https://en.wikipedia.org/wiki/Kuiper%27s_test)
- Statistical libraries for implementation, e.g., Python's SciPy, R, and MATLAB.

