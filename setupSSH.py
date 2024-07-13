import os
import stat
from pathlib import Path
from typing import Optional
import datetime
import subprocess

def get_user_input(prompt: str) -> str:
    '''Get user input with a given prompt.'''
    return input(prompt).strip()

def generate_ssh_key(email: str) -> tuple[Path, Path]:
    '''Generate a new SSH key pair with a timestamp.'''
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    key_name = f"id_rsa_git_{timestamp}"
    key_path = Path.home() / ".ssh" / key_name
    
    subprocess.run(['ssh-keygen', '-t', 'rsa', '-b', '4096', '-C', email, '-f', str(key_path)], check=True)
    
    return key_path, key_path.with_suffix('.pub')

def get_ssh_directory() -> Path:
    '''Get the SSH directory path.'''
    return Path.home() / ".ssh"

def create_ssh_directory(ssh_dir: Path) -> None:
    '''Create the SSH directory if it doesn't exist.'''
    ssh_dir.mkdir(mode=0o700, parents=True, exist_ok=True)

def print_instructions(key_file: Path) -> None:
    '''Print instructions for the user.'''
    print("\nSSH key has been successfully generated and added to the SSH agent.")
    print(f"Private key location: {key_file}")
    print(f"Public key location: {key_file}.pub")
    print("\nTo start using this SSH key with Git:")
    print("1. The key has been added to your SSH agent. You shouldn't need to enter the passphrase again in this session.")
    print("2. Add the public key to your Git account (e.g., GitHub, GitLab):")
    print(f"   cat {key_file}.pub")
    print("   Copy the output and add it to your Git account's SSH keys.")
    print("\nConsiderations:")
    print("- Keep your private key secure and never share it.")
    print("- If you need to change your SSH key in the future, generate a new key")
    print("  and replace the existing one in your Git account.")
    print("- To add the key to the SSH agent in future sessions, use:")
    print(f"   ssh-add {key_file}")
    print("- If you're using macOS, you might want to add the key to your keychain to remember the passphrase:")
    print(f"   ssh-add -K {key_file}")

def main() -> None:
    '''Main function to orchestrate the SSH key setup process.'''
    email = get_user_input("Enter your email address: ")
    ssh_dir = get_ssh_directory()
    create_ssh_directory(ssh_dir)
    
    private_key, public_key = generate_ssh_key(email)
    
    if private_key.exists() and public_key.exists():
        print(f"SSH key pair generated successfully:")
        print(f"Private key: {private_key}")
        print(f"Public key: {public_key}")
        
        with public_key.open('r') as f:
            public_key_content = f.read().strip()
        
        print("\nHere's your public key. Add this to your GitHub account:")
        print(public_key_content)
        
        print_instructions(private_key)
    else:
        print("Failed to generate SSH key pair.")

if __name__ == "__main__":
    main()