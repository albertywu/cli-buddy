## Clibuddy (`cb`) 🤝

A command-line OpenAI-enabled assistant that helps:
- [x] explain errors
- [ ] analyze stack traces (pass the stack trace file content through to the prompt)
- [ ] include better examples
- [ ] give credit to OpenAI; explain how this works, including prompt generation
- [ ] fix bugs
  - [ ] generic fixer
  - [ ] python-optimized fixer
  - [ ] javascript-optimized fixer
  - [ ] typescript-optimized fixer
  - [ ] golang-optimized fixer
- [ ] scaffold tests

## Usage
```
cb --explain -- <cmd> <...cmdArgs>
```

## Examples

#### Explain `git` error
<details>
  <summary>Solution</summary>

  ```sh
❯ cb --explain -- git rebase foo
fatal: invalid upstream 'foo'
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── CliBuddy ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                                                                                                                        │
│  The error message you received indicates that 'foo' is not a valid upstream branch that can be used as a reference for the `git rebase` command. In other words, Git is not able to find the branch 'foo' that you are trying to rebase onto, as it doesn't exist.    │
│                                                                                                                                                                                                                                                                        │
│  To resolve this issue, you may want to first confirm if the branch `foo` exists in your local repository or the remote repository. You can use the command `git branch` to get a list of all local branches or `git branch -r` to get a list of all remote branches.  │
│                                                                                                                                                                                                                                                                        │
│  Once you have confirmed that the branch exists, make sure that you have properly specified the branch name with the correct capitalization and spelling, as `git` is a case-sensitive tool.                                                                           │
│                                                                                                                                                                                                                                                                        │
│  If the branch does not exist or was deleted, you can either recreate it or choose a different upstream branch to rebase onto, depending on your project's requirements.                                                                                               │
│                                                                                                                                                                                                                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

  ```
</details>

#### Explain [git push heroku master](https://stackoverflow.com/questions/4269922/permission-denied-publickey-when-deploying-heroku-code-fatal-the-remote-end) error
<details>
  <summary>Solution</summary>

  ```sh
❯ cb --explain -- git push heroku master
error: src refspec master does not match any
error: failed to push some refs to 'heroku'
─────────────────────────────────────────────────────────────────────── CliBuddy ───────────────────────────────────────────────────────────────────────
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                      │
│  The error message "error: src refspec master does not match any" typically means that Git can't find the branch that you are trying to push to      │
│  Heroku. This usually occurs when you haven't yet committed any changes to your local Git repository, or there is no "master" branch to push.        │
│                                                                                                                                                      │
│  Here are a few steps you can take to resolve the issue:                                                                                             │
│                                                                                                                                                      │
│  1. Check if you have any changes in your local Git repository that can be committed. To do this, run `git status` in your terminal. If there are    │
│  any files that have been modified or added, you may need to commit these changes before pushing to Heroku.                                          │
│                                                                                                                                                      │
│  2. Check if the local Git repository has a branch named "master". To do this, run `git branch` in your terminal. If there isn't a "master" branch,  │
│  you can create one by running `git checkout -b master`.                                                                                             │
│                                                                                                                                                      │
│  3. If you have recently renamed your branch or created a new branch, you may need to specify the branch name in your push command. For example,     │
│  instead of running `git push heroku master`, you could try running `git push heroku new-branch-name`.                                               │
│                                                                                                                                                      │
│  Hopefully, one of these steps will help you resolve the issue and successfully push your changes to Heroku.                                         │
│                                                                                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
  ```
</details>

#### Explain Cannot find module error
<details>
  <summary>Solution</summary>

  ```sh
❯ cb --explain -- node express_error.js
node:internal/modules/cjs/loader:1042
  throw err;
  ^

Error: Cannot find module 'express'
Require stack:
- /Users/wua/Uber/repro/express_error.js
    at Module._resolveFilename (node:internal/modules/cjs/loader:1039:15)
    at Module._load (node:internal/modules/cjs/loader:885:27)
    at Module.require (node:internal/modules/cjs/loader:1105:19)
    at require (node:internal/modules/cjs/helpers:103:18)
    at Object.<anonymous> (/Users/wua/Uber/repro/express_error.js:1:17)
    at Module._compile (node:internal/modules/cjs/loader:1218:14)
    at Module._extensions..js (node:internal/modules/cjs/loader:1272:10)
    at Module.load (node:internal/modules/cjs/loader:1081:32)
    at Module._load (node:internal/modules/cjs/loader:922:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:81:12) {
  code: 'MODULE_NOT_FOUND',
  requireStack: [ '/Users/wua/Uber/repro/express_error.js' ]
}

Node.js v18.13.0
─────────────────────────────────────────────────────────────────────── CliBuddy ───────────────────────────────────────────────────────────────────────
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                      │
│  The error message indicates that the module 'express' was not found when running the script 'express_error.js'. This module appears to be a         │
│  dependency of your script and needs to be installed before it can be used.                                                                          │
│                                                                                                                                                      │
│  To resolve the issue, you can try installing the 'express' module by running the following command in your terminal:                                │
│                                                                                                                                                      │
│  ```                                                                                                                                                 │
│  npm install express                                                                                                                                 │
│  ```                                                                                                                                                 │
│                                                                                                                                                      │
│  This should install the 'express' module and its dependencies, allowing you to run the 'express_error.js' script without encountering the error.    │
│                                                                                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

  ```
</details>

#### Explain `name 'x' is not defined` error
<details>
  <summary>Solution</summary>

  ```sh
❯ cb --explain -- python name_error.py
Traceback (most recent call last):
  File "/Users/wua/Uber/repro/name_error.py", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
─────────────────────────────────────────────────────────────────────── CliBuddy ───────────────────────────────────────────────────────────────────────
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                      │
│  The error message indicates that there is a variable named `x` that was referenced in your script but it has not been defined or assigned a value   │
│  before its usage by the `print` statement. Therefore, your script is attempting to print the value of `x` that does not exist. To resolve this      │
│  error, you should either define the variable `x` before referencing it or assign it a value.                                                        │
│                                                                                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
  ```
</details>

- [ ] Common Problems:
- https://stackoverflow.com/questions/24114676/git-error-failed-to-push-some-refs-to-remote
- https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories-on-rebase
- https://stackoverflow.com/questions/4181861/message-src-refspec-master-does-not-match-any-when-pushing-commits-in-git


---

### Fix Bugs
- [ ] Fix generic bugs
```
cb --fix -- <cmd> <...cmdArgs>
```

## Optimized per-language
- [ ] Fix Python Bugs
```
cb --fix --python -- <cmd> <...cmdArgs>
```

- [ ] Fix Typescript Bugs
```
cb --fix --typescript -- <cmd> <...cmdArgs>
```

- [ ] Fix Golang Bugs
```
cb --fix --typescript -- <cmd> <...cmdArgs>
```

## Examples
- [ ] TODO
