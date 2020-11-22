# seo-git-hooks

✅ Simple git pre-commit hooks to check if your Static Website follows the rules describe [here](https://andreffs.com/blog/seo-tips/).


## Install

You can run the following one liner on your project's root folder to install this pre-commit hook:

```shell
$ curl -fsSL https://raw.githubusercontent.com/andreffs18/seo-git-hooks/master/pre-commit >> .git/hooks/pre-commit && curl -fsSL https://raw.githubusercontent.com/andreffs18/seo-git-hooks/master/seo-pre-commit.py > .git/hooks/seo-pre-commit.py

```


This simply:
* Appends to your `.git/hooks/pre-commit` file the content of this `pre-commit` hook
* Downloads `seo-pre-commit.py` bash script and stores it on you projects ".git/hooks/" folder
