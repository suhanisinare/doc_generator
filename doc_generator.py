def generate_doc(functions, classes):

    doc = "# Documentation\n\n"

    # Classes
    for cls in classes:
        doc += f"## Class: {cls}\n"
        doc += f"{cls} is a class in the program.\n\n"

    # Functions
    for func in functions:
        doc += f"## Function: {func}\n"
        doc += f"{func} is a function in the program.\n\n"

    doc += "## Example Usage\n"
    doc += "Call the functions with required parameters.\n"

    return doc