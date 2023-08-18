# PyScript Demo
A minimalist and realistic project showing a web application using [PyScript](https://pyscript.net) with matplotlib.  
A short presentation of PyScript is available on the [wiki](https://github.com/peracine/PyscriptDemo/wiki) page.

## Development
PyScript does not require any special setups. Any IDEs supporting HTML, Javascript and Python will help the coding experience. A local server 'localhost' is required to run the application properly on the development machine.  
A 'Hello, world!' example is available on this page [Getting started with PyScript](https://docs.pyscript.net/latest/tutorials/getting-started.html).

## Testing
Any testing framework should work but the PyScript team uses internaly Jest and Pytest (with Playwright).  
Pytest and Playwright will be used too in this project and the following packages will be required:
```cmd
pip install -U playwright
pip install -U pytest
pip install -U pytest-asyncio
pip install -U pytest-playwright
```
PS: some modules are available only as PIP package.  

All tests in this repo are written only in Python (3.9). [More info about Pytest and Playwright installation](https://playwright.dev/python/docs/intro).