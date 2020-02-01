from os import listdir
from os.path import dirname, realpath, splitext
from importlib import import_module

ROUTES = []

if not __name__.endswith("__init__"):
    FILES = listdir(dirname(realpath(__file__)))

    for name, extension in [splitext(f) for f in FILES if f != __file__]:
        if extension != ".py":
            continue

        mod = import_module("{0}.{1}".format(__name__, name))
        route = getattr(mod, "ROUTE", None)

        if route is not None and isinstance(route, tuple):
            ROUTES.append(route)
