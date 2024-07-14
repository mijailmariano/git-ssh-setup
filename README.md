# Git SSH Key Generator

This script creates and sets up SSH keys for Git services like GitHub, making it easier to manage multiple keys.

## Features

- [ ] Creates SSH key pairs with unique and timestamp
- [ ] Sets up SSH for use with GitHub/GitLab
- [ ] ~~Adds keys to the SSH agent for convenience~~

## Requirements

- [ ] Python 3.12+ 
- [ ] Access to your UNIX-like terminal (Linux, macOS)

See `requirements.txt/environment.yaml` for Python requirements

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

3. **Follow Prompts to Create Your SSH Key**

### What It Does

Follow the prompts to enter your email address, which will be associated with your new SSH key. The script handles the rest, including:

- Links your email to your new SSH key
- Creates a  SSH key pair
- Prints terminal instructions to add your public key to GitHub or other Git services

### Config Notes

- **Private Key**: The file without the `.pub` extension.
- **Public Key**: The `.pub` file, which you should add to your Git service account.

## Additional Setup Instructions

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

### Manual SSH Agent Setup (use as needed in your workflow)

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

- [ ] Keep your private key secure and never share it.
- [ ] Regularly update or rotate your SSH keys for enhanced security.

For detailed instructions on adding keys to specific Git services, check-out their official docs.