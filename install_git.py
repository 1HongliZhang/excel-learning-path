import os
import sys
import urllib.request
import subprocess
import shutil

def download_file(url, save_path):
    print(f"Downloading Git installer from {url}")
    print(f"Saving to: {save_path}")
    
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"Download completed!")
        print(f"File size: {os.path.getsize(save_path) / (1024 * 1024):.2f} MB")
        return True
    except Exception as e:
        print(f"Download failed: {str(e)}")
        return False

def install_git(installer_path):
    print(f"\nStarting Git installation...")
    
    cmd = [
        installer_path,
        "/VERYSILENT",
        "/NORESTART",
        "/NOCANCEL",
        "/SP-",
        "/SUPPRESSMSGBOXES",
        "/CLOSEAPPLICATIONS",
        "/RESTARTAPPLICATIONS",
        "/COMPONENTS=icons,ext\reg\shellhere,assoc,assoc_sh"
    ]
    
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate(timeout=300)
        
        if proc.returncode == 0:
            print("Git installation completed successfully!")
            return True
        else:
            print(f"Installation failed with exit code: {proc.returncode}")
            if stderr:
                print(f"Error: {stderr.decode('utf-8', errors='ignore')}")
            return False
    except subprocess.TimeoutExpired:
        print("Installation timed out!")
        return False
    except Exception as e:
        print(f"Installation error: {str(e)}")
        return False

def find_git_path():
    paths = [
        r"C:\Program Files\Git\bin\git.exe",
        r"C:\Program Files (x86)\Git\bin\git.exe",
        os.path.expanduser(r"~\AppData\Local\Programs\Git\bin\git.exe")
    ]
    
    for path in paths:
        if os.path.exists(path):
            return path
    return None

def main():
    installer_path = os.path.join(os.environ.get("TEMP", "."), "Git-2.46.0-64-bit.exe")
    
    # Check if Git is already installed
    git_path = find_git_path()
    if git_path:
        print(f"Git is already installed at: {git_path}")
        print(f"Git version:", end=" ")
        subprocess.run([git_path, "--version"])
        return
    
    # Download Git installer
    urls = [
        "https://github.com/git-for-windows/git/releases/download/v2.46.0.windows.1/Git-2.46.0-64-bit.exe",
        "https://mirrors.tuna.tsinghua.edu.cn/github-release/git-for-windows/git/LatestRelease/Git-2.46.0-64-bit.exe"
    ]
    
    download_success = False
    for url in urls:
        if download_file(url, installer_path):
            download_success = True
            break
    
    if not download_success:
        print("Failed to download Git installer from all sources")
        print("Please download Git manually from: https://git-scm.com/download/win")
        sys.exit(1)
    
    # Install Git
    if install_git(installer_path):
        # Clean up installer
        os.remove(installer_path)
        print("\nInstaller cleaned up")
        
        # Verify installation
        git_path = find_git_path()
        if git_path:
            print(f"\nGit installed successfully!")
            print(f"Path: {git_path}")
            result = subprocess.run([git_path, "--version"], capture_output=True, text=True)
            print(result.stdout.strip())
        else:
            print("\nGit installation may need a restart to take effect")
    else:
        print("\nGit installation failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
