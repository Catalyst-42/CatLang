# CatLang
A language based on [S-expressions](https://en.wikipedia.org/wiki/S-expression). Written on Python, uses [SLY](https://github.com/dabeaz/sly) library to parse and tokenize code.

To run code install sly:

```shell
pip3 install sly
```

Usage:
```shell
python3 catlang.py <file> [-d]
```

# Features
Implemented:
- Variables
- Output keyword
- Basic math operations
- Basic comparison operators
- If statement
- While statement
- Functions
- Comments

# Examples
### Comments and prints
To comment a line use percent symbol `%`, to print text in console use `out` keyword

```Lisp
% Output text to console
(out "Hello, world!" . "from CatLang")  % Dot means newline
```

### Variables
Variables can be created via assign symbol `=`

```Lisp
(= int 10)
(= float 99.47)
(= str "Hello, world")
(= bool T)  % T means True and F means False

% Let's output this variables
(out 
  "int = " int .
  "float = " float .
  "str = " str .
  "bool = " bool
)
```

### Operators
CatLang supports next math operations:
- `+` to add 
- `-` to sub
- `*` to mul
- `/` to div
- `^` to pow

And some logical operations
- `&` to and
- `|` to or
- `!` to not

Eq operations:
- `=` to assign
- `+=` to add and assign
- `-=` to sub and assign
- `*=` to mul and assign
- `/=` to div and assign

And some comparsion operators:
- `>` to gt
- `>=` to gte
- `<` to lt
- `<=` to lte
- `!=` to ne
- `==` to iseq

All operators must be written in prefix form

```Lisp
(out (+ 1 1))
(out (- 0 4))  % Way to create negative numbers
(out (* 4.5 2))
(out (/ 42 144))
(out (^ 2 4))

(out (! F))  % Negation of False is True

(out (> 1 0))
(out (<= 1.5 3))
(out (!= 1 7))
(out (== 3.0 3))
```

### Statements
CatLang supports only `if` and `while` statements, conditional statements can be executed through `if` keyword

```Lisp
(if (!= 3 4) (
  (out "Well, 3 it's not equal 4")
))

(if (!= (+ 0.1 0.2) 0.3) (
  (out 
    "Wait... what? " .
    "(" (+ 0.1 0.2) ")"
  )
))
```

Cycles may be executed via `while` keyword
```Lisp
(= i 5)
(while (>= i 0) (
  (out i "...")
  (-= i 1)
))
```

### Functions
Functions can be executed with or without one parameter. To define function use `def` keyword

```Lisp
(def say_hi () (
  (out "hi")
))

(say_hi)  % Execute

(def fact (n) (
  (= f 1)
  (while (> n 1) (
    (*= f n)
    (-= n 1)
  ))

  (ret f)  % Return f
))

% 5! = 1 * 2 * 3 * 4 * 5
(out "5! = " (fact 5))
```
