from typing import Any

from kedro.pipeline import Pipeline, node

from .nodes import preprocess_X_test, preprocess_X_train


def create_pipeline(**kwargs: Any) -> Pipeline:
    return Pipeline(
        [
            node(
                func=preprocess_X_train,
                inputs=dict(X_train_raw="X_train_raw", parameters="parameters"),
                outputs=["train_preprocessed_df", "StandardScaler"],
                name="preprocess_X_train_node",
            ),
            node(
                func=preprocess_X_test,
                inputs=dict(
                    X_test_raw="X_test_raw",
                    parameters="parameters",
                    scaler="StandardScaler",
                ),
                outputs="X_test_preprocessed_df",
                name="preprocess_X_test_node",
            ),
        ]
    )
