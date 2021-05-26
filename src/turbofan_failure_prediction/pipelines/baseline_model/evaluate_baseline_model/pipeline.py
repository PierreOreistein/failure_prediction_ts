from typing import Any

from kedro.pipeline import Pipeline, node

from .nodes import evaluate_model, predict


def create_pipeline(**kwargs: Any) -> Pipeline:
    return Pipeline(
        [
            node(
                func=predict,
                inputs=dict(
                    model="BaselineModelTrained", X_test_df="X_test_preprocessed_df"
                ),
                outputs="y_test_pred",
                name="predict_baseline_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=dict(y_true="y_test_raw", y_hat="y_test_pred"),
                outputs="BaselineMetrics",
                name="evaluate_model_model_node",
            ),
        ]
    )
