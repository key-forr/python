import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns

wine = load_wine()
X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
rf_model.fit(X_train_scaled, y_train)

y_pred_rf = rf_model.predict(X_test_scaled)

rf_accuracy = accuracy_score(y_test, y_pred_rf)
rf_cv_scores = cross_val_score(rf_model, X_train_scaled, y_train, cv=5)
rf_report = classification_report(y_test, y_pred_rf, target_names=wine.target_names)
cm_rf = confusion_matrix(y_test, y_pred_rf)

svm_model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
svm_model.fit(X_train_scaled, y_train)

y_pred_svm = svm_model.predict(X_test_scaled)

svm_accuracy = accuracy_score(y_test, y_pred_svm)
svm_cv_scores = cross_val_score(svm_model, X_train_scaled, y_train, cv=5)
svm_report = classification_report(y_test, y_pred_svm, target_names=wine.target_names)
cm_svm = confusion_matrix(y_test, y_pred_svm)

print("=" * 60)
print("ПОРІВНЯННЯ РЕЗУЛЬТАТІВ")
print("=" * 60)
print(f"\n{'Метод':<20} {'Точність':<12} {'CV Середнє':<15} {'CV Std':<10}")
print("-" * 60)
print(f"{'Random Forest':<20} {rf_accuracy:<12.4f} {rf_cv_scores.mean():<15.4f} {rf_cv_scores.std():<10.4f}")
print(f"{'SVM':<20} {svm_accuracy:<12.4f} {svm_cv_scores.mean():<15.4f} {svm_cv_scores.std():<10.4f}")

best_method = "Random Forest" if rf_accuracy > svm_accuracy else "SVM"
print(f"\nКращий метод за точністю: {best_method}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Порівняння моделей класифікації', fontsize=14, fontweight='bold')

sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Blues', ax=axes[0],
            xticklabels=wine.target_names, yticklabels=wine.target_names)
axes[0].set_title(f'Random Forest\nТочність: {rf_accuracy:.4f}')
axes[0].set_ylabel('Справжній клас')
axes[0].set_xlabel('Передбачений клас')

sns.heatmap(cm_svm, annot=True, fmt='d', cmap='Greens', ax=axes[1],
            xticklabels=wine.target_names, yticklabels=wine.target_names)
axes[1].set_title(f'SVM\nТочність: {svm_accuracy:.4f}')
axes[1].set_ylabel('Справжній клас')
axes[1].set_xlabel('Передбачений клас')

plt.tight_layout()
plt.show()