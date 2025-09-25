import os
import csv
import subprocess
from datetime import datetime

# === CONFIGURATION ===
GIT_URL = "https://github.com/Black-Santhosh/Student_Monitoring_System.git"
LOCAL_REPO = r"D:\document"  # Change path
OUTPUT_CSV = r"D:\document\student_monitoring_commits.csv"

def clone_repo_if_needed():
    """Clone the repo if it doesn't exist."""
    if not os.path.exists(LOCAL_REPO):
        print("Cloning repository...")
        subprocess.run(["git", "clone", GIT_URL, LOCAL_REPO], check=True)
    else:
        print("Repo already exists, skipping clone.")

def get_git_file_info(repo_path):
    """Get file name, last commit hash, and date from a Git repository."""
    os.chdir(repo_path)
    result = subprocess.run(
        ["git", "log", "--pretty=format:%H|%ad", "--date=iso", "--name-only"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print("Error running git command:", result.stderr)
        return []

    lines = result.stdout.strip().split("\n")
    data = []
    current_commit = None
    current_date = None

    for line in lines:
        if "|" in line:  # Commit hash and date
            parts = line.split("|")
            current_commit = parts[0].strip()
            current_date = parts[1].strip()
        elif line.strip():  # File name
            data.append([line.strip(), current_commit, current_date])

    return data

def save_to_csv(data, output_file):
    """Save the extracted data to CSV."""
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["File Name", "Commit Hash", "Commit Date"])
        writer.writerows(data)
    print(f"CSV saved successfully at: {output_file}")

# === RUN SCRIPT ===
if __name__ == "__main__":
    clone_repo_if_needed()
    file_info = get_git_file_info(LOCAL_REPO)
    if file_info:
        save_to_csv(file_info, OUTPUT_CSV)
