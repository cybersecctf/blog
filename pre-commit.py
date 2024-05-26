import subprocess

def run_pre_commit_checks():
    # Example: Run linting checks
    result = subprocess.run(["flake8"], capture_output=True)
    if result.returncode != 0:
        print("Linting checks failed:")
        print(result.stdout.decode("utf-8"))
        return False
    return True

if __name__ == "__main__":
    if not run_pre_commit_checks():
        exit(1)