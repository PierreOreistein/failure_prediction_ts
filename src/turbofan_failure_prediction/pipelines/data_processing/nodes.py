# Data Handling Packages
from typing import Dict

import pandas as pd
from sklearn.base import BaseEstimator

# Machine Learning Packages
from sklearn.preprocessing import StandardScaler


def drop_unecessary_columns(df: pd.DataFrame, parameters: Dict) -> pd.DataFrame:
    """Remove unecessary columns."""
    # Load columns to drop defined in params
    columns_to_drop_l = parameters["columns_to_drop"]

    # Drop the columns
    df.drop(columns_to_drop_l, inplace=True, axis=1)

    return df


def add_remaining_useful_life(df: pd.DataFrame) -> pd.DataFrame:
    """Add remaining useful life to df."""
    # Get the total number of cycles for each unit
    grouped_by_unit_df = df.groupby(by="unit_nb")
    max_cycle_s = grouped_by_unit_df["time"].max()

    # Merge the max cycle back into the original frame
    result_df = df.merge(
        max_cycle_s.to_frame(name="max_cycle"), left_on="unit_nb", right_index=True
    )

    # Calculate remaining useful life for each row
    remaining_useful_life_s = result_df["max_cycle"] - result_df["time"]
    result_df["RUL"] = remaining_useful_life_s

    # drop max_cycle as it's no longer needed
    result_df = result_df.drop("max_cycle", axis=1)
    return result_df


def preprocess_X_train(X_train_raw: pd.DataFrame, parameters: Dict) -> pd.DataFrame:
    """Preprocesses the training data.

    Args:
        X_train_raw: Raw data.
    Returns:
        Preprocessed data, by dropping unnecessary columns and adding
        the Remaining Useful Life (RUL).
    """
    # Add RUL (target) to training set
    train_df = add_remaining_useful_life(X_train_raw)

    # Drop unecessary features
    train_df = drop_unecessary_columns(train_df, parameters=parameters)

    # Scale the sensors values
    scaler = StandardScaler()

    scaling_columns = [
        col_name for col_name in train_df.columns if col_name not in ["RUL"]
    ]
    train_df[scaling_columns] = scaler.fit_transform(train_df[scaling_columns])

    return train_df, scaler


def preprocess_X_test(
    X_test_raw: pd.DataFrame, parameters: Dict, scaler: BaseEstimator
) -> pd.DataFrame:
    """Preprocesses the testing data.

    Args:
        X_test_raw: Raw data.
    Returns:
        Preprocessed data, by dropping unecessary columns.
    """
    # Keep only the last timestamp
    X_test_df = X_test_raw.groupby("unit_nb").last().reset_index()

    # Drop unecessary features
    X_test_df = drop_unecessary_columns(X_test_df, parameters=parameters)

    # Scale the sensors values
    X_test = scaler.transform(X_test_df)
    X_test_df = pd.DataFrame(X_test, columns=X_test_df.columns, index=X_test_df.index)
    return X_test_df
