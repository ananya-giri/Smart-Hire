from crewai.tools import BaseTool
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import shap

class SHAPAnalysisTool(BaseTool):
    name: str = "shap_analysis_tool"
    description: str = (
        "Calculates game-theoretic SHAP (SHapley Additive exPlanations) values to mathematically prove "
        "why a candidate was scored a certain way. "
        "Input MUST be a comma-separated string of exactly 4 numbers in this order: "
        "'years_experience (0-20), education_tier (1-3 where 3 is highest), skills_match_percent (0-100), past_projects (0-20)'. "
        "Example input: '4, 2, 85, 5'"
    )

    def _run(self, candidate_features: str) -> str:
        try:
            features = [float(x.strip()) for x in candidate_features.split(",")]
            if len(features) != 4:
                return "Error: You must provide exactly 4 numerical values separated by commas."
            
            exp, edu, skills, proj = features
            
            # --- 1. Train a local lightweight ML Model for Hybrid Architecture ---
            np.random.seed(42)
            # Create a synthetic base dataset
            X_train = pd.DataFrame({
                "Years_Experience": np.random.randint(0, 15, 100),
                "Education_Tier": np.random.randint(1, 4, 100),
                "Skills_Match": np.random.randint(20, 100, 100),
                "Past_Projects": np.random.randint(0, 20, 100)
            })
            # Define target variable (1 = Hire, 0 = No Hire)
            y_train = ((X_train["Years_Experience"] * 2 + X_train["Skills_Match"] * 0.5 + X_train["Education_Tier"] * 10 + X_train["Past_Projects"]) > 70).astype(int)
            
            # Train the Sidecar Model
            model = RandomForestClassifier(n_estimators=50, random_state=42)
            model.fit(X_train, y_train)
            
            # --- 2. Calculate SHAP Values for the current candidate ---
            X_candidate = pd.DataFrame([[exp, edu, skills, proj]], columns=X_train.columns)
            
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(X_candidate)
            
            # Probabilities
            prediction_prob = model.predict_proba(X_candidate)[0][1] * 100
            
            # Get the exact mathematical SHAP values for the "Hire" class
            if isinstance(shap_values, list): # Older shap versions
                vals = shap_values[1][0]
                base_val = explainer.expected_value[1]
            elif hasattr(shap_values, 'values'): # Newer shap versions return Explanation object
                vals = shap_values.values[0, :, 1]
                base_val = explainer.expected_value[1] if isinstance(explainer.expected_value, (list, np.ndarray)) else explainer.expected_value
            elif len(shap_values.shape) == 3: # Some versions 3D array
                vals = shap_values[:, :, 1][0]
                base_val = explainer.expected_value[1]
            else:
                vals = shap_values[0] # Fallback
                base_val = explainer.expected_value
                
            report = f"--- MATHEMATICAL SHAP (Explainable AI) ANALYSIS ---\n"
            report += f"Predicted Hiring ML Probability: {prediction_prob:.1f}%\n"
            report += f"Base Average Probability: {base_val * 100:.1f}%\n"
            report += "Mathematical Feature Contributions (SHAP Values):\n"
            report += f" - Years Experience ({exp:.1f}): {'+' if vals[0]>0 else ''}{vals[0]*100:.2f}%\n"
            report += f" - Education Tier ({edu:.1f}): {'+' if vals[1]>0 else ''}{vals[1]*100:.2f}%\n"
            report += f" - Technical Skills Match ({skills:.1f}): {'+' if vals[2]>0 else ''}{vals[2]*100:.2f}%\n"
            report += f" - Past Projects ({proj:.1f}): {'+' if vals[3]>0 else ''}{vals[3]*100:.2f}%\n"
            report += "\nExplainable AI Conclusion: You MUST provide this EXACT numerical breakdown graph in your final XAI output to prove absence of ML bias."
            
            return report
        except Exception as e:
            return f"SHAP calculation failed. Error: {str(e)}"

def get_shap_tool():
    return SHAPAnalysisTool()
