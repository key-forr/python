import os

class UserInterface:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_menu():
        print("\n" + "="*60)
        print("СИСТЕМА УПРАВЛІННЯ КОРИСТУВАЧАМИ".center(60))
        print("="*60)
        print("a. Вивести весь фрейм")
        print("b. Додати нового користувача")
        print("c. Відсортувати фрейм за атрибутом")
        print("d. Видалити користувача за значенням атрибута")
        print("e. Видалити користувача за індексом")
        print("f. Вивести користувачів за значенням атрибута")
        print("q. Вийти з програми")
        print("="*60)
    
    @staticmethod
    def display_dataframe(df, title="СПИСОК КОРИСТУВАЧІВ"):
        if df.empty:
            print("\nDataFrame порожній!")
        else:
            print("\n" + "="*60)
            print(title.center(60))
            print("="*60)
            print(df.to_string(index=True))
            print("="*60)
            print(f"Всього користувачів: {len(df)}")
    
    @staticmethod
    def display_columns(columns):
        print("Доступні атрибути:")
        for i, col in enumerate(columns, 1):
            print(f"{i}. {col}")
    
    @staticmethod
    def get_input(prompt):
        return input(prompt).strip()
    
    @staticmethod
    def get_user_data():
        print("\n--- ДОДАВАННЯ НОВОГО КОРИСТУВАЧА ---")
        login = input("Введіть логін: ").strip()
        password = input("Введіть пароль: ").strip()
        phone = input("Введіть телефон: ").strip()
        email = input("Введіть email: ").strip()
        auth_count = input("Введіть кількість авторизацій: ").strip()
        return login, password, phone, email, auth_count
    
    @staticmethod
    def get_sort_params():
        print("\n--- СОРТУВАННЯ ---")
        attribute = input("Введіть назву атрибута для сортування: ").strip()
        order = input("Порядок (asc - за зростанням, desc - за спаданням): ").strip().lower()
        ascending = True if order == 'asc' else False
        return attribute, ascending
    
    @staticmethod
    def get_attribute_and_value(title):
        print(f"\n--- {title} ---")
        attribute = input("Введіть назву атрибута: ").strip()
        value = input(f"Введіть значення атрибута '{attribute}': ").strip()
        return attribute, value
    
    @staticmethod
    def confirm(message):
        response = input(f"\n{message} (y/n): ").strip().lower()
        return response == 'y'
    
    @staticmethod
    def show_message(message, message_type="info"):
        symbols = {
            "success": "✅",
            "error": "❌",
            "warning": "⚠️",
            "info": "ℹ️"
        }
        symbol = symbols.get(message_type, "")
        print(f"\n{symbol} {message}")
    
    @staticmethod
    def show_user_info(user_series):
        print(f"\nВи хочете видалити користувача:")
        print(f"Логін: {user_series['Логін']}")
        print(f"Email: {user_series['Email']}")
    
    @staticmethod
    def wait_for_enter():
        input("\nНатисніть Enter для продовження...")