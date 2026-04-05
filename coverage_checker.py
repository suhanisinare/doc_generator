def calculate_coverage(functions, classes, file_path):

    with open(file_path, "r") as f:
        code = f.read()

    total_items = len(functions) + len(classes)

    documented = 0

    # Simple check: if docstring exists
    if '"""' in code:
        documented = total_items

    coverage = (documented / total_items) * 100 if total_items > 0 else 0

    return coverage