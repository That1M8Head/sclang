# Stupidly Concise Language

Stupidly Concise Language (SCLang) is a **conceptual** programming language with extremely concise syntax, borrowing functional programming concepts.

SCLang is inspired mostly by Python and Rust, and to a lesser extent Haskell.

> ⚠️ **Expectation Warning**
>
> SCLang is **only a concept** and is not an actually implemented language.
> Its implementation is a goal for the future.

## Example

```sclang
# `>` prints
> "Hello, SCLang!"

# `print()` also prints
print("Hello, SCLang!")

# immutable and mutable variables
let a (u8) = 5
let mut b (u8) = 4
b += a;
> b

# `_` is used for immediate variables that never get used and are immediately deallocated
x % 2 for _ in ..5:
    > "Wow, that's odd"

# function signatures with no params need no parentheses
fn true:
    true # implicit returns

# inline variables in strings like Python 
> "{true()}"

# you can also do it the Rust way, which only works with `print()`, not `>`
# semicolons are supported but optional
print("{}", true());

# vectors
let list (vector<int>) = [ 1, 2, 3, 4 ]

# func. programming, closures
# `x**` will double x, exponentiation is done with `^` instead
let doubles = list.map(|num| num**)
let squares = list.map(|num| num^2)

# if param `in` is tuple, for loop goes through each
for num in (list, doubles, squares):
    > num
```

This example and other examples are available in the repository this README is in.

## File Attributes

SCLang's file extension will ideally be `.scl`.

I would have decided on `.sc` but it turns out that's already used.

`.sclang` is another option. Maybe even `.stupid`.

## Contribute?

Please. I want to make this real but I have no idea how to actually make a programming language.

If you're interested in making this concept a reality and have expertise in language development, your contributions are welcome.

## License

SCLang will be licensed under GNU LGPL v3.0 when it's actually implemented.

Right now? [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), since it's only conceptual.
