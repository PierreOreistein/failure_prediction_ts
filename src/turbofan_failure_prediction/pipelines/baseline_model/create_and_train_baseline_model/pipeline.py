from typing import Any

from kedro.pipeline import Pipeline, node

from .nodes import create_baseline_model, train_baseline_model


def create_pipeline(**kwargs: Any) -> Pipeline:
    return Pipeline(
        [
            node(
                func=create_baseline_model,
                inputs=None,
                outputs="BaselineModel",
                name="create_baseline_model_node",
            ),
            node(
                func=train_baseline_model,
                inputs=dict(model="BaselineModel", train_df="train_preprocessed_df"),
                outputs="BaselineModelTrained",
                name="train_baseline_model_node",
            ),
        ]
    )
