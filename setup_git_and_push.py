import subprocess
import os
import sys
import urllib.request
import zipfile
import shutil

def download_file(url, save_path):
    print(f"Downloading from: {url}")
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"Downloaded: {os.path.getsize(save_path) / (1024*1024):.2f} MB")
        return True
    except Exception as e:
        print(f"Download failed: {e}")
        return False

def extract_zip(zip_path, extract_dir):
    print(f"Extracting to: {extract_dir}")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print("Extraction complete")
        return True
    except Exception as e:
        print(f"Extraction failed: {e}")
        return False

def setup_git():
    git_dir = os.path.join(os.path.dirname(__file__), "git-portable")
    git_exe = os.path.join(git_dir, "bin", "git.exe")
    
    if os.path.exists(git_exe):
        print(f"Git already available at: {git_exe}")
        return git_exe
    
    print("\n=== Setting up portable Git ===")
    
    zip_path = os.path.join(os.environ.get("TEMP", "."), "git-portable.zip")
    urls = [
        "https://github.com/git-for-windows/git/releases/download/v2.46.0.windows.1/PortableGit-2.46.0-64-bit.7z.exe",
        "https://mirrors.tuna.tsinghua.edu.cn/github-release/git-for-windows/git/v2.46.0.windows.1/PortableGit-2.46.0-64-bit.7z.exe"
    ]
    
    download_success = False
    for url in urls:
        if download_file(url, zip_path):
            download_success = True
            break
    
    if not download_success:
        print("Failed to download Git")
        sys.exit(1)
    
    print("\nExtracting portable Git...")
    if os.path.exists(git_dir):
        shutil.rmtree(git_dir)
    
    os.makedirs(git_dir, exist_ok=True)
    
    result = subprocess.run(
        [zip_path, "-o" + git_dir, "-y"],
        capture_output=True,
        text=True,
        timeout=120
    )
    
    if result.returncode != 0 and not os.listdir(git_dir):
        print(f"Extraction failed: {result.stderr}")
        sys.exit(1)
    
    os.remove(zip_path)
    
    if os.path.exists(git_exe):
        print(f"Git setup successful: {git_exe}")
        return git_exe
    else:
        print("Git executable not found after extraction")
        sys.exit(1)

def git_push(git_exe, repo_url, commit_message):
    print(f"\n=== Pushing to GitHub ===")
    
    commands = [
        [git_exe, "init"],
        [git_exe, "config", "user.name", "1Honglizhang"],
        [git_exe, "config", "user.email", "user@example.com"],
        [git_exe, "add", "."],
        [git_exe, "commit", "-m", commit_message],
        [git_exe, "branch", "-M", "main"],
        [git_exe, "remote", "add", "origin", repo_url],
        [git_exe, "push", "-u", "origin", "main"]
    ]
    
    for cmd in commands:
        print(f"\nRunning: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.stdout:
            print(result.stdout.strip())
        if result.stderr:
            print(result.stderr.strip())
        
        if result.returncode != 0:
            print(f"\nCommand failed with code: {result.returncode}")
            return False
    
    print("\n✅ Push successful!")
    print(f"Repository: {repo_url}")
    return True

def main():
    repo_url = "https://github.com/1Honglizhang/excel-learning-path.git"
    commit_message = "Initial commit: Excel learning path from basic to professional"
    
    git_exe = setup_git()
    
    os.chdir(os.path.dirname(__file__))
    
    success = git_push(git_exe, repo_url, commit_message)
    
    if success:
        print("\n🎉 All done! Project uploaded to GitHub.")
    else:
        print("\n❌ Push failed. Please check the error messages above.")
        print("Make sure you have created the repository on GitHub first.")

if __name__ == "__main__":
    main()
