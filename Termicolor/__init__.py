from .Color import Color
from .Ansi import ansi
import sys

if sys.platform == "win32":
    from colorama import just_fix_windows_console
    just_fix_windows_console()

__version__ = "0.1.0"