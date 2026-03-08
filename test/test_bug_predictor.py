from repo_loader import load_repository, get_file_change_frequency
from feature_extractor import extract_repo_features
from bug_predictor import BugPredictor

repo_path = r"C:\Users\Aditya\Projects\AI_Code_Review_Assistant"

repo = load_repository(repo_path)

freq = get_file_change_frequency(repo)

features = extract_repo_features(repo_path, freq)

predictor = BugPredictor(
    "models/bug_prediction_model.pkl",
    "models/feature_list.pkl"
)

results = predictor.predict(features)

print(results[["file","bug_probability"]])