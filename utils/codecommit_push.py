import boto3
import os

client = boto3.client('codecommit')

def create_first_commit(repo):
    response = client.create_commit(
    repositoryName=repo,
    branchName='master',
    authorName='python_script',
    email='python_script@mail.com',
    commitMessage='ARGOCD ROLLOUTS POC',
    putFiles=[
            {
                'filePath': "README.md",
                'fileContent': b'README.md foi o primeiro commit, por conta das limita\xc3\xa7\xc3\xb5es da API Boto3 do CodeCommit'
            }
        ]
    )
    print(f" ✅  Successful first commit to: {repo}")

def get_first_commit_id(repo):
    response = client.get_branch(
    repositoryName=repo,
    branchName='master'
    )

    commit_id = response['branch']['commitId']
    return commit_id


def create_commit(repo, file_path):
    for file in os.listdir(file_path):
        print(f" ℹ️  Sending {file} to: {repo}")
        commit_id = get_first_commit_id(repo)
        with open(f"{file_path}/{file}", 'rb') as myfile:
            line = myfile.read()
            response = client.create_commit(
                repositoryName=repo,
                branchName='master',
                parentCommitId=commit_id, 
                authorName='python_script',
                email='python_script@mail.com',
                commitMessage='ARGOCD ROLLOUTS POC',
                putFiles=[
                    {
                        'filePath': file,
                        'fileContent': line
                    }
                ]
            )
            print(f" ✅ Successful to send the {file} to {repo}")


def start(BASE_PATH, APP_PATH):
    REPOSITORY_NAMES = ["flask-app", "flask-app-bluegreen", "flask-app-canary"]
    FILES_PATH = [f"{BASE_PATH}/app", f"{BASE_PATH}/Kubernetes/flask-app-bluegreen", f"{BASE_PATH}/Kubernetes/flask-app-canary"]
    

    for repo, file_path in zip(REPOSITORY_NAMES, FILES_PATH):
        print(f" ℹ️  Sending first commit to: {repo}")
        create_first_commit(repo)
        create_commit(repo, file_path)
    
if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")