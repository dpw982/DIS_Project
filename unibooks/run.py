from app import create_app

app = create_app()
print(app.static_folder)
if __name__ == "__main__":
    app.run(debug=True)