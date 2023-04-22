import os
import subprocess

def main():
    requirements_file = "requirements.txt"
    with open(requirements_file, "r") as f:
        packages = f.readlines()

    for package in packages:
        package = package.strip()
        subprocess.check_call(["pip", "install", package])

if __name__ == "__main__":
    main()
