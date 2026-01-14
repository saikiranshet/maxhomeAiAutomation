import os
import shutil

REPORTS_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'reports')

def clean_reports_folder():
    if os.path.exists(REPORTS_DIR):
        for filename in os.listdir(REPORTS_DIR):
            file_path = os.path.join(REPORTS_DIR, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

