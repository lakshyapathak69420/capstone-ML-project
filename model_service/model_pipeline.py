import pickle

MEAN = 28.5627
STD = 6.6899


model_path = "/home/black_tree/Documents/computer_science/capstone-ML-project/models/random_forest.pkl"
with open(model_path, "rb") as f:
    prediction_model = pickle.load(f)

numeric_feature = ["BMI"]
def standardScaler(value , mean = MEAN, Std = STD):
    rescaled_value = (value - mean)/Std
    return rescaled_value 
