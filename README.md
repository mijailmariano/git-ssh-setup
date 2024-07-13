# SSH Key Generator for Git

This script automates the generation and setup of SSH keys for use with Git, especially for managing multiple keys and configurations with services like GitHub.

## Features

- Generates SSH key pairs with a unique timestamp.
- Configures SSH to use specific keys for GitHub.
- Adds keys to the SSH agent for convenience.

## Requirements

- Python 3.12+ >> refer to the requirements.txt/yaml files
- Access to a UNIX-like terminal (Linux, macOS)

## Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Run the Script**
    ```bash
    python3 setupSSH.py
    ```

## Usage

Follow the prompts to enter your email address, which will be associated with your new SSH key. The script handles the rest, including:

- Generating a new SSH key pair.
- Adding the key to the SSH agent.
- Outputting instructions to add your public key to GitHub or other Git services.

### Important Notes

- **Private Key**: The file without the `.pub` extension.
- **Public Key**: The `.pub` file, which you should add to your Git service account.

## Additional Setup

### Configure SSH for Multiple Keys

If you have multiple keys and need to specify which to use with GitHub:

1. Edit or create `~/.ssh/config` and add:
    ```plaintext
    Host github.com
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_rsa_git_YYYYMMDD_HHMMSS
        IdentitiesOnly yes
    ```
    Replace `id_rsa_git_YYYYMMDD_HHMMSS` with your key filename.

### Start the SSH Agent Manually (use as needed in your workflow)

1. Start the SSH agent:
    ```bash
    eval "$(ssh-agent -s)"
    ```

2. Add your SSH key:
    ```bash
    ssh-add ~/.ssh/your_private_key_name
    ```

3. Verify the key is added:
    ```bash
    ssh-add -l
    ```

4. macOS users: To store the passphrase in your keychain:
    ```bash
    ssh-add -K ~/.ssh/your_private_key_name
    ```

## Persistence Across Sessions

- **macOS**: The key can be added to your keychain as shown above.
- **Linux**: Add the `ssh-add` command to your shell's startup file (e.g., `.bashrc` or `.zshrc`).

## Security Considerations

- Keep your private key secure and never share it.
- Regularly update or rotate your SSH keys for enhanced security.

For detailed instructions on adding keys to specific Git services, consult their respective documentation.
