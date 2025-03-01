#!/bin/bash

echo "===== Local Git Context ====="

# Get current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)
echo "Current Branch: $current_branch"

# Get latest commit
latest_commit=$(git log -1 --oneline)
echo "Latest Commit: $latest_commit"

# Check for uncommitted changes
uncommitted_changes=$(git status --porcelain | wc -l)
if [ "$uncommitted_changes" -gt 0 ]; then
    echo "Uncommitted Changes: Yes"
else
    echo "Uncommitted Changes: No"
fi

# Get remote repository information
echo "Remote Repositories:"
git remote -v

# Get working directory status
echo "Working Directory Status:"
git status --short

# Get recent commit history
echo "Recent Commit History:"
git log --oneline -n 5

# Get staged changes
echo "Staged Changes:"
git diff --staged

# Get uncommitted changes
echo "Uncommitted Changes (Detailed):"
git diff
