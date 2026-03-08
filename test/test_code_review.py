from code_review import analyze_repository

repo = r"C:\Users\Aditya\Projects\AI_Code_Review_Assistant"

issues = analyze_repository(repo)

for i in issues:
    print(i)