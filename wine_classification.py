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
    X, y, test_size=0.5, random_state=42, stratify=y
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

# Знаходимо помилки
rf_errors = y_test != y_pred_rf
svm_errors = y_test != y_pred_svm
rf_error_indices = np.where(rf_errors)[0]
svm_error_indices = np.where(svm_errors)[0]

print("=" * 60)
print("ПОРІВНЯННЯ РЕЗУЛЬТАТІВ")
print("=" * 60)
print(f"\n{'Метод':<20} {'Точність':<12} {'CV Середнє':<15} {'CV Std':<10}")
print("-" * 60)
print(f"{'Random Forest':<20} {rf_accuracy:<12.4f} {rf_cv_scores.mean():<15.4f} {rf_cv_scores.std():<10.4f}")
print(f"{'SVM':<20} {svm_accuracy:<12.4f} {svm_cv_scores.mean():<15.4f} {svm_cv_scores.std():<10.4f}")

best_method = "Random Forest" if rf_accuracy > svm_accuracy else "SVM"
print(f"\nКращий метод за точністю: {best_method}")
print(f"\nКількість помилок Random Forest: {len(rf_error_indices)}")
print(f"Кількість помилок SVM: {len(svm_error_indices)}")

fig = plt.figure(figsize=(18, 12))
gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.3)

fig.suptitle('Порівняння моделей класифікації вин з аналізом помилок', fontsize=16, fontweight='bold')

ax1 = fig.add_subplot(gs[0, 0])
sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Blues', ax=ax1,
            xticklabels=wine.target_names, yticklabels=wine.target_names)
ax1.set_title(f'Random Forest\nТочність: {rf_accuracy:.4f}')
ax1.set_ylabel('Справжній клас')
ax1.set_xlabel('Передбачений клас')

ax2 = fig.add_subplot(gs[0, 1])
sns.heatmap(cm_svm, annot=True, fmt='d', cmap='Greens', ax=ax2,
            xticklabels=wine.target_names, yticklabels=wine.target_names)
ax2.set_title(f'SVM\nТочність: {svm_accuracy:.4f}')
ax2.set_ylabel('Справжній клас')
ax2.set_xlabel('Передбачений клас')

ax3 = fig.add_subplot(gs[0, 2])
models = ['Random Forest', 'SVM']
accuracies = [rf_accuracy, svm_accuracy]
colors = ['#2E86AB', '#06A77D']
bars = ax3.bar(models, accuracies, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
ax3.set_ylim([0.9, 1.0])
ax3.set_ylabel('Точність', fontweight='bold')
ax3.set_title('Порівняння точності моделей')
ax3.grid(axis='y', alpha=0.3, linestyle='--')
for bar, acc in zip(bars, accuracies):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 0.005,
             f'{acc:.4f}', ha='center', va='bottom', fontweight='bold', fontsize=10)

ax4 = fig.add_subplot(gs[1, :2])
x_pos = np.arange(5)
width = 0.35
bars1 = ax4.bar(x_pos - width/2, rf_cv_scores, width, label='Random Forest',
                color='#2E86AB', alpha=0.7, edgecolor='black')
bars2 = ax4.bar(x_pos + width/2, svm_cv_scores, width, label='SVM',
                color='#06A77D', alpha=0.7, edgecolor='black')
ax4.axhline(y=rf_cv_scores.mean(), color='#2E86AB', linestyle='--', 
            linewidth=2, alpha=0.5, label=f'RF середнє: {rf_cv_scores.mean():.4f}')
ax4.axhline(y=svm_cv_scores.mean(), color='#06A77D', linestyle='--', 
            linewidth=2, alpha=0.5, label=f'SVM середнє: {svm_cv_scores.mean():.4f}')
ax4.set_xlabel('Fold кросвалідації', fontweight='bold')
ax4.set_ylabel('Точність', fontweight='bold')
ax4.set_title('Результати крос-валідації (5-fold)')
ax4.set_xticks(x_pos)
ax4.set_xticklabels([f'Fold {i+1}' for i in range(5)])
ax4.legend(loc='lower right')
ax4.grid(axis='y', alpha=0.3, linestyle='--')

ax5 = fig.add_subplot(gs[1, 2])
metrics_data = {
    'Random Forest': [rf_accuracy, rf_cv_scores.mean(), rf_cv_scores.std()],
    'SVM': [svm_accuracy, svm_cv_scores.mean(), svm_cv_scores.std()]
}
metric_names = ['Точність\nна тесті', 'CV\nсереднє', 'CV\nстандартне\nвідхилення']
x = np.arange(len(metric_names))
width = 0.35
bars1 = ax5.bar(x - width/2, metrics_data['Random Forest'], width, 
                label='Random Forest', color='#2E86AB', alpha=0.7, edgecolor='black')
bars2 = ax5.bar(x + width/2, metrics_data['SVM'], width,
                label='SVM', color='#06A77D', alpha=0.7, edgecolor='black')
ax5.set_ylabel('Значення', fontweight='bold')
ax5.set_title('Зведення метрик')
ax5.set_xticks(x)
ax5.set_xticklabels(metric_names, fontsize=9)
ax5.legend()
ax5.grid(axis='y', alpha=0.3, linestyle='--')

# НОВА ДІАГРАМА: Аналіз помилок
ax6 = fig.add_subplot(gs[2, :])

# Підготовка даних для візуалізації помилок
error_data = []
for idx in rf_error_indices:
    error_data.append({
        'index': idx,
        'model': 'Random Forest',
        'true': wine.target_names[y_test[idx]],
        'predicted': wine.target_names[y_pred_rf[idx]]
    })

for idx in svm_error_indices:
    error_data.append({
        'index': idx,
        'model': 'SVM',
        'true': wine.target_names[y_test[idx]],
        'predicted': wine.target_names[y_pred_svm[idx]]
    })

if error_data:
    # Підрахунок типів помилок
    from collections import Counter
    
    rf_error_types = Counter([f"{wine.target_names[y_test[i]]} → {wine.target_names[y_pred_rf[i]]}" 
                               for i in rf_error_indices])
    svm_error_types = Counter([f"{wine.target_names[y_test[i]]} → {wine.target_names[y_pred_svm[i]]}" 
                                for i in svm_error_indices])
    
    # Об'єднуємо всі типи помилок
    all_error_types = set(list(rf_error_types.keys()) + list(svm_error_types.keys()))
    
    if all_error_types:
        error_types_list = sorted(list(all_error_types))
        rf_counts = [rf_error_types.get(et, 0) for et in error_types_list]
        svm_counts = [svm_error_types.get(et, 0) for et in error_types_list]
        
        x = np.arange(len(error_types_list))
        width = 0.35
        
        bars1 = ax6.bar(x - width/2, rf_counts, width, label='Random Forest',
                        color='#2E86AB', alpha=0.7, edgecolor='black')
        bars2 = ax6.bar(x + width/2, svm_counts, width, label='SVM',
                        color='#06A77D', alpha=0.7, edgecolor='black')
        
        ax6.set_xlabel('Тип помилки (Справжній → Передбачений)', fontweight='bold')
        ax6.set_ylabel('Кількість помилок', fontweight='bold')
        ax6.set_title('Аналіз помилок: Де саме моделі помилилися', fontsize=12, fontweight='bold')
        ax6.set_xticks(x)
        ax6.set_xticklabels(error_types_list, rotation=45, ha='right')
        ax6.legend()
        ax6.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Додаємо значення на стовпці
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                if height > 0:
                    ax6.text(bar.get_x() + bar.get_width()/2., height,
                            f'{int(height)}', ha='center', va='bottom', fontsize=9)
    else:
        ax6.text(0.5, 0.5, 'Помилок не виявлено!', 
                ha='center', va='center', fontsize=14, fontweight='bold',
                transform=ax6.transAxes)
        ax6.set_xticks([])
        ax6.set_yticks([])
else:
    ax6.text(0.5, 0.5, 'Обидві моделі класифікували всі зразки правильно!', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            transform=ax6.transAxes)
    ax6.set_xticks([])
    ax6.set_yticks([])

plt.show()

# Детальний звіт про помилки
if len(rf_error_indices) > 0 or len(svm_error_indices) > 0:
    print("\n" + "=" * 60)
    print("ДЕТАЛЬНИЙ АНАЛІЗ ПОМИЛОК")
    print("=" * 60)
    
    if len(rf_error_indices) > 0:
        print("\nПомилки Random Forest:")
        for idx in rf_error_indices:
            print(f"  Зразок {idx}: Справжній клас = {wine.target_names[y_test[idx]]}, "
                  f"Передбачений = {wine.target_names[y_pred_rf[idx]]}")
    
    if len(svm_error_indices) > 0:
        print("\nПомилки SVM:")
        for idx in svm_error_indices:
            print(f"  Зразок {idx}: Справжній клас = {wine.target_names[y_test[idx]]}, "
                  f"Передбачений = {wine.target_names[y_pred_svm[idx]]}")