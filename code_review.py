import os
from radon.complexity import cc_visit


def analyze_file(file_path):

    issues = []

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    functions = cc_visit(code)

    for func in functions:

        if func.complexity > 10:
            issues.append({
                "type": "High Complexity",
                "function": func.name,
                "complexity": func.complexity
            })

        if func.endline - func.lineno > 50:
            issues.append({
                "type": "Long Function",
                "function": func.name,
                "length": func.endline - func.lineno
            })

    return issues


def analyze_repository(repo_path):

    results = []

    for root, dirs, files in os.walk(repo_path):

        if "__pycache__" in root:
            continue

        for file in files:

            if file.endswith(".py"):

                path = os.path.join(root, file)

                try:

                    issues = analyze_file(path)

                    for issue in issues:
                        issue["file"] = path
                        results.append(issue)

                except:
                    pass

    return results