# Kolmogorov-Smirnov (KS) Distance Metric

The Kolmogorov-Smirnov (KS) distance is a non-parametric measure used to quantify the difference between two cumulative distribution functions (CDFs). It is widely used in hypothesis testing to determine whether a sample follows a theoretical distribution or whether two samples come from the same distribution.

## Definition

For two cumulative distribution functions \( F(x) \) and \( G(x) \), the KS distance \( D \) is defined as:

\[
D = \sup_x \left| F(x) - G(x) \right|
\]

Where:
- \( F(x) \) and \( G(x) \) are the CDFs of the two distributions being compared.
- \( \sup_x \) denotes the supremum (maximum) over all values of \( x \).

If \( G(x) \) represents the empirical CDF of a sample and \( F(x) \) is the theoretical CDF, the KS distance measures the largest vertical difference between the two CDFs.

## Properties

1. **Interpretation**:
   - \( D = 0 \): Perfect agreement between the two distributions.
   - Larger \( D \): Greater dissimilarity between the distributions.
2. **Non-Parametric**: Does not assume any specific distribution for the data.
3. **Sensitivity**: Emphasizes differences across the entire range of the distributions, not just in the tails or center.

## Applications

- **Goodness-of-Fit Tests**: Commonly used in the Kolmogorov-Smirnov test to evaluate whether a sample matches a given distribution.
- **Comparing Distributions**: Determines how similar two empirical distributions are.
- **Statistical Modeling**: Validates assumptions about data distributions in various models.

## Intuition

The KS distance identifies the largest gap between two cumulative distribution curves. This makes it a powerful tool for comparing distributions in a wide variety of scenarios, from validating statistical models to assessing the quality of random number generators.

## Formula for Empirical Data

For a sample of size \( n \) with ordered values \( x_{(1)}, x_{(2)}, \dots, x_{(n)} \) and a theoretical CDF \( F(x) \), the empirical CDF \( F_n(x) \) is:

\[
F_n(x) = \frac{\text{Number of observations } \leq x}{n}
\]

The KS distance is:

\[
D = \max_{1 \leq i \leq n} \left| F_n(x_{(i)}) - F(x_{(i)}) \right|
\]


## References

- [Kolmogorov-Smirnov Test (Wikipedia)](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test)
- Statistical and machine learning libraries implementing the KS test (e.g., SciPy, R, MATLAB).
