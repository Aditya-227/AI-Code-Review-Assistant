import pickle
import pandas as pd

class BugPredictor:

    def __init__(self, model_path=None, feature_path=None):
        # Model loading kept optional so old files don't break
        self.model = None
        self.features = None

        if model_path and feature_path:
            try:
                with open(model_path, "rb") as f:
                    self.model = pickle.load(f)

                with open(feature_path, "rb") as f:
                    self.features = pickle.load(f)
            except:
                pass


    def predict(self, repo_features):

        df = pd.DataFrame(repo_features)

        if df.empty:
            raise ValueError("No repository features extracted")

        # Normalize values for scoring
        loc_norm = df["lines_of_code"] / (df["lines_of_code"].max() + 1)
        complexity_norm = df["cyclomatic_complexity"] / (df["cyclomatic_complexity"].max() + 1)
        func_norm = df["function_count"] / (df["function_count"].max() + 1)
        change_norm = df["change_frequency"] / (df["change_frequency"].max() + 1)

        # Bug risk score
        df["bug_probability"] = (
            0.35 * complexity_norm +
            0.30 * loc_norm +
            0.20 * func_norm +
            0.15 * change_norm
        )

        df["bug_probability"] = df["bug_probability"].round(3)

        return df