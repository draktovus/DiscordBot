# Discord Bot

My discord bot.

I am learning how to use github, python, and the discord API in order to make the bot.

## Pip and Virtual Environments

[Stackoverflow page.](https://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repository)

[pip documentation](https://pip.pypa.io/en/stable/reference/pip/)

It is not neccessary to store the entire virtual environment. Instead, it is better to just make and install what is needed.

```virtualenv .env && source .env/bin/activate && pip install -r requirements.txt```

## Github: Enforcing .gitignore on previously not ignored things

[Stackoverflow page.](https://stackoverflow.com/questions/25436312/gitignore-not-working)

It is important to note that before doing this, git add and git commit any changes made.

```md
git rm -rf --cached .
git add .
```
