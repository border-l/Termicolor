Termicolor
==========

Termicolor is a package that offers an easy-to-use API for quickly applying colors to text. It is excellent for rapidly creating appropriate styles and allows for extensive reusability.


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

styled_text = f"{ansi('red', 'bold', 'underline')} Hello World! {ansi('reset')}"
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

# There's also a print method (but it doesnt take any parameters):
warn("A print method does indeed exist").print()
```

### Nesting & Adding new text

### Spacing & Padding

### Clear styling

