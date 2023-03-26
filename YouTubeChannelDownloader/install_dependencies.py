import os
import time
import subprocess

def install_dependencies():
    dependencies_dir = "DependenciesCheck"
    if not os.path.exists(dependencies_dir):
        os.makedirs(dependencies_dir)

    installed_flag_file = os.path.join(dependencies_dir, "dependencies_installed.txt")

    if os.path.exists(installed_flag_file):
        print("Dependencies already installed. Skipping installation.")
        return

    packages = ["httplib2", "google-auth-httplib2", "google-auth-oauthlib", "google-auth", "google-api-python-client", "pytube", "tqdm"]
    for package in packages:
        print(f"Installing {package}...")
        subprocess.check_call(["pip", "install", package])

    with open(installed_flag_file, "w") as f:
        f.write("Dependencies installed on: " + time.strftime("%Y-%m-%d %H:%M:%S"))

    print("All dependencies installed.")

if __name__ == "__main__":
    install_dependencies()
