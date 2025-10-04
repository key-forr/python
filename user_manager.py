import pandas as pd

class UserManager:
    def __init__(self):
        self.df = self._create_initial_dataframe()
    
    def _create_initial_dataframe(self):
        data = {
            'Логін': ['user1', 'admin', 'john_doe', 'maria_k', 'developer'],
            'Пароль': ['pass123', 'admin2024', 'john1990', 'maria_secure', 'dev_pass'],
            'Телефон': ['+380501234567', '+380672345678', '+380933456789', '+380504567890', '+380675678901'],
            'Email': ['user1@gmail.com', 'admin@company.com', 'john@mail.com', 'maria@gmail.com', 'dev@company.com'],
            'Кількість_авторизацій': [15, 243, 8, 67, 102]
        }
        return pd.DataFrame(data)
    
    def get_dataframe(self):
        return self.df
    
    def get_columns(self):
        return self.df.columns.tolist()
    
    def is_empty(self):
        return self.df.empty
    
    def add_user(self, login, password, phone, email, auth_count):
        try:
            if not login:
                return False, "Логін не може бути порожнім!"
            
            auth_count = int(auth_count)
            
            new_user = pd.DataFrame({
                'Логін': [login],
                'Пароль': [password],
                'Телефон': [phone],
                'Email': [email],
                'Кількість_авторизацій': [auth_count]
            })
            
            self.df = pd.concat([self.df, new_user], ignore_index=True)
            return True, "Користувача успішно додано!"
            
        except ValueError:
            return False, "Кількість авторизацій має бути числом!"
        except Exception as e:
            return False, f"Помилка при додаванні: {e}"
    
    def sort_by_attribute(self, attribute, ascending=True):
        if self.df.empty:
            return False, "DataFrame порожній! Нічого сортувати.", None
        
        if attribute not in self.df.columns:
            return False, f"Атрибут '{attribute}' не знайдено!", None
        
        try:
            sorted_df = self.df.sort_values(by=attribute, ascending=ascending)
            return True, f"DataFrame відсортовано за атрибутом '{attribute}'", sorted_df
        except Exception as e:
            return False, f"Помилка при сортуванні: {e}", None
    
    def apply_sorted_dataframe(self, sorted_df):
        self.df = sorted_df.reset_index(drop=True)
    
    def delete_by_attribute(self, attribute, value):
        if self.df.empty:
            return False, "DataFrame порожній! Нічого видаляти.", None
        
        if attribute not in self.df.columns:
            return False, f"Атрибут '{attribute}' не знайдено!", None
        
        try:
            if attribute == 'Кількість_авторизацій':
                value = int(value)
            
            matching = self.df[self.df[attribute] == value]
            
            if matching.empty:
                return False, f"Користувачів з {attribute} = '{value}' не знайдено!", None
            
            return True, f"Знайдено {len(matching)} користувач(ів)", matching
            
        except ValueError:
            return False, "Невірний формат значення!", None
        except Exception as e:
            return False, f"Помилка: {e}", None
    
    def confirm_delete_by_attribute(self, attribute, value):
        try:
            if attribute == 'Кількість_авторизацій':
                value = int(value)
            
            count = len(self.df[self.df[attribute] == value])
            self.df = self.df[self.df[attribute] != value].reset_index(drop=True)
            return True, f"Видалено {count} користувач(ів)!"
        except Exception as e:
            return False, f"Помилка при видаленні: {e}"
    
    def delete_by_index(self, index):
        if self.df.empty:
            return False, "DataFrame порожній! Нічого видаляти.", None
        
        try:
            index = int(index)
            
            if index not in self.df.index:
                return False, f"Індекс {index} не існує!", None
            
            user_info = self.df.loc[index]
            return True, "Користувача знайдено", user_info
            
        except ValueError:
            return False, "Індекс має бути цілим числом!", None
        except Exception as e:
            return False, f"Помилка: {e}", None
    
    def confirm_delete_by_index(self, index):
        try:
            self.df = self.df.drop(int(index)).reset_index(drop=True)
            return True, "Користувача видалено!"
        except Exception as e:
            return False, f"Помилка при видаленні: {e}"
    
    def filter_by_attribute(self, attribute, value):
        if self.df.empty:
            return False, "DataFrame порожній!", None
        
        if attribute not in self.df.columns:
            return False, f"Атрибут '{attribute}' не знайдено!", None
        
        try:
            if attribute == 'Кількість_авторизацій':
                value = int(value)
            
            filtered = self.df[self.df[attribute] == value]
            
            if filtered.empty:
                return False, f"Користувачів з {attribute} = '{value}' не знайдено!", None
            
            return True, f"Знайдено {len(filtered)} користувач(ів)", filtered
            
        except ValueError:
            return False, "Невірний формат значення!", None
        except Exception as e:
            return False, f"Помилка: {e}", None