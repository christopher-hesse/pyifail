from pyifail.ops import func_name, ClassName
from pyifail import ops

def other_func_name() -> None:
    ...

__all__ = ["func_name", "other_func_name", "ClassName", "ops"]