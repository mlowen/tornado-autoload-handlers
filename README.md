# Autoloading handlers in Tornado

This repository contains the code examples for the article [Autoloading Handlers in Tornado](http://mike.lowen.co.nz/article/2020/02/02/Autoloading-Handlers-in-Tornado/) at [mike.lowen.co.nz](http://mike.lowen.co.nz). The code in this repository shows how you can set up [Tornado](https://www.tornadoweb.org/en/stable/) to automatically load handlers and their routes on application start up.

## Running

Before running you need to ensure that you have [Python 3.x](https://www.python.org/) & [Tornado](https://www.tornadoweb.org/en/stable/#installation) installed. Once the dependencies are installed you can run `python app.py` to run the example. When the example is running you can make a request to either `http://localhost:3000/one` and `http://localhost:3000/one`.

### Running on windows

This example may not work on windows out of the box. If that is the case you need to add the following line:

```python
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```

As the first line in the `if __name__ == '__main__':` block in `app.py`.
