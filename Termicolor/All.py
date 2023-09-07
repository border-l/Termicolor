class All:
    esc = "\033[0m"
    next_key = 1

    def __init__(s, text, back, fore, style, space_b, space_a, pad_b, pad_a, applied):
        s.exclusive_key = f"C[[CLASS_ALL_APPLY_STYLES_HERE_{str(All.next_key)}]]C"
        All.next_key += 1
        s.text = text
        s.back = back
        s.fore = fore
        s.style = style
        s.space_b = space_b
        s.space_a = space_a
        s.pad_b = pad_b
        s.pad_a = pad_a
        s.applied = applied
        s.update()

    def __str__(s):
        return s.all
        
    def __getitem__(s, key):
        return getattr(s, key)
    
    def __setitem__(s, key, value):
        if isinstance(key, tuple): 
            act_key, should_override = key
        else:
            act_key, should_override = key, True
        if act_key == "all" or not hasattr(s, act_key): 
            return
        if should_override:
            setattr(s, act_key, value)
        else:
            setattr(s, act_key, str(getattr(s, act_key)) + str(value))
        s.update()

    def __delitem__(s, key):
        setattr(s, key, "")
    
    def __attr(s):
        return s.back + s.fore + s.style
    
    def attr(s):
        return s.exclusive_key
    
    def copy(s):
        return All(s.text, s.back, s.fore, s.style, s.space_b, s.space_a, s.pad_b, s.pad_a, s.applied)

    def clear(s, text, back, fore, style, space_b, space_a, pad_b, pad_a, applied):
        if text: s.text = ""
        if back: s.back = ""
        if fore: s.fore = ""
        if style: s.style = ""
        if space_b: s.space_b = ""
        if space_a: s.space_a = ""
        if pad_b: s.pad_b = ""
        if pad_a: s.pad_a = ""
        if applied: s.applied = ""
        s.update()
    
    def update(s):
        s.all = (
            str(s.space_b) + 
            str(s.back) + str(s.fore) + str(s.style) + 
            str(s.pad_b) +
            str(s.applied(s.text, s.exclusive_key)).replace(s.exclusive_key, s.__attr()) + 
            str(s.pad_a) +
            str(All.esc) + 
            str(s.space_a)
        )