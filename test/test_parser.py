from parser import extract_repo_functions

repo = r"C:\Users\Aditya\Projects\AI_Code_Review_Assistant"

data = extract_repo_functions(repo)

for file, content in data.items():
    print(file)
    print("Functions:", content["functions"])
    print("Classes:", content["classes"])
    print()