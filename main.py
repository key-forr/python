from ui import UserInterface
from user_manager import UserManager

def main():
    manager = UserManager()
    ui = UserInterface()
    
    ui.show_message("Програму запущено!", "success")
    print("Початковий DataFrame створено з 5 користувачами.")
    
    while True:
        ui.print_menu()
        choice = ui.get_input("\nВиберіть опцію: ").lower()
        
        if choice == 'a':
            ui.display_dataframe(manager.get_dataframe())
        
        elif choice == 'b':
            login, password, phone, email, auth_count = ui.get_user_data()
            success, message = manager.add_user(login, password, phone, email, auth_count)
            ui.show_message(message, "success" if success else "error")
        
        elif choice == 'c':
            if manager.is_empty():
                ui.show_message("DataFrame порожній! Нічого сортувати.", "warning")
            else:
                ui.display_columns(manager.get_columns())
                attribute, ascending = ui.get_sort_params()
                
                success, message, sorted_df = manager.sort_by_attribute(attribute, ascending)
                
                if success:
                    ui.show_message(message, "success")
                    ui.display_dataframe(sorted_df)
                    
                    if ui.confirm("Зберегти відсортований порядок?"):
                        manager.apply_sorted_dataframe(sorted_df)
                        ui.show_message("Порядок збережено!", "success")
                else:
                    ui.show_message(message, "error")
        
        elif choice == 'd':
            if manager.is_empty():
                ui.show_message("DataFrame порожній! Нічого видаляти.", "warning")
            else:
                ui.display_columns(manager.get_columns())
                attribute, value = ui.get_attribute_and_value("ВИДАЛЕННЯ ЗА АТРИБУТОМ")
                
                success, message, matching = manager.delete_by_attribute(attribute, value)
                
                if success:
                    ui.show_message(message, "success")
                    ui.display_dataframe(matching)
                    
                    if ui.confirm("Видалити цих користувачів?"):
                        success, msg = manager.confirm_delete_by_attribute(attribute, value)
                        ui.show_message(msg, "success" if success else "error")
                    else:
                        ui.show_message("Видалення скасовано.", "error")
                else:
                    ui.show_message(message, "error")
        
        elif choice == 'e':
            if manager.is_empty():
                ui.show_message("DataFrame порожній! Нічого видаляти.", "warning")
            else:
                print("\n--- ВИДАЛЕННЯ ЗА ІНДЕКСОМ ---")
                ui.display_dataframe(manager.get_dataframe())
                index = ui.get_input("\nВведіть індекс для видалення: ")
                
                success, message, user_info = manager.delete_by_index(index)
                
                if success:
                    ui.show_user_info(user_info)
                    
                    if ui.confirm("Підтвердити видалення?"):
                        success, msg = manager.confirm_delete_by_index(index)
                        ui.show_message(msg, "success" if success else "error")
                    else:
                        ui.show_message("Видалення скасовано.", "error")
                else:
                    ui.show_message(message, "error")
        
        elif choice == 'f':
            if manager.is_empty():
                ui.show_message("DataFrame порожній!", "warning")
            else:
                ui.display_columns(manager.get_columns())
                attribute, value = ui.get_attribute_and_value("ФІЛЬТРАЦІЯ ЗА АТРИБУТОМ")
                
                success, message, filtered = manager.filter_by_attribute(attribute, value)
                
                if success:
                    ui.show_message(message, "success")
                    ui.display_dataframe(filtered)
                else:
                    ui.show_message(message, "error")
        
        elif choice == 'q':
            ui.show_message("Дякуємо за використання програми! До побачення!", "success")
            break
        
        else:
            ui.show_message("Невірний вибір! Спробуйте ще раз.", "error")
        
        ui.wait_for_enter()


if __name__ == "__main__":
    main()