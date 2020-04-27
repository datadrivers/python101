from typing import List, Dict, Union


a: List[int] = [1, 2, 3]
b: List[str] = [1, 2, 3]  # funktioniert!


def foo() -> List[str]:
    return [1, 2, 3]  # IDEA meckert!



