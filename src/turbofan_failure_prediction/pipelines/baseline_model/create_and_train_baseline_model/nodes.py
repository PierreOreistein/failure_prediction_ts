# Data Handling Packages
import pandas as pd
from sklearn.base import RegressorMixin

# Machine Learning Packages
from sklearn.linear_model import LinearRegression


def create_baseline_model() -> RegressorMixin:
    """Create Baseline model"""
    # Initialisation of the model
    model = LinearRegression()
    return model


def train_baseline_model(
    model: RegressorMixin, train_df: pd.DataFrame
) -> RegressorMixin:
    """Train the baseline model."""
    # Extract X and Y
    X_train_df = train_df
    y_train_df = X_train_df.pop("RUL")

    # Train the baseline model
    model.fit(X_train_df, y_train_df)

    return model
