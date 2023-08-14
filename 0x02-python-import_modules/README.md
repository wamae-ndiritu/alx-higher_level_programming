# Import Modules


## Importing modules

When importing a module, the code maybe executed or not. We can write python code that can be used as both a `standalone script` and as a `module` that can be imported into other scripts.

### Standalone Script Execution

> When you run a python script directly from the command line, the special variable `__name__` is set to `__main__`. This indicates that the script is the main program being executed.

### Imported Module Execution

> When you import a Python script as a module into another script, the special variable `__name__` is set tot the name of the module. This indicate that the script is being imported as a module, rather than being executed directly.

### Preventing code from being executed when imported

Checking `if __name__ == "__main__"` allows as to differentiate between a standalone script and an imported module. Any code within this block will only be executed when the script is run directly, not when it's imported as a module.
