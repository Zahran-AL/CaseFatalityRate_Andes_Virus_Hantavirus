
import joblib
import pandas as pd
from sklearn.metrics import r2_score

# Lokasi file model dan data uji
MODEL_FILE = 'linear_regression_cfr_model.joblib'
X_TEST_FILE = 'X_test_for_pytest.csv'
Y_TEST_FILE = 'y_test_for_pytest.csv'

def test_model_loading():
    """Uji apakah model dapat dimuat dengan benar."""
    model = joblib.load(MODEL_FILE)
    assert model is not None

def test_model_performance():
    """Uji kinerja model pada data uji yang disimpan."""
    model = joblib.load(MODEL_FILE)
    X_test_loaded = pd.read_csv(X_TEST_FILE)
    y_test_loaded = pd.read_csv(Y_TEST_FILE)

    y_pred = model.predict(X_test_loaded)

    # Assert R-squared is still high (e.g., > 0.95, adjust as needed)
    r2 = r2_score(y_test_loaded, y_pred)
    print(f"\nPytest R2 Score: {r2:.4f}")
    assert r2 > 0.95, f"R2 score {r2:.4f} is not above expected threshold (0.95)"

def test_prediction_output_shape():
    """Uji apakah bentuk output prediksi sudah benar."""
    model = joblib.load(MODEL_FILE)
    X_test_loaded = pd.read_csv(X_TEST_FILE)
    
    # Ambil satu sampel dari X_test untuk prediksi
    sample_X = X_test_loaded.head(1)
    y_pred_single = model.predict(sample_X)
    assert y_pred_single.shape == (1,)

    # Uji prediksi batch
    y_pred_batch = model.predict(X_test_loaded)
    assert y_pred_batch.shape == (len(X_test_loaded),)
