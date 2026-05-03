import numpy as np
from sklearn.linear_model import LinearRegression

# In a real-world scenario, you would load a pre-trained model.
# For this simple example, we'll train a basic model on-the-fly or simulate one.
class ExamScoreModel:
    def __init__(self):
        self.model = LinearRegression()
        # Simple synthetic data: score = 10 * hours + 5
        # Reshaping for sklearn: X must be 2D
        X = np.array([[1], [2], [3], [4], [5], [10]])
        y = np.array([15, 25, 35, 45, 55, 105])
        self.model.fit(X, y)

    def predict(self, hours_studied: float) -> float:
        # Prepare input for prediction
        input_data = np.array([[hours_studied]])
        prediction = self.model.predict(input_data)
        return float(prediction[0])

# Instantiate the model for use in the API
exam_model = ExamScoreModel()
