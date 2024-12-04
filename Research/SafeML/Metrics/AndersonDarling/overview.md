# Anderson-Darling Distance Metric

The Anderson-Darling distance metric is a statistical measure used to quantify how well a sample data distribution matches a specified theoretical distribution. It extends the Kolmogorov-Smirnov test by placing more emphasis on the tails of the distribution, making it particularly sensitive to deviations in the extremes.

## Formula

Given a sample of `n` observations sorted in ascending order, and the cumulative distribution function (CDF) of the theoretical distribution `F`, the Anderson-Darling statistic \(A^2\) is defined as:

\[
A^2 = -n - \frac{1}{n} \sum_{i=1}^n \left[ (2i-1) \left( \ln(F(x_i)) + \ln(1 - F(x_{n+1-i})) \right) \right]
\]

Where:
- \( x_i \) are the ordered sample data points.
- \( F(x) \) is the CDF of the specified theoretical distribution.

The test evaluates the null hypothesis that the sample comes from the specified distribution.

## Properties

1. **Tail Sensitivity**: Emphasizes discrepancies in the tails of the distribution, unlike the Kolmogorov-Smirnov test which treats all parts of the distribution equally.
2. **Goodness-of-Fit**: Commonly used to assess how well data follows normal, exponential, or other distributions.
3. **Critical Values**: Pre-computed critical values depend on the theoretical distribution and sample size, and they are used to determine significance.

## Applications

- **Goodness-of-Fit Testing**: Ensures that data conforms to theoretical models in statistical analysis.
- **Hypothesis Testing**: Evaluates distributional assumptions for further analysis.

## References

- [Wikipedia: Anderson-Darling Test](https://en.wikipedia.org/wiki/Anderson%E2%80%93Darling_test)
- Statistical software documentation for implementation details.
