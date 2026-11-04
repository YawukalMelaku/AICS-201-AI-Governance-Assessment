# Task 4: Synthetic Fairness and Explainability Assessment

## 1. Objective

This experiment evaluates the predictive performance, group fairness, and
explainability of a synthetic financial eligibility model developed for
the SecureFinance Africa case study.

No real customer information or production banking data was used.

## 2. Dataset and experimental design

- Dataset: data/synthetic_financial_applicants.csv
- Number of records: 1,000
- Demographic groups: Group_A and Group_B
- Training records: 700
- Testing records: 300
- Random state: 42
- Target variable: Actual_Eligible
- Model: Logistic Regression
- Preprocessing: StandardScaler
- Sensitive attribute: Demographic_Group

The demographic group was excluded from the model's training features
but retained for fairness evaluation.

The dataset was generated synthetically. Its distributions and labels
are illustrative assumptions and do not represent real lending outcomes.

## 3. Overall model performance

| Metric | Result |
|---|---:|
| Accuracy | 0.6833 |
| Precision | 0.6926 |
| Recall | 0.8942 |
| F1-score | 0.7806 |

The model achieved relatively high recall but more moderate accuracy and
precision. This indicates that the model identifies many eligible
applicants, while still producing incorrect predictions.

Before any real deployment, the institution would need to assess the
business impact and costs of false-positive and false-negative decisions.

## 4. Group fairness results

| Metric | Group A | Group B |
|---|---:|---:|
| Selection rate | 0.8153 | 0.8112 |
| True-positive rate | 0.8878 | 0.9011 |
| False-positive rate | 0.6949 | 0.6538 |
| Accuracy | 0.6688 | 0.6993 |
| Precision | 0.6797 | 0.7069 |
| Recall | 0.8878 | 0.9011 |
| F1-score | 0.7699 | 0.7923 |

Fairness differences:

- Demographic parity difference: 0.0041
- Equal opportunity difference: 0.0133
- Equalized odds difference: 0.0411

The observed selection rates and true-positive rates are close between
the two synthetic groups. The equalized odds difference is larger,
primarily reflecting the difference in false-positive rates.

These results describe only this experiment. They do not prove that
the model is fair in a real population or that it complies with
applicable law.

## 5. Model explainability

### Logistic regression coefficients

| Feature | Standardized coefficient |
|---|---:|
| Credit_History | 0.5206 |
| Employment_Years | 0.3470 |
| Annual_Income | 0.2967 |
| Debt_To_Income | -0.2466 |
| Age | 0.1209 |

Positive coefficients indicate a positive association with the model's
predicted eligibility; negative coefficients indicate a negative
association, holding the other model features constant.

### Permutation feature importance

| Feature | Mean F1 importance | Standard deviation |
|---|---:|---:|
| Credit_History | 0.041709 | 0.010898 |
| Debt_To_Income | 0.021322 | 0.009777 |
| Annual_Income | 0.021097 | 0.010401 |
| Employment_Years | 0.018053 | 0.013078 |
| Age | 0.007941 | 0.009963 |

Credit history had the largest measured contribution to predictive
performance in the test set. Age had the smallest measured contribution.

Permutation importance measures predictive dependence, not causation.
The standard deviations also indicate variability across repeated
permutations.

## 6. Ethical interpretation

Excluding demographic group from model training does not guarantee
fairness. Other features, such as annual income and employment history,
may act as proxies for structural or socioeconomic differences.

The institution should investigate whether input variables are
necessary, proportionate, accurate, and legally permissible. It should
also assess outcomes across relevant groups and investigate disparities
before and after deployment.

Fairness metrics should be considered together with model accuracy,
data quality, explainability, human oversight, and the consequences
of incorrect decisions.

## 7. Limitations

1. All records and outcomes are synthetic.
2. The test set contains only 300 records.
3. Results depend on the chosen synthetic data generation process,
   model, random seed, and decision threshold.
4. The experiment does not establish causal relationships.
5. The analysis does not establish legal compliance.
6. The results do not demonstrate performance on real applicants,
   other populations, or future data.
7. No production deployment or real-world validation was performed.

## 8. Evidence files

- data/synthetic_financial_applicants.csv
- analysis/generate_synthetic_data.py
- analysis/fairness_analysis.py
- analysis/explainability_analysis.py
- results/fairness_metrics_by_group.csv
- results/fairness_overall_summary.csv
- results/fairness_test_predictions.csv
- results/model_feature_coefficients.csv
- results/permutation_feature_importance.csv
- results/permutation_feature_importance.png

## 9. Recommendation

The model should remain in a controlled research and validation
environment. It should not make autonomous financial eligibility
decisions.

Before any pilot or production deployment, SecureFinance Africa should
conduct representative-data validation, assess fairness across
relevant groups, review proxy variables, establish meaningful human
oversight and appeal mechanisms, and implement ongoing monitoring.
