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

## Examples

`>` is a macro that uses Soel's underlying `println()` function.

```soel
> "Hello, Soel!"
```

`println()` can be called directly, too.

```soel
println("Hello, Soel!")
```

Variables are immutable by default, like in Rust.

```soel
let a (u8) = 5
let mut b (u8) = 4
b += a;
> b
```

For loops are a lot more concise when you only need it to work in specific conditions (for example, only print if the current number, divided by 2, has a remainder, i.e. is odd)

`_` is used for immediate variables that never get used, and are immediately
deallocated.

```soel
x % 2 for _ in ..5:
    > "Wow, that's odd"
```

When defining a function, the function signature doesn't need brackets
(parentheses) if it takes no parameters.

```soel
fn true:
    true # implicit returns
```

Variables inside strings work like Python's f-strings without the `f`.

```soel
> "{true()}"
```

You can also do it similarly to Rust, although this doesn't work with the `>`
macro.

Semi-colons are supported, but they're optional like JavaScript.

```soel
println("{}", true());
```

Rust-like vectors are supported.

```soel
let list (vector<int>) = [ 1, 2, 3, 4 ]
```

Functional programming concepts, as discussed earlier, are supported,
including the `map()` higher-order function and closures.

`x**` will double x, exponentiation is done with `^` instead.

```soel
let doubles = list.map(|num| num**)
let squares = list.map(|num| num^2)
```

For loops support iterating through each element in a list or tuple.

```soel
for num in (list, doubles, squares):
    > num
```

The full source file and other examples are available in the repository this
README is in.

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
