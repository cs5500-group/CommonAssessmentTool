"""
Model training module for the Common Assessment Tool.
Handles the preparation, training, and saving of the prediction model.
"""

# Standard library imports
import pickle

# Third-party imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor


def prepare_training_data():
    """
    Loads and prepares the dataset for training.
    Returns:
        tuple: (features_train, targets_train)
    """
     # Load dataset
    data = pd.read_csv('data_commontool.csv')
    # Define feature columns
    feature_columns = [
        'age',                    # Client's age
        'gender',                 # Client's gender (bool)
        'work_experience',        # Years of work experience
        'canada_workex',          # Years of work experience in Canada
        'dep_num',               # Number of dependents
        'canada_born',           # Born in Canada
        'citizen_status',        # Citizenship status
        'level_of_schooling',    # Highest level achieved (1-14)
        'fluent_english',        # English fluency scale (1-10)
        'reading_english_scale', # Reading ability scale (1-10)
        'speaking_english_scale',# Speaking ability scale (1-10)
        'writing_english_scale', # Writing ability scale (1-10)
        'numeracy_scale',        # Numeracy ability scale (1-10)
        'computer_scale',        # Computer proficiency scale (1-10)
        'transportation_bool',   # Needs transportation support (bool)
        'caregiver_bool',       # Is primary caregiver (bool)
        'housing',              # Housing situation (1-10)
        'income_source',        # Source of income (1-10)
        'felony_bool',          # Has a felony (bool)
        'attending_school',     # Currently a student (bool)
        'currently_employed',   # Currently employed (bool)
        'substance_use',        # Substance use disorder (bool)
        'time_unemployed',      # Years unemployed
        'need_mental_health_support_bool'  # Needs mental health support (bool)
    ]
    # Define intervention columns
    intervention_columns = [
        'employment_assistance',
        'life_stabilization',
        'retention_services',
        'specialized_services',
        'employment_related_financial_supports',
        'employer_financial_supports',
        'enhanced_referrals'
    ]
    # Combine all feature columns
    all_features = feature_columns + intervention_columns
    # Prepare training data
    features = np.array(data[all_features])  # Changed from X to features
    targets = np.array(data['success_rate'])  # Changed from y to targets
    # Split the dataset
    features_train, _, targets_train, _ = train_test_split(  # Removed unused variables
        features,
        targets,
        test_size=0.2,
        random_state=42
    )
    return features_train, targets_train

def train_model_1(features_train, targets_train):
    """
    Train the Random Forest model using the dataset.
    Returns:
        RandomForestRegressor: Trained model for predicting success rates
    """
    # Initialize and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(features_train, targets_train)
    return model


def train_model_2(features_train, targets_train):
    """
    Train the Linear Regression model using the dataset.
    Returns:
        LinearRegression: Trained model for predicting success rates
    """
    # Initialize and train the model
    model = LinearRegression()
    model.fit(features_train, targets_train)
    return model


def train_model_3(features_train, targets_train):
    """
    Train the Gradient Boost model using the dataset.
    Returns:
        GradientBoostingRegressor: Trained model for predicting success rates
    """
    # Initialize and train the model
    model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    model.fit(features_train, targets_train)
    return model

def save_model(model, filename="model.pkl"):
    """
    Save the trained model to a file.
    Args:
        model: Trained model to save
        filename (str): Name of the file to save the model to
    """
    with open(filename, "wb") as model_file:
        pickle.dump(model, model_file)


def load_model(filename="model.pkl"):
    """
    Load a trained model from a file.
    Args:
        filename (str): Name of the file to load the model from
    Returns:
        The loaded model
    """
    with open(filename, "rb") as model_file:
        return pickle.load(model_file)


def main():
    features_train, targets_train = prepare_training_data()

    """Main function to train and save the model."""
    print("Starting model training...")
    model_1 = train_model_1(features_train, targets_train)
    model_2 = train_model_2(features_train, targets_train)
    model_3 = train_model_3(features_train, targets_train)
    save_model(model_1, filename="random_forest.pkl")
    save_model(model_2, filename="linear_regression.pkl")
    save_model(model_3, filename="gradient_boost.pkl")
    print("Model training completed and saved successfully.")


if __name__ == "__main__":
    main()
