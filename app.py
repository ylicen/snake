import webview
import os
import sys
from pathlib import Path

def get_base_dir():
    """
    Return the base directory for assets.
    - onefile: use sys._MEIPASS
    - onedir: use os.path.dirname(sys.executable)
    - dev: use directory of this file
    """
    if getattr(sys, 'frozen', False):
        if hasattr(sys, '_MEIPASS'):
            return sys._MEIPASS  # onefile bundle temp dir
        return os.path.dirname(sys.executable)  # onedir exe dir
    return os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    base_dir = get_base_dir()
    index_path = os.path.join(base_dir, 'index.html')
    index_uri = Path(index_path).resolve().as_uri()
    webview.create_window('Snake Game', index_uri, width=800, height=740, min_size=(800, 740))
    webview.start(debug=False)