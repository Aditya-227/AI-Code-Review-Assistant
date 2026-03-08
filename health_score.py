def calculate_health_score(features, bug_predictions, issues):

    total_files = len(features)

    avg_complexity = sum(f["cyclomatic_complexity"] for f in features) / total_files

    avg_bug_prob = bug_predictions["bug_probability"].mean()

    issue_penalty = len(issues) * 2

    score = 100

    score -= avg_complexity * 3
    score -= avg_bug_prob * 40
    score -= issue_penalty

    if score < 0:
        score = 0

    return round(score, 2)