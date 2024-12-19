from app import create_app

# Создаем приложение с помощью фабрики
app = create_app()

# Запускаем приложение
if __name__ == '__main__':
    app.run(debug=True)
