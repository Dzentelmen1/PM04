import sqlite3
from datetime import datetime

# 1. Функция инициализации системы (Настройка окружения)
def initialize_system():
    conn = sqlite3.connect('system_log.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS maintenance_log 
                      (id INTEGER PRIMARY KEY, component TEXT, action TEXT, date TEXT)''')
    conn.commit()
    conn.close()
    print("Система успешно инициализирована.")

# 2. Функция модификации компонента (Выполнение ТЗ)
def log_modification(component_name, change_description):
    conn = sqlite3.connect('system_log.db')
    cursor = conn.cursor()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO maintenance_log (component, action, date) VALUES (?, ?, ?)", 
                   (component_name, change_description, current_date))
    conn.commit()
    conn.close()
    print(f"Обновление компонента '{component_name}' зафиксировано.")

if __name__ == "__main__":
    initialize_system()
    log_modification("UI_Module", "Исправлена ошибка отображения шрифтов")
