import os
import requests # type: ignore
import subprocess

def check_git_repository():
    try:
        subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], check=True, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError:
        raise EnvironmentError("This directory is not a Git repository.")

def get_forks():
    # Fetch the GitHub token from the environment variable
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
    
    url = "https://api.github.com/repos/Pero-s-Academy/Assignments/forks"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code} {response.reason}")
    
    forks = response.json()
    # Include the creation date in the return value
    return [(fork['owner']['login'], fork['html_url'], fork['created_at']) for fork in forks]

def update_register(forks):
    with open('REGISTER.md', 'w') as file:
        file.write('# Fork Registry\n\n')
        file.write('| Student Username | Fork URL | Date Created |\n')
        file.write('|------------------|----------|--------------|\n')
        for username, url, created_at in forks:
            # Format the date to only show YYYY-MM-DD
            date_created = created_at.split("T")[0]  # Splits the datetime and takes only the date part
            file.write(f'| {username} | {url} | {date_created} |\n')

def git_commit_and_push():
    # Ensure that changes are only committed if there are changes
    if subprocess.run(['git', 'diff', '--exit-code', 'REGISTER.md']).returncode != 0:
        subprocess.run(['git', 'add', 'REGISTER.md'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Update register'], check=True)
        subprocess.run(['git', 'push', 'origin', 'master'], check=True)
    else:
        print("No changes to commit.")

if __name__ == "__main__":
    os.chdir("c:/Users/RaydoMatthee/Documents/GitRepositories/Assignments/Forking Pero's Academy Repository - Assignment")  # Ensure correct directory
    check_git_repository()  # Check if the directory is a Git repository
    forks = get_forks()
    update_register(forks)
    git_commit_and_push()
