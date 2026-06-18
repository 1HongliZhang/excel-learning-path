import subprocess
import os
import time

installer_path = os.path.join(os.environ.get("TEMP", "."), "Git-2.46.0-64-bit.exe")

print(f"Running installer: {installer_path}")
print("This may take a few minutes...")

start_time = time.time()
result = subprocess.run(
    [installer_path, "/VERYSILENT", "/NORESTART", "/NOCANCEL", "/SP-", "/SUPPRESSMSGBOXES"],
    capture_output=True,
    text=True,
    timeout=300
)

elapsed = time.time() - start_time
print(f"Installation completed in {elapsed:.1f} seconds")
print(f"Return code: {result.returncode}")

if result.stdout:
    print("STDOUT:", result.stdout[:500])
if result.stderr:
    print("STDERR:", result.stderr[:500])

if result.returncode == 0:
    print("\nChecking if Git was installed...")
    git_paths = [
        r"C:\Program Files\Git\bin\git.exe",
        r"C:\Program Files (x86)\Git\bin\git.exe"
    ]
    
    found = False
    for path in git_paths:
        if os.path.exists(path):
            print(f"Git installed at: {path}")
            found = True
            break
    
    if found:
        print("Git installation successful!")
    else:
        print("Git path not found, but installer succeeded")
        print("May need to restart terminal or check PATH")
else:
    print(f"Installation failed with code: {result.returncode}")
