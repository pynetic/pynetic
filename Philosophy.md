<p align="center">
  <a href="https://github.com/Jabbey92/PyNetic">
    <img height="300" src="assets/icon.svg">
  </a>
</p>

# ❓What is PyNetic?

### 🍃 A fresh take on a frontend framework

PyNetic aims to be on modern frontend framework. Focusing on simplicity and modularity, utilizing the Python language to eliminate the need for extra boilerplate code or confusion in the development process.

### 🛩️ Reactivity should be easy

- Variable binding should be implicit, not explicit
  - Instead of explicitly binding a variable to a component and having a wrapper function be the means to causing effects within the dom, a variable should trigger an effect wherever it is used automatically.
  - To be put in other terms, Variables should act like normal variables, only they cause reactivity. This just makes sense.
- All variables can be accessed at runtime
  - All variables are defined in global scope at runtime
  - Access to a variable will subscribe the accessor to changes in that variable

### 📦 Only necessary code is sent to the client

- this means:
  - no comments
  - no type hints
  - Code should be minified as much as possible without losing the original meaning

### 🖨️ A Frontend Framework written in Python that compiles to HTML, CSS, JS and/or lean Python code that can be sent to the browser

PyNetic will either need to be compiled to JavaScript, or package a Python runtime to the client.

- <b>JavaScript should not be the de-facto</b>
  - Until very recently, JavaScript has been the only kid on the block
    - <ins>Insert: WASM!</ins> With WASM any language can be compiled for the browser
      - <ins>**[Pyodide](https://pyodide.org/en/stable/)**</ins> - Python runtime compiled for use in the browser
      - While still in development, this allows for python code to be ran in the browser as if it was natively supported
        - Automatically cached
          - On first load of the page the Pyodide runtime is saved into browser cache. Every other time the page is loaded only the Python environment needs to spin-up
    - <ins>**[Brython]()**</ins>
    - The ultimate goal would be that Python be supported by browsers as JavaScript is now. (this is just a pipe dream)

# ❗What PyNetic <ins>IS NOT</ins>

### 🍼 PyNetic is not a frontend framework made for beginners

Although it is still easy for beginners to pick up!

- You still need an understanding of HTML and CSS
- PyNetic should be a sigh of relief for people who have worked with JavaScript frameworks
  - Especially if you already know python
-

# 🤷Why Python?

<details>
<summary>
🔋<b>Batteries</b>
</summary>

Javascript is a great tool, but it is not _"batteries-included"_.

_Batteries being standard functions or implementations of common functions that are already built into the language itself_

<ins>Consider the following:</ins>

> You have an iterable or array of numbers that you want to get the sum of:

### Summing in JavaScript,

You would need to implement this yourself.
Starting off, just a search for "js sum array" in the browser gives many different implementations of this.
The top rated answer (at the time of writing this) looks as follows:

```js
const sum = nums.reduce((partialSum, a) => partialSum + a, 0);
```

<sup>Reference [^1]</sup>

This can cause confusion, as one frameworks or one developer's way of summing an array can easily be
completely different from another's.

### Summing in Python,

This functionality is already builtin to the language as part of the standard library.
Therefore, the code for producing the sum of an array (`list` in python) is already done for you.
There is no need to lookup how something as trivial as a sum of an array is performed because it's already
documented in the python documentation and will always produce the same output

```py
sum(nums)
```

<sup>Reference [^2]</sup>

This means you as the developer do not need to send to the client your code to the client
because it's already done for you.

</details>

---

# 🔀 What language is sent to the client?

### In short, <ins>Python</ins>.

Although there will be means to include JavaScript into the bundle, and means to transpile Python to JavaScript wherever possible.

- Javascript translation should be something the developer opt's into to send to the client.
- If the developer wants to send JavaScript to the client then it should be explicitly written as JavaScript, or requested from PyNetic, by the developer, to transpile the desired python code to JavaScript.
- PyNetic should be runtime-invariant
  - Currently the vision is to have Pyodide be the supported runtime.
  - As time goes on, Pyodide will have improvements, or a new runtime may come out. PyNetic should be expected to be able to run on any Python environment (given the environment supports cPython code)

# 🛠️ ️How does PyNetic work?

## Session (Application)

- Represents the entire client session.
  - It is the global scope of the dom.
  - All References (States in React) (Variables in Svelte) will be defined globally for all to use
  - All tick/interval based events are emitted from Session.

## References (Variables)

- Maintain their state for the entirety of the client-session
- When created they are automatically added to Session at runtime
  using the file path as the key
- Wherever used, the calling component is bound to the Reference

## Events

- (Like References) Event functions are defined at local scope at runtime therefore if a function applies to 2 or more events, they can be imported and used wherever needed.

[^1]: https://stackoverflow.com/questions/1230233/how-to-find-the-sum-of-an-array-of-numbers

[^2]: https://stackoverflow.com/questions/4362586/sum-a-list-of-numbers-in-python
