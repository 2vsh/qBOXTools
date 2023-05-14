import ctypes
import sys
import subprocess
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        raise RuntimeError("Admin check is not supported on this platform.")

def run_with_admin_privileges():
    if is_admin():
        os.system(f'python "{os.path.abspath("split_drive.py")}"')
    else:
        script_path = os.path.abspath(sys.argv[0])
        params = f'"{script_path}"'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

if __name__ == "__main__":
    run_with_admin_privileges()
