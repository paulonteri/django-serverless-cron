import importlib
from typing import Dict


def run_function_from_path(function_path: str, kwargs: Dict):
    """
    Runs a function given its path
    ...
    Parameters
    ----------
    function_path: str
        the path to the function to be executed
    kwargs: Dict
        kwargs passed to to the function to be executed
    """

    module_name, function_name = function_path.rsplit('.', 1)
    module = importlib.import_module(module_name)

    task = getattr(module, function_name)

    return task(**kwargs)
