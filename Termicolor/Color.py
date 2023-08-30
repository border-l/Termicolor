from .Background import Background
from .Foreground import Foreground
from .Styles import Styles
from .All import All

class Color(Foreground, Background, Styles):
    def __init__(s, text="", *nests, after="", back="", fore="", style="", space_b="", space_a="", padding_l="", padding_r="", applied=lambda x, y: x, ALL=False, sp=" "):
        s.sp = sp
        if isinstance(ALL, All):
            s.val = ALL
        else:
            s.val = All(text, back, fore, style, space_b, space_a, padding_l, padding_r, applied)
        s(s.val["text"], *nests, after=after)

    def __str__(s):
        return s.val["all"]
    
    def __call__(s, text, *nests, after="", sp=True):
        s.val["text"] = text
        s.nest(*nests, sp=sp)
        s.val["text", False] = str(after)
        return s
    
    def __iter__(s):
        return iter(str(s.val["text"]))

    def __add__(s, other):
        new_COLOR = Color(ALL=s.val.copy(), sp=s.sp)
        new_COLOR.after(All.esc + str(other), sp=False)
        return new_COLOR

    def after(s, string, *nests, after="", sp=True):
        s.val["text", False] = s.sp*sp + str(string)
        s.nest(*nests)
        s.val["text", False] = str(after)
        return s
    
    def before(s, string, *nests, after="", sp=True):
        original = s.sp*sp + s.val["text"]
        s.val["text"] = string
        s.nest(*nests)
        s.val["text", False] = str(after) + original
        return s
    
    def nest(s, *nests, sp=True):
        nested = ""
        for nest in nests:
            nested += s.sp*sp + s.__nest(nest)
        if len(nested) > 0:
            s.val["text"] += nested + str(All.esc) + s.val.attr()
        return s
    
    def __nest(s, string):
        new_text = str(All.esc) + str(string)
        return new_text
    
    def space(s, spaces, before=False, after=True, clear=True):
        if before: s.val['space_b', clear] = spaces * " "
        if after: s.val['space_a', clear] = spaces * " "
        return s
    
    def space_b(s, spaces, clear=True):
        s.space(spaces, before=True, after=False, clear=clear)
        return s
    
    def space_a(s, spaces, clear=True):
        s.space(spaces, before=True, after=False, clear=clear)
        return s
    
    def padding(s, spaces, left=True, right=True, clear=True):
        if left: s.val["padding_l", clear] = spaces * " "
        if right: s.val["padding_r", clear] = spaces * " "
        return s
    
    def padding_l(s, spaces, clear=True):
        s.padding(spaces, right=False, clear=clear)

    def padding_r(s, spaces, clear=True):
        s.padding(spaces, left=False, clear=clear)

    def clear(s, text=False, back=False, fore=False, style=False, space_b=False, space_a=False, padding_l=False, padding_r=False, applied=False):
        s.val.clear(text, back, fore, style, space_b, space_a, padding_l, padding_r)
        return s
    
    def clear_space(s, b=True, a=True):
        if b: s.clear(space_b=True)
        if a: s.clear(space_a=True)
        return s
    
    def clear_padding(s, l=True, r=True):
        if l: s.clear(padding_l=True)
        if r: s.clear(padding_r=True)
        return s
    
    def clear_text(s):
        s.clear(text=True)
        return s
    
    def clear_back(s):
        s.clear(back=True)
        return s

    def clear_fore(s):
        s.clear(fore=True)
        return s
    
    def clear_applied(s):
        s.clear(applied=True)
    
    def clear_style(s):
        s.clear(style=True)
        return s

    def new_sp(s, text):
        s.sp = text
        return s
    
    def remove_sp(s):
        s.sp = ""
        return s
    
    def reset(s):
        s.val.clear(True, True, True, True, True, True, True, True, True)
        return s

    def new(s, new_text="", text=False, back=True, fore=True, style=True, space_b=True, space_a=True, padding_l=True, padding_r=True):
        all = All(s.val["text"] if text else new_text,
            s.val["back"] if back else "",
            s.val["fore"] if fore else "",
            s.val["style"] if style else "",
            s.val["space_b"] if space_b else "",
            s.val["space_a"] if space_a else "",
            s.val["padding_l"] if padding_l else "",
            s.val["padding_r"] if padding_r else "")
        return Color(ALL=all)
    
    def apply(s, func):
        s.val["applied"] = func
        return s
    
    def print(s, *args):
        print(s.val["all"], *args)

    @property
    def ansi(s):
        return s.val["back"] + s.val["fore"] + s.val["style"]
    
    def freeze(s):
        return Static(s.val.copy(), s.sp)
    
    @property
    def text(s):
        return s.val["text"]

class Static:
    def __init__(s, all, sp):
        s.val = all
        s.sp = sp
    
    def __str__(s):
        return ""
        
    def __call__(s, text):
        s.val["text"] = text
        return Color(ALL=s.val.copy(), sp=s.sp)