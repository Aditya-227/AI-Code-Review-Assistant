import os
from radon.complexity import cc_visit


def extract_features(file_path, change_frequency):
    
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    loc = len(code.splitlines())

    complexity = cc_visit(code)
    avg_complexity = 0

    if complexity:
        avg_complexity = sum(c.complexity for c in complexity) / len(complexity)

    features = {
        "file": file_path,
        "lines_of_code": loc,
        "cyclomatic_complexity": avg_complexity,
        "function_count": len(complexity),
        "change_frequency": change_frequency.get(os.path.basename(file_path), 0)
    }

    return features


def extract_repo_features(repo_path, change_frequency):

    repo_features = []

    for root, dirs, files in os.walk(repo_path):

        if "__pycache__" in root:
            continue

        for file in files:

            if file.endswith(".py"):

                path = os.path.join(root, file)

                try:
                    features = extract_features(path, change_frequency)
                    repo_features.append(features)
                except:
                    pass

    return repo_features