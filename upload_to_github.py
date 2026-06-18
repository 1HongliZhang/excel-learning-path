import os
import sys
import json
import base64
import argparse
import urllib.request

def get_files_recursive(root_dir):
    files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.startswith('.') or filename.endswith('.pyc'):
                continue
            if '__pycache__' in dirpath:
                continue
            full_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(full_path, root_dir).replace('\\', '/')
            files.append((full_path, rel_path))
    return files

def upload_files(token, owner, repo, files):
    base_url = f"https://api.github.com/repos/{owner}/{repo}"
    
    for full_path, rel_path in files:
        try:
            with open(full_path, 'rb') as f:
                content = f.read()
            
            encoded_content = base64.b64encode(content).decode('utf-8')
            
            url = f"{base_url}/contents/{rel_path}"
            headers = {
                'Authorization': f'token {token}',
                'Content-Type': 'application/json'
            }
            
            data = {
                'message': f'Add {rel_path}',
                'content': encoded_content
            }
            
            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='PUT')
            response = urllib.request.urlopen(req, timeout=30)
            result = json.loads(response.read().decode('utf-8'))
            
            print(f"✅ {rel_path}")
            
        except Exception as e:
            print(f"❌ {rel_path} - {str(e)}")

def create_repo(token, owner, repo_name):
    url = "https://api.github.com/user/repos"
    headers = {
        'Authorization': f'token {token}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'name': repo_name,
        'description': 'Excel learning path from basic to professional',
        'private': False,
        'auto_init': False
    }
    
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
        response = urllib.request.urlopen(req, timeout=30)
        result = json.loads(response.read().decode('utf-8'))
        print(f"✅ Repository created: {result['html_url']}")
        return True
    except urllib.error.HTTPError as e:
        if e.code == 422:
            print(f"⚠️  Repository already exists")
            return True
        else:
            print(f"❌ Failed to create repo: {e.read().decode('utf-8')}")
            return False

def main():
    parser = argparse.ArgumentParser(description='Upload project to GitHub')
    parser.add_argument('--token', required=True, help='GitHub Personal Access Token')
    args = parser.parse_args()
    
    owner = "1Honglizhang"
    repo_name = "excel-learning-path"
    
    print(f"=== Uploading to GitHub ===")
    print(f"Owner: {owner}")
    print(f"Repo: {repo_name}")
    print()
    
    print("Step 1: Creating repository...")
    if not create_repo(args.token, owner, repo_name):
        sys.exit(1)
    
    print()
    print("Step 2: Collecting files...")
    root_dir = os.path.dirname(__file__)
    files = get_files_recursive(root_dir)
    print(f"Found {len(files)} files to upload")
    
    print()
    print("Step 3: Uploading files...")
    upload_files(args.token, owner, repo_name, files)
    
    print()
    print(f"🎉 Done!")
    print(f"Repository URL: https://github.com/{owner}/{repo_name}")

if __name__ == "__main__":
    main()
