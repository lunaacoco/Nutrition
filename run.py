from app.app import create_app

#This file keeps starting the Flask server in a seperate file

app = create_app()

if __name__ == '__main__':
    app.run()