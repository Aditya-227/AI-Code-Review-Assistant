from repo_loader import load_repository, get_file_change_frequency

repo = load_repository(r"C:\Users\Aditya\Projects\AI_Code_Review_Assistant")

freq = get_file_change_frequency(repo)

print(freq)