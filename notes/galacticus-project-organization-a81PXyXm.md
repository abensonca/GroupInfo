# Galacticus Project Organization

###### tags: `git` `GitHub`

The following is a suggested organization/workflow for projects that make use of Galacticus. This centers around using `git` and GitHub to manage the code and your project files.

## Managing the Galacticus Code

The Galacticus codebase is maintained on [GitHub](https://github.com/) - you can find it [here](https://github.com/galacticusorg/galacticus). To begin working with it, the recommended path is as follows:
1. Get a [GitHub account](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account) - you'll want a free Personal account
2. Make a fork (a copy under your own control) of the Galacticus repo following [these instructions](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
3. Clone the repo to where you want to use it (your laptop, `mies`, CaltechHPC etc.)
    1. See [here](https://hackmd.io/ukWn23JaTbaiX_LdQq4Prg?both#Git-and-GitHub) for details on how to set up access to GitHub from `mies` or CaltechHPC
    2. See [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository) for how to clone your repo
4. Create a branch (a separate line of development, distinct from the `master` branch of Galacticus) for your work
    1. A good introduction to branching can be found [here](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
    2. The basic steps needed to create the branch and move onto it are (choose a more descriptive name than "`myNewBranch`"!):
```
git branch myNewBranch
git checkout myNewBranch
```
5. Keep up to date with changes to the main repo
    1. It is good practice to sync changes from the main Galacticus repo into your forked copy on a regular basis
    2. This avoids too much divergence building up which can be difficult to reconcile later
    3. You can sync on GitHub following the instructions [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)
    4. Be sure to then `git pull` to update your copies of your repo on whatever computers/clusters you're using it
6. [Commit](https://github.com/git-guides/git-commit) and push your changes regularly
    1. In general you can do:
```
git add file1 file2.....
git commit -m A good commit message
git push
```
This will add the named files (`file1`, `file2` for commiting), will commit them (Galacticus uses the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary) format for commit messages), and then push those updates to your repo.

## Managing Your Project Files

You should create a separate repo for project files. These will be kept separate from your copy of the Galacticus code - this way if you need to make changes to the Galacticus code it is easy to do so without also adding your project files to the main (public) Galacticus repo.
1. [Create a new repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) (it can, and probably should be private) on GitHub - give it a suitable name for your project
2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the project repo to wherever you need to use it
3. Add project files to it, including things such as Galacticus parameter files
    1. A suggested folder organization would be (but, of course, you can structure this however works best for your project):
        * `parameters/` - for Galacticus parameter files
        * `scripts/` - for simple scripts used to submit jobs to the queue, do analysis, etc.
        * `notes/` - for any notes you make.
    3. Don't add computationally-created files (e.g. Galacticus outputs, plots, etc.) to your repo - it should only contain files created manually (e.g. source code, parameter files, etc.)
4. [Invite](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository) any collaborators to your repo
5. [Commit](https://github.com/git-guides/git-commit) and push your changes regularly
