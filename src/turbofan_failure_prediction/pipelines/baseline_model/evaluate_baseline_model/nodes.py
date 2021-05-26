# Math Packages
# Logger
import logging

# Typing
from typing import Union

import numpy as np

# Data Handling Packages
import pandas as pd
from sklearn.base import RegressorMixin

# Machine Learning Packages
from sklearn.metrics import mean_squared_error, r2_score


def predict(model: RegressorMixin, X_test_df: pd.DataFrame) -> pd.DataFrame:
    """Compute the prediction of the model over the test set."""
    # Predict and evaluate the model
    y_test_pred = model.predict(X_test_df).reshape(-1, 1)

    # Convert to dataFrame
    y_test_pred_df = pd.DataFrame(y_test_pred, columns=["y_pred"])

    return y_test_pred_df


def evaluate_model(
    y_true: Union[np.array, pd.DataFrame],
    y_hat: Union[np.array, pd.DataFrame],
    label: str = "test",
) -> pd.DataFrame:
    """Evaluate the model."""
    # Compute the different metrics
    mse = mean_squared_error(y_true, y_hat)
    rmse = np.sqrt(mse)
    r2_metric = r2_score(y_true, y_hat)

    # Save the metrics
    metrics_dct = {"mse": mse, "rmse": rmse, "r2_score": r2_metric}

    # Log the metrics
    logging.info(f"{label} set RMSE:{rmse}, R2:{r2_metric}")

    # Convert the dict into a DataFrame
    metrics_df = pd.DataFrame(metrics_dct, index=["1"])

    return metrics_df
