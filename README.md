Termicolor
==========

Termicolor is a package that offers an easy-to-use API for quickly applying colors to text. It is excellent for swiftly creating appropriate styles and allows for extensive reusability.

The only dependency is Colorama, to ensure that escape characters work with Windows.

Installation
------------

You can easily install Termicolor using pip

```
pip install Termicolor
```

Usage
-----

Once you have Termicolor installed, it is quite simple to use.

You can import `Color` from Termicolor:

```python
from Termicolor import Color
```

And start using it in your project. Here's a simple demo:

```python
styled_text = Color("Hello, World!").red.bold.underline
other_text = Color("Hello, World, Again.").bg_blue.bold.underline

print(styled_text, other_text)
```

Alternatively, you can import `ansi`, which is more hands-on with styling, but still removes the need to manually type in escape codes:

```python
from Termicolor import ansi

styled_text = f"{ansi('red', 'bold', 'underline')} Hello, World! {ansi('reset')}"
```

Even though Termicolor is very straightforward to get started with, it has many features which will be explained and demonstrated below.

### Supported Colors & Styles

Here is a list of what you can apply to your text using Termicolor:

| **Foreground**     | **Background**      | **Style**                
| ------------------ | ------------------- | ------------------------ 
| **black** `\033[30m`   | **bg_black** `\033[40m` | **reset** `\033[0m`
| **red** `\033[31m`     | **bg_red** `\033[41m`   | **bold** `\033[1m`
| **green** `\033[32m`   | **bg_green** `\033[42m` | **dim** `\033[2m`
| **yellow** `\033[33m`  | **bg_yellow** `\033[43m`| **underline** `\033[4m`
| **blue** `\033[34m`    | **bg_blue** `\033[44m`  | **blink** `\033[5m`
| **magenta** `\033[35m` | **bg_magenta** `\033[45m`| **rapid_blink** `\033[6m`
| **cyan** `\033[36m`    | **bg_cyan** `\033[46m`  | **inverse** `\033[7m`
|                    |                     | **hidden** `\033[8m`
|                    |                     | **strikethrough** `\033[9m`

### Reusing the same styles

Defining reusable styles with Termicolor is convenient and fast.

To do this, you can specify whatever styles you want as usual, omitting passing in a string as this will be used as a base. All you need to do is use the `freeze` method afterwords. This allows you to create new instances of `Color` with exactly the same specifications. Here's an example:

```python
warn = Color().yellow.underline.freeze()
danger = Color().red.bold.freeze()

print(warn("This is some serious text"))
print(danger("This is some even more serious text"))

# There's also a print method (it can take arguments):
warn("Using print method").print()
```

Of course, you can import these styles, allowing you to organize and define them in other files.

### Nesting & Adding new text

Termicolor offers support for nesting, as well as appending and prepending text to what you have already initialized.

There is a few ways you can nest text, but the simplest way to do it is to include it in the constructor of your dominant style:

```python
nested_text = Color("World!").blue
styled_text = Color("Hello,", nested_text).green.bold

print(styled_text)
```

Optionally, you can also nest using the `nest` method.

```python
nested_text = Color("World!").blue
styled_text = Color("Hello,").green.bold.nest(nested_text)
```

Either of these can take several arguments to nest several separate strings.

If you don't want to nest text, but would like to add it on, you can use either the `before` or `after` methods:

```python
after_demo = Color("Hello,").magenta.after("World!")
before_demo = Color("World!").magenta.before("Hello,")

print(after_demo, before_demo)
```

Both of these methods can also nest text, using the same approach.

As a side note, you can delay passing in the text until later, by calling the `Color` instance after your styling:

```python
styled_text = Color().green.bold("Hello, World!")

print(styled_text)
```

Other things to note:
* To add text right after any of these methods, pass in the keyword argument "after" when calling the instance.
* You will notice there's an automatic space added as a separator when nesting or adding additional text, you can override it by passing in false for the "sp_a" keyword argument to either the `after` or `before` method.

### Setting Seperators

To configure the separator space that is automatically placed between added text, the keyword argument "sp" can be set to whatever character or string you want. If no space is desired, set it to an empty string. Here's an example:

```python
styled_text = Color("Hello, ", "World", sp="")

print(styled_text) # Prints "Hello, World" instead of "Hello,  World" with two spaces
```

Additionally, you can remove or set a new separator by using these methods:
* `new_sp`, takes the new separator as an argument
* `remove_sp`, removes the separator

### Spacing & Padding

With Termicolor, you can set spacing which is automatically added before and after but is a part of the styled string, or padding which adds spacing without it being styled. This is a simple demo:

```python
styled_text = Color("Hello, World!").red.pad(4).space(4)

print(styled_text)
```

If you want to only add padding or spacing after/right or before/left using the `pad_a` or `pad_b` method, and `space_b` or `space_a` method.

Note: padding or spacing **does** carry over when using the `freeze` method to reuse a style.

### Clear styling

To clear whatever attributes have been set, you can use the `reset` method to clear everything, or one of these other methods to clear a specific attribute:

* `clear_fore`, `clear_back`, or `clear_style` to clear foreground, background, or text formatting
* `clear_pad`, or `clear_space` to clear padding or spacing
* `clear_text` to clear any text that is set
* `remove_sp` to remove the separator
