class Background:
    def bg_color(s, color):
        if color < 40 or color > 47: return
        s.val["back"] = f"\033[{str(color)}m"
        return s

    @property
    def bg_black(s):
        s.bg_color(40)
        return s
    
    @property
    def bg_red(s):
        s.bg_color(41)
        return s
    
    @property
    def bg_green(s):
        s.bg_color(42)
        return s

    @property
    def bg_yellow(s):
        s.bg_color(43)
        return s

    @property
    def bg_blue(s):
        s.bg_color(44)
        return s

    @property
    def bg_magenta(s):
        s.bg_color(45)
        return s

    @property
    def bg_cyan(s):
        s.bg_color(46)
        return s

    @property
    def bg_white(s):
        s.bg_color(47)
        return s
