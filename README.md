# Random Forest
Before going deep into Random Forest lets look at some important topics

## Bias and Variance

**Bias** is the error that measures how far a model’s predictions are from the true values.

- Bias is high -> the model is too simple and fails to capture the underlying patterns in the data. This usually leads to underfitting.
- Bias is low -> the model is able to represent the data more accurately.

**Variance**  refers to how sensitive a model is to changes in the training dataset.

- When variance is high, the model is too complex and tries to fit every data point in the training set.
- As a result, even small changes in the training data can cause large changes in the model’s predictions. This typically leads to overfitting.

## Underfitting and Overfitting

**Underfitting** occurs when a model is too simple to capture the underlying patterns in the data.
- High bias and low variance
- Performs poorly on both training and test data.

**Overfitting** occurs when a model learns noise and details in the training data instead of the actual pattern.
- Has low bias and high variance
- Performs very well on training data, but poorly on unseen data.


For a model to be ideal, it should have low bias and low variance. However, in practice, it is not possible to build a model that achieves both simultaneously. This limitation leads to the use of ensemble models.

# Ensembles 
Instead of relying on a single model, ensemble learning involves building multiple models. Some of these models may underfit, while others may overfit. However, when we combine their predictions, typically by averaging or voting, the overall model performance improves. This aggregation helps reduce variance and partially compensate for bias, resulting in better generalization than any individual model.

This is the core idea behind ensemble methods.

Ensmbles is nothing but collection of models.


