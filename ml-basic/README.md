# Machine Learning Fundamentals

A comprehensive guide covering core machine learning concepts, algorithms, and deep learning architectures. This resource is designed for technical interviews and practical ML engineering.

## Contents

- [Core ML Concepts](./ml_fundamentals.md#1-core-concepts)
  - ML Workflow
  - Loss Functions
  - Evaluation Metrics
  - Overfitting & Underfitting
  - Bias-Variance Tradeoff

- [Classic ML Algorithms](./ml_fundamentals.md#2-classic-machine-learning-algorithms)
  - Linear & Logistic Regression
  - Support Vector Machines (SVM)
  - Naive Bayes
  - Decision Trees
  - Random Forest
  - Gradient Boosting (GBDT/XGBoost)
  - K-Means Clustering

- [Deep Learning](./ml_fundamentals.md#3-deep-learning)
  - Deep Neural Networks (DNN)
  - Convolutional Neural Networks (CNN)
  - Recurrent Neural Networks (RNN)
  - Transformers & Attention Mechanism

- [Feature Engineering](./ml_fundamentals.md#feature-engineering)
  - Numerical Features
  - Categorical Features
  - Sequence Data Processing
  - Word2Vec & Embeddings

## Quick Reference

### Common Loss Functions

**Regression:**
- MSE (L2): Smooth, differentiable, penalizes large errors
- MAE (L1): Robust to outliers, not differentiable at zero
- Huber Loss: Combines MSE (small errors) + MAE (large errors)

**Classification:**
- Cross-Entropy: Measures difference between predicted and true probability distributions
- Binary Cross-Entropy: For binary classification
- Focal Loss: Addresses class imbalance

### Evaluation Metrics

**Classification:**
```
Accuracy = (TP + TN) / Total
Precision = TP / (TP + FP)  # Of predicted positives, how many are correct?
Recall = TP / (TP + FN)     # Of actual positives, how many did we find?
F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
```

**Regression:**
- MSE, RMSE, MAE, R², MAPE

### Model Selection Guide

| Task | Recommended Models | Why? |
|------|-------------------|------|
| **Tabular Classification** | XGBoost, LightGBM, Random Forest | Handle mixed features, missing values, interpretable |
| **Tabular Regression** | XGBoost, LightGBM, Ridge/Lasso | Similar benefits as classification |
| **Image Classification** | CNN (ResNet, EfficientNet) | Spatial hierarchies, translation invariance |
| **Sequence Modeling** | Transformer, LSTM, GRU | Long-range dependencies, attention mechanism |
| **Time Series** | ARIMA, LSTM, Temporal Fusion Transformer | Capture temporal patterns |
| **Clustering** | K-Means, DBSCAN, Hierarchical | Depends on cluster shape and density |

## Visual References

The `img/` directory contains key diagrams:

1. `1_mse_mae.png` - MSE vs MAE comparison
2. `2_cross_entropy.png` - Cross-entropy loss visualization
3. `3_emp_struct.png` - Empirical vs structural error
4. `4_model_generalization.png` - Model generalization ability
5. `5_L2_weight_decay.png` - L2 regularization vs weight decay
6. `6_Roc_Auc.png` - ROC-AUC curve
7. `7_decision_tree_explainability.png` - Decision tree interpretability
8. `8_parameter_random.png` - Hyperparameter search methods
9. `9_bayesian_optimization.png` - Bayesian optimization
10. `10_wordbag.png` - Bag of words model
11. `11_word2vec.png` - Word2Vec architecture
12. `12_lda.png` - LDA topic modeling
13. `13_linear_vs_logistic.png` - Linear vs logistic regression
14. `14_decision_tree_pruning.png` - Tree pruning strategies
15. `15_decision_tree_post_pruning.png` - Post-pruning example
16. `16_random_forest.png` - Random forest ensemble
17. `17_random_forest_missing_value.png` - RF missing value handling
18. `18_shap.png` - SHAP value explainability

## Files

- `ml_basics.md` - Original Chinese version (comprehensive, 1600+ lines)
- `ml_fundamentals.md` - **NEW** Refactored English version with improved structure
- `img/` - Visual diagrams and reference images

## Study Approach

### For Interviews

1. **Week 1-2**: Core Concepts (Section 1)
   - Focus on bias-variance tradeoff, overfitting/underfitting
   - Understand all evaluation metrics and when to use each

2. **Week 3-4**: Classic ML (Section 2)
   - Deep dive into decision trees → random forest → GBDT progression
   - Understand SVM kernel trick and when to use different kernels
   - Practice explaining trade-offs between models

3. **Week 5-6**: Deep Learning (Section 3)
   - Understand CNN architecture for images
   - Master RNN/LSTM for sequences
   - Learn Transformer attention mechanism

4. **Week 7**: Integration & Practice
   - Feature engineering techniques
   - End-to-end ML pipeline design
   - Practice explaining concepts out loud

### For Practical Projects

- Start with exploratory data analysis (EDA)
- Choose simple baseline model first (logistic regression, simple tree)
- Iterate with more complex models only if needed
- Focus on feature engineering before complex models
- Always validate with proper train/validation/test splits

## Common Interview Questions

This guide answers these frequently asked questions:

**Fundamentals:**
- What's the difference between supervised and unsupervised learning?
- Explain bias-variance tradeoff
- How do you handle overfitting?
- When would you use L1 vs L2 regularization?

**Algorithms:**
- Explain gradient boosting vs random forest
- How does the kernel trick work in SVM?
- Why does XGBoost perform better than GBDT?
- How do you choose hyperparameters?

**Deep Learning:**
- Explain backpropagation
- What causes vanishing/exploding gradients? How to fix?
- Why use batch normalization?
- Explain attention mechanism in Transformers

**Practical:**
- How do you handle imbalanced datasets?
- How to deal with missing values?
- How to encode categorical features?
- How to evaluate model performance?

## Related Resources

- [LeetCode Solutions](../python/LeetCode_AC_list.md) - Python coding practice
- [Dynamic Programming Guide](../summary_notes/dp_mastery_guide.md) - Algorithm patterns
- [Pandas Cheatsheet](../pandas/pandas_cheatsheet.ipynb) - Data manipulation

---

**Language Note**: Both Chinese (`ml_basics.md`) and English (`ml_fundamentals.md`) versions are available. The English version is restructured for clarity and international accessibility.

**Last Updated**: February 2026
