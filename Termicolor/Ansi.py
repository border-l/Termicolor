from .Attributes import Attributes

def ansi(*names):
    combined = ""
    for name in names:
        if not name in Attributes:
            continue
        combined += Attributes[name]
    return combined