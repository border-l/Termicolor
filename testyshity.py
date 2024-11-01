from .src.Termicolor import Color

# Basic usage with chaining
styled_text = Color("Hello, World!").red.bold.underline
other_text = Color("Hello, World, Again.").bg_blue.bold.underline

print(styled_text)
print(other_text)

# Using the ansi function

# Reusable styles with freeze
warn = Color().yellow.underline.freeze()
danger = Color().red.bold.freeze()

print(warn("This is some serious text"))
print(danger("This is some even more serious text"))

# Using print method
warn("Using print method").print()

# Nesting text
nested_text = Color("World!").blue
styled_text_nested = Color("Hello,", nested_text).green.bold
print(styled_text_nested)

# Adding text with before and after
after_demo = Color("Hello,").magenta.after("World!")
before_demo = Color("World!").magenta.before("Hello,")
print(after_demo)
print(before_demo)

# Spacing and padding
styled_text_spacing = Color("Hello, World!").red.pad(4).space(4)
print(styled_text_spacing)

# Clear styling
clear_text = Color("This is colorful").red.bold
clear_text.reset()

# Custom separator
custom_sep_text = Color("Hello,", "World", sp="-")
print(custom_sep_text)
print(custom_sep_text * 5)
