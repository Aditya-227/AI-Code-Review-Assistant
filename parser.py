import ast
import os


def parse_python_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    try:
        tree = ast.parse(code)
    except Exception as e:
        print("Parse error in:", file_path, e)
        return {"functions": [], "classes": []}

    functions = []
    classes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        if isinstance(node, ast.ClassDef):
            classes.append(node.name)

    return {
        "functions": functions,
        "classes": classes
    }


def extract_repo_functions(repo_path):
    results = {}

    for root, dirs, files in os.walk(repo_path):
        if "__pycache__" in root:
            continue

        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)

                parsed = parse_python_file(path)
                results[path] = parsed

    return results