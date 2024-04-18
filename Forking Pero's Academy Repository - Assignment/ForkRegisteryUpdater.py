import os
import requests
import subprocess

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
    return [(fork['owner']['login'], fork['html_url']) for fork in forks]

def update_register(forks):
    with open('REGISTER.md', 'w') as file:
        file.write('# Fork Registry\n\n')
        file.write('| Student Username | Fork URL |\n')
        file.write('|------------------|----------|\n')
        for username, url in forks:
            file.write(f'| {username} | {url} |\n')

def git_commit_and_push():
    # Ensure that changes are only committed if there are changes
    if subprocess.run(['git', 'diff', '--exit-code', 'REGISTER.md']).returncode != 0:
        subprocess.run(['git', 'add', 'REGISTER.md'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Update register'], check=True)
        subprocess.run(['git', 'push', 'origin', 'master'], check=True)
    else:
        print("No changes to commit.")

if __name__ == "__main__":
    forks = get_forks()
    update_register(forks)
    git_commit_and_push()
