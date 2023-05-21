from createApp import parent_dir
import subprocess
import os

def main():
    print("Welcome to Django Project Creator!")

    project_name = input("Enter name for your Django Project:") 
    
    print("Creating Project...")
    project_path = os.path.join(parent_dir, project_name)
    subprocess.run(["django-admin", "startproject", project_name])
    print("Project Created Successfully")
    manage_path = os.path.join(project_path, 'manage.py')

    print("Running migrations and creating superuser...")
    subprocess.run(['python', manage_path, 'makemigrations'])
    subprocess.run(['python', manage_path, 'migrate'])
    subprocess.run(['python', manage_path, 'createsuperuser'])

    app_name = input("Enter name for your Django App: ")
    # this should create the app from within the project directory
    out = subprocess.run(['python', manage_path, 'startapp', app_name], cwd=project_path)
    while out.returncode != 0:
        print("App already exists")
        app_name = input("Enter name for your Django App: ")
        out = subprocess.run(['python', manage_path, 'startapp', app_name])



    print("App Created Successfully")

    # run migrations
    print("Running migrations...")
    subprocess.run(['python', manage_path, 'makemigrations'])
    subprocess.run(['python', manage_path, 'migrate'])
    print("Migrations completed successfully")

    # open admin page
    print("Opening admin page...")
    subprocess.run(['python', manage_path, 'runserver'])


if __name__ == '__main__':
    print("test success")

# run script in terminal

