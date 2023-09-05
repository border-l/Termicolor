class Styles:
    def style(s, style):
        s.val["style", False] = f"\033[{str(style)}m"
        return s
    
    @property
    def bold(s):
        s.style(1)
        return s
    
    @property
    def dim(s):
        s.style(2)
        return s
        
    @property
    def underline(s):
        s.style(4)
        return s
    
    @property
    def blink(s):
        s.style(5)
        return s
    
    @property
    def rapid_blink(s):
        s.style(6)
        return s
    
    @property
    def inverse(s):
        s.style(7)
        return s
    
    @property
    def hidden(s):
        s.style(8)
        return s
    
    @property
    def strikethrough(s):
        s.style(9)
        return s