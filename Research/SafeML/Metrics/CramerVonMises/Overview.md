# Cramér-von Mises Distance Metric

The Cramér-von Mises distance is a statistical measure used to assess the goodness-of-fit between a sample distribution and a theoretical cumulative distribution function (CDF), or to compare two empirical distributions. It is a widely-used metric in hypothesis testing, particularly for non-parametric tests.

## Definition

For a sample \( x_1, x_2, \dots, x_n \) of size \( n \) drawn from a distribution with CDF \( F(x) \), the Cramér-von Mises statistic \( W^2 \) is defined as:

\[
W^2 = n \int_{-\infty}^{\infty} \left( F_n(x) - F(x) \right)^2 dF(x)
\]

Where:
- \( F_n(x) \) is the empirical CDF of the sample.
- \( F(x) \) is the theoretical CDF being tested against.

In practice, \( W^2 \) is often computed using the ordered sample data points \( x_{(1)}, x_{(2)}, \dots, x_{(n)} \) as:

\[
W^2 = \frac{1}{12n} + \sum_{i=1}^n \left( F(x_{(i)}) - \frac{2i-1}{2n} \right)^2
\]

## Properties

1. **Sensitivity**: The metric considers the entire distribution and is particularly sensitive to differences in the center of the distributions.
2. **Interpretation**: 
   - \( W^2 \approx 0 \): Indicates a good fit between the sample and the theoretical distribution.
   - Larger values of \( W^2 \): Indicate a poorer fit.
3. **Test Statistic**: Used in hypothesis testing to determine if a sample follows a specified theoretical distribution.

## Applications

- **Goodness-of-Fit Tests**: Commonly used in non-parametric statistical tests like the Cramér-von Mises test.
- **Comparing Distributions**: Measures the difference between two empirical distributions or an empirical and a theoretical distribution.
- **Data Validation**: Assesses whether observed data aligns with a specified model.

## Intuition

The Cramér-von Mises distance quantifies the difference between two cumulative distributions by measuring the squared area between their curves. This makes it a robust and comprehensive goodness-of-fit metric.

## References

- [Cramér-von Mises Criterion (Wikipedia)](https://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93von_Mises_criterion)
- Statistical textbooks and software documentation for implementation details.
