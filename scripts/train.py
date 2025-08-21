
import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Define file paths
BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "model_ready_data.csv"
MODEL_OUTPUT_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_OUTPUT_DIR / "logistic_regression_model.pkl"
SCALER_PATH = MODEL_OUTPUT_DIR / "scaler.pkl"
COLUMN_PATH = MODEL_OUTPUT_DIR / "model_columns.pkl"

def train_and_save_artifacts():
    """Loads data, trains the model, and saves the artifacts."""
    print("Loading processed data...")
    df = pd.read_csv(PROCESSED_DATA_PATH)

    # 1. Define Features (X) and Target (y)
    y = df['FraudResult']
    X = df.drop(columns=['FraudResult', 'CustomerId'])

    # 2. Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Scale Features
    print("Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 4. Train Model
    print("Training Logistic Regression model...")
    model = LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000)
    model.fit(X_train_scaled, y_train)
    print("Training complete.")
    
    # 5. Evaluate and print report
    y_pred = model.predict(X_test_scaled)
    print("\n--- Model Evaluation Report ---")
    print(classification_report(y_test, y_pred))
    print("-----------------------------\n")

    # 6. Save Artifacts
    print("Saving model and scaler artifacts...")
    MODEL_OUTPUT_DIR.mkdir(exist_ok=True)
    
    print("Saving model column order...")
    joblib.dump(X.columns.tolist(), COLUMN_PATH)
    print(f"Columns saved to: {COLUMN_PATH}")

    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    print(f"Model saved to: {MODEL_PATH}")
    print(f"Scaler saved to: {SCALER_PATH}")


if __name__ == "__main__":
    train_and_save_artifacts()

