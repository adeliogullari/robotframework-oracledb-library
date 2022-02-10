from typing import Dict, Any


class ArgumentMapper:

    def __init__(self):
        pass

    @staticmethod
    def map_argument(source: Dict, target: Any) -> None:
        target_vars = vars(target)
        for key, value in source.items():
            if value in target_vars:
                source.update({key: target_vars.get(value)})

