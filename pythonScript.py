import subprocess

def run_command(command):
    """Runs a shell command and returns the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "Error running command"

print("===== Local Git Context =====")

# Get all branches with their latest commit
print("\nBranches and Latest Commits:")
branches = run_command("git branch -a").split("\n")
for branch in branches:
    branch_name = branch.strip().replace("* ", "")  # Remove '*' from current branch
    latest_commit = run_command(f"git log -1 --oneline {branch_name}")
    print(f"- {branch_name}: {latest_commit}")

# Check for uncommitted changes
uncommitted_changes = run_command("git status --porcelain")
print(f"\nUncommitted Changes: {'Yes' if uncommitted_changes else 'No'}")

# Get remote repository information
print("\nRemote Repositories:")
print(run_command("git remote -v"))

# Get working directory status
print("\nWorking Directory Status:")
print(run_command("git status --short"))

# Get recent commit history for all branches
print("\nRecent Commits for Each Branch:")
for branch in branches:
    branch_name = branch.strip().replace("* ", "")
    print(f"\nBranch: {branch_name}")
    print(run_command(f"git log --oneline -n 5 {branch_name}"))

# Get staged changes
print("\nStaged Changes:")
print(run_command("git diff --staged"))

# Get uncommitted changes
print("\nUncommitted Changes (Detailed):")
print(run_command("git diff"))
