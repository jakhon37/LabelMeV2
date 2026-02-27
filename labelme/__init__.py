import importlib.metadata
import logging

__appname__ = "Labelme"

# Semantic Versioning 2.0.0: https://semver.org/
# 1. MAJOR version when you make incompatible API changes;
# 2. MINOR version when you add functionality in a backwards-compatible manner;
# 3. PATCH version when you make backwards-compatible bug fixes.
# e.g., 1.0.0a0, 1.0.0a1, 1.0.0b0, 1.0.0rc0, 1.0.0, 1.0.0.post0
try:
    __version__ = importlib.metadata.version("labelmev2")
except importlib.metadata.PackageNotFoundError:
    # Development mode - get version from git tags
    try:
        import subprocess
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            cwd=__file__.rsplit("/", 1)[0],
        )
        __version__ = result.stdout.strip() if result.returncode == 0 else "dev"
    except Exception:
        __version__ = "dev"

# XXX: has to be imported before PyQt5 to load dlls in order on Windows
# https://github.com/wkentaro/labelme/issues/1564
import onnxruntime

from labelme import testing
from labelme import utils
from labelme._label_file import LabelFile
