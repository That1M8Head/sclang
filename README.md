# Soel

Soel is a **conceptual** programming language that's stupidly concise and is a
programming language. (or, it will be)

Soel features an extremely concise syntax, borrowing concepts from functional
programming.

Soel is inspired mostly by Python and Rust, and to a lesser extent Haskell.

Soel is not a purely functional programming language, in fact, it has more in
common with Rust than with Haskell, but it has full support for functional
programming concepts.

(Or, well, it *will*.)

> ⚠️ **Expectation Warning**
>
> Soel is **only a concept** and is not an actually implemented language.
> Its implementation is a goal for the future.

## Example

```soel
# `>` prints
> "Hello, Soel!"

# `print()` also prints
print("Hello, Soel!")

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

This example and other examples are available in the repository this README is
in.

## Where the name comes from

It's a portmanteau of "something" and "else", because the language sure is
something else.

Also, you pronounce it `/sōl/`, like the word "soul".

## File Attributes

Soel's file extension will ideally be `.soel`.

There are other options, probably, but I can't think of any right now.

## Contribute?

Please. I want to make this real but I have no idea how to actually make a
programming language.

If you're interested in making this concept a reality and have expertise in
language development, your contributions are welcome.

## License

Soel will be licensed under GNU LGPL v3.0 when it's actually implemented.

Right now? [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/),
since it's only conceptual.
