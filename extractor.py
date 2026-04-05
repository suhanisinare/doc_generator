import ast

def extract_info(file_path):
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    functions = []
    classes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

    return functions, classes