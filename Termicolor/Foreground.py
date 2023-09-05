class Foreground:
    def color(s, color):
        if color < 31 or color > 37: return
        s.val["fore"] = f"\033[{str(color)}m"
        return s
    
    @property
    def black(s):
        s.color(30)
        return s
    
    @property
    def red(s):
        s.color(31)
        return s
    
    @property
    def green(s):
        s.color(32)
        return s
    
    @property
    def yellow(s):
        s.color(33)
        return s
    
    @property
    def blue(s):
        s.color(34)
        return s
    
    @property
    def magenta(s):
        s.color(35)
        return s
    
    @property
    def cyan(s):
        s.color(36)
        return s
    
    @property
    def white(s):
        s.color(37)
        return s