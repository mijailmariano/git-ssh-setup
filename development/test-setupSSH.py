import os
import stat
import argparse
from pathlib import Path
from typing import Optional

def get_user_input(prompt: str) -> str:
    '''Get user input with a given prompt.'''
    return input(prompt).strip()

def get_ssh_key() -> str:
    '''Prompt the user for their Git SSH key.'''
    print("Please enter your Git SSH key (paste and press Enter, then Ctrl+D to finish):")
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return "\n".join(lines)

def get_ssh_directory() -> Path:
    '''Get the SSH directory path.'''
    return Path.home() / ".ssh"

def create_ssh_directory(ssh_dir: Path) -> None:
    '''Create the SSH directory if it doesn't exist.'''
    ssh_dir.mkdir(mode=0o700, parents=True, exist_ok=True)

def write_ssh_key(ssh_dir: Path, ssh_key: str) -> Optional[Path]:
    '''Test writing an SSH key to a pseudo file in the SSH directory.'''

    key_file = ssh_dir / "id_rsa_git_test" # changed filename from id_rsa_git to id_rsa_git_test
    try:
        with key_file.open("w", encoding="utf-8") as f:
            f.write(ssh_key)
        key_file.chmod(0o600)
        return key_file
    except IOError as e:
        print(f"Error writing SSH key: {e}")
        return None

def print_instructions(key_file: Path) -> None:
    '''Print instructions for the user.'''
    print("\nSSH key has been successfully stored.")
    print(f"File location: {key_file}")
    print("\nTo start using this SSH key with Git:")
    print("1. Add the key to your SSH agent:")
    print(f"   ssh-add {key_file}")
    print("2. Add the public key to your Git account (e.g., GitHub, GitLab):")
    print(f"   cat {key_file}.pub")
    print("   Copy the output and add it to your Git account's SSH keys.")
    print("\n***************************************************************")
    print("************************ Considerations ************************")
    print("***************************************************************")
    print("- Keep your private key secure and never share it.")
    print("- If you need to change your SSH key in the future, generate a new key")
    print("  and replace the existing one in the same location.")
    print("- Remember to update the key on your Git account as well.")

def main() -> None:
    """
    Main function to orchestrate the SSH key setup process.
    Includes a test mode option for safely trying out the program.
    """
    # Set up the argument parser to handle command-line options
    parser = argparse.ArgumentParser(description="Set up Git SSH key")
    
    # Add a '--test' flag. If used, it will activate test mode
    parser.add_argument("--test", action="store_true", help="Run in test mode")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the SSH key from the user
    ssh_key = get_ssh_key()

    # Decide which directory to use based on whether we're in test mode
    if args.test:
        # In test mode, use a separate test directory
        ssh_dir = Path.home() / ".ssh_test"
    else:
        # In normal mode, use the standard SSH directory
        ssh_dir = get_ssh_directory()

    # Create the chosen directory if it doesn't exist
    create_ssh_directory(ssh_dir)

    # Write the SSH key to a file in the chosen directory
    key_file = write_ssh_key(ssh_dir, ssh_key)
    
    # If the key was successfully written, print instructions for the user
    if key_file:
        print_instructions(key_file)

if __name__ == "__main__":
    main()