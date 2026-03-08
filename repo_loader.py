import os
from git import Repo
import pandas as pd


def load_repository(repo_path):
    """
    Load git repository and return repo object
    """
    repo = Repo(repo_path)

    if repo.bare:
        raise Exception("Invalid Git Repository")

    return repo


def get_commit_history(repo):
    """
    Extract commit history
    """
    commits = list(repo.iter_commits())

    data = []

    for commit in commits:
        for file in commit.stats.files:
            data.append({
                "file": file,
                "insertions": commit.stats.files[file]["insertions"],
                "deletions": commit.stats.files[file]["deletions"],
                "changes": commit.stats.files[file]["lines"]
            })

    df = pd.DataFrame(data)

    return df


def get_file_change_frequency(repo):
    """
    Count how frequently each file changes
    """
    commits = list(repo.iter_commits())

    change_count = {}

    for commit in commits:
        for file in commit.stats.files:
            if file not in change_count:
                change_count[file] = 0
            change_count[file] += 1

    return change_count