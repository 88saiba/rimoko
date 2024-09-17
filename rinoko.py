import sys
import subprocess

def set_git_remote_url(repo_name):
    if not repo_name:
        print("Please provide a repository name.")
        return

    # Replace this section with a suitable URL
    url = f"https://<username>:<access_token>@github.com/<username>/{repo_name}.git"

    try:
        # Update the remote URL
        subprocess.run(["git", "remote", "set-url", "origin", url], check=True)
        print(f"Remote URL for repository '{repo_name}' has been updated.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while setting remote URL: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sbrepo.py <repo_name>")
    else:
        repo_name = sys.argv[1]
        set_git_remote_url(repo_name)
