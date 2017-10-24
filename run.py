from banking.app import create_app, db

if __name__ == "__main__":
    app = create_app()
    app.run(port=3000, host="0.0.0.0")
