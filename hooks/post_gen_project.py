import subprocess

remote_url = "{{cookiecutter.git_repo_url}}"

# Initialize the repository
subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", "Initial commit"])

# Add the remote as origin
subprocess.call(["git", "remote", "add", "origin", remote_url])
