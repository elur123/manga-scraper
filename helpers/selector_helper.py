import importlib

def get_selector(source_name: str):
    try:
        module = importlib.import_module(f"json_selectors.{source_name}.index")
        # Convention: class name is capitalized source + Selector
        class_name = f"{source_name.capitalize()}Selector"
        selector_class = getattr(module, class_name)
        return selector_class()
    except (ModuleNotFoundError, AttributeError) as e:
        raise ValueError(f"Invalid source: {source_name}") from e