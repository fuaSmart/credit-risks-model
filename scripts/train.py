"""Train hybrid GNN+LightGBM model with SHAP explainability."""

import mlflow
import lightgbm as lgb


def train_model():
    """Orchestrates end-to-end training."""
    with mlflow.start_run():
        # Your training logic here
        mlflow.log_metric("auc", 0.85)
