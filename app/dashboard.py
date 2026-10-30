import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from explainerdashboard import ClassifierExplainer, ExplainerDashboard

df = pd.read_csv("dataset.csv")

# та же предобработка, что и в ноутбуках
df["Sex"] = df["Sex"].str.upper()
for col in ["Diameter", "Whole weight", "Shell weight"]:
    df[col] = df[col].fillna(df[col].median())

# 1 - старый абалон (колец больше медианы 9), 0 - молодой
y = (df["Rings"] > 9).astype(int)
X = pd.get_dummies(df.drop(columns=["Rings"]), columns=["Sex"], dtype=int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
model.fit(X_train, y_train)

explainer = ClassifierExplainer(model, X_test, y_test, labels=["Молодой", "Старый"])

db = ExplainerDashboard(explainer, title="Abalone: молодой или старый?")
db.to_yaml("dashboard.yaml", explainerfile="explainer.joblib", dump_explainer=True)
