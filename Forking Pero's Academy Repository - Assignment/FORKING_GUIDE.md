# Guide to Forking Pero's Academy Repository

## Step 1: Navigate to the Repository
- Go to the URL: [Pero's Academy Assignments Repo](https://github.com/Pero-s-Academy/Assignments)

## Step 2: Fork the Repository
- Click on the "Fork" button at the top right corner of the page. This will create a copy of the repository in your GitHub account.

## Step 3: Clone Your Fork
- After forking, go to your GitHub profile, navigate to "Your repositories," find the forked repository, and clone it to your local machine using the provided Git command.

## Step 4: Set Upstream Remote
- Set the original Pero's Academy repository as an upstream remote to sync changes made in the main repository with your fork.

``` bash
git remote add upstream https://github.com/Pero-s-Academy/Assignments.git
```

## Step 5: Sync Your Fork
- Fetch the latest updates from the upstream and merge them into your local repository.

``` bash
git fetch upstream
git merge upstream/main main
```

## Step 6: Push Changes
- Push the changes to your fork on GitHub.

``` bash
git push origin main
```

## Conclusion
Follow these steps to maintain an up-to-date fork of the Pero's Academy Assignments Repository. Keep experimenting and exploring Git and GitHub functionalities as you progress with your assignments.
