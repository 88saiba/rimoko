# Rimokopy

## Overview

Allows you to easily update the remote URL of your Git-repo in local machine. This is particularly<br>
useful when working with multiple repositories and needing to switch the remote URL frequently.

## Script Details
### First Step

- **Dependencies:** This script uses the `subprocess` module, which is part of the Python standard library.
- **Configuration:** In `rimoko.py`, make sure to replace `<username>` and `<access_token>` in the script with<br>
your GitHub username and personal access token, respectively.


## Usage

1. **Clone the repository or download the script.**
   
2. **Open a terminal and navigate to the directory containing the script.**

3. **Run the script with the repository name as an argument:**

    ```bash
    python rimoko.py <repo_name>
    ```
    
    Replace `<repo_name>` with the name of your repository.

## Example

If you want to set the remote URL for a repository named `your-repo`, you would use:

```bash
python rimoko.py your-repo
```

This command will update the `origin` remote URL to:

```
https://<username>:<access_token>@github.com/<username>/your-repo.git
```

## Alias Suggestion

To make it easier to run the script, you can create an alias called `rimoko` by adding it to your `.bashrc` or `.zshrc` file:

```bash
alias rimoko='python /path/to/rimoko.py'
```

Replace `/path/to/rimoko.py` with the actual path to the script on your system.

Once the alias is set, you can update the remote URL by simply running the following command in the terminal while inside the desired repository:

```bash
rimoko <repo_name>
```

For example:

```bash
rimoko your-repo
```

## Notes

- Ensure you have the necessary permissions to modify the Git repository's remote URL.
- For security reasons, avoid sharing the script with sensitive information like personal access tokens. Use placeholders or environment variables as needed.

---

Using [MIT LICENSE](/LICENSE)
