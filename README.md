# Rinokopy | 梨乃子py

## Overview

Allows you to easily update the remote URL of your Git-repo in local machine. This is particularly<br>
useful when working with multiple repositories and needing to switch the remote URL frequently.

## Script Details
### First Step

- **Dependencies:** This script uses the `subprocess` module, which is part of the Python standard library.
- **Configuration:** In `rinoko.py`, make sure to replace `<username>` and `<access_token>` in the script with<br>
your GitHub username and personal access token, respectively.

## Alias Suggestion

To make it easier to run the script, you can create an alias called `rinoko` by adding it to your `.bashrc` or `.zshrc` file:

```bash
alias rinoko='python /path/to/rinoko.py'
```

Replace `/path/to/rinoko.py` with the actual path to the script on your system.

Once the alias is set, you can update the remote URL by simply running the following command in the terminal while inside the desired repository:

```bash
rinoko <repo_name>
```

For example:

```bash
rinoko your-repo
```

## Notes

- Ensure you have the necessary permissions to modify the Git repository's remote URL.
- For security reasons, avoid sharing the script with sensitive information like personal access tokens. Use placeholders or environment variables as needed.

---
**License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
