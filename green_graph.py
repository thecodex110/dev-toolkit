#!/usr/bin/env python3
import subprocess
import random
from datetime import datetime, timedelta
import os
import sys

COMMIT_MESSAGES = [
    "feat: add slugify utility for string formatting",
    "refactor: optimize LRU Cache eviction performance",
    "fix: handle edge cases in string truncation",
    "test: add unit test coverage for string_utils",
    "docs: update API documentation in README",
    "chore: clean up internal module imports",
    "perf: optimize memory footprint of data structures",
    "feat: implement Trie data structure for prefix searching",
    "refactor: extract helper methods in algorithms module",
    "fix: resolve potential key error in cache lookup",
    "test: add benchmark tests for algorithmic helpers",
    "docs: add docstrings and typing annotations",
    "chore: update linting rules and code formatting",
    "feat: add binary search utility for sorted arrays",
    "refactor: simplify conditional logic in string parser",
    "fix: correct boundary conditions in segment tree",
    "test: expand test suite for edge case handling",
    "docs: improve usage examples for quick start guide",
    "chore: update dependencies and version bump",
    "perf: reduce execution time of array chunking",
    "feat: add matrix transformation functions",
    "refactor: modularize data structures module",
    "fix: address minor type checker warnings",
    "test: assert immutability of returned data chunks"
]

def make_commit(date_str, count):
    """Make commits with specified date and realistic messages."""
    for i in range(count):
        hour = random.randint(8, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        timestamp = f"{date_str} {hour:02d}:{minute:02d}:{second:02d}"
        
        msg = random.choice(COMMIT_MESSAGES)
        
        with open("dev_toolkit/changelog.txt", "a") as f:
            f.write(f"[{timestamp}] {msg}\n")
            
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = timestamp
        env["GIT_COMMITTER_DATE"] = timestamp
        env["GIT_CONFIG_GLOBAL"] = "/dev/null"
        
        subprocess.run(["git", "add", "dev_toolkit/changelog.txt"], check=True, env=env, stdout=subprocess.DEVNULL)
        subprocess.run(
            ["git", "commit", "-m", msg],
            check=True,
            env=env,
            stdout=subprocess.DEVNULL
        )

def main():
    days = 365
    if len(sys.argv) > 1:
        try:
            days = int(sys.argv[1])
        except ValueError:
            pass
            
    print(f"Generating custom commit history (30% Dark Green > 25 commits)...")
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    current_date = start_date
    total_commits = 0
    dark_green_days = 0
    
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        
        # User requirement:
        # 30% Dark Green days: > 25 commits per day (26 - 35 commits)
        # 40% Medium/Bright Green days: 8 - 20 commits per day
        # 30% Light/Medium Green days: 3 - 7 commits per day
        rand_val = random.random()
        if rand_val < 0.30:
            commits_today = random.randint(26, 35)
            dark_green_days += 1
        elif rand_val < 0.70:
            commits_today = random.randint(8, 20)
        else:
            commits_today = random.randint(3, 7)
            
        make_commit(date_str, commits_today)
        total_commits += commits_today
        current_date += timedelta(days=1)
        
    print(f"Success! Generated {total_commits} commits across {days} days ({dark_green_days} days with >25 commits).")

if __name__ == "__main__":
    main()
