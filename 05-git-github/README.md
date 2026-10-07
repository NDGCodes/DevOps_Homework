# Git and GitHub

This section covers Git commit behavior and cherry-pick practice.

## Commit Practice

### Difference

- `git commit -m` commits staged files.
- `git commit -a -m` stages changed tracked files, then commits them.
- `-a` does not add new files.

### Result

```text
?? untracked.txt
The new file is not committed by git commit -a -m.
```

### Evidence

![Git commit output](commit-practice/git-commit-a_24bcs10451.png)

## Cherry-Pick Practice

`git cherry-pick` copies one commit to the current branch.

The script makes:

- Three commits on `main`
- Three commits on `feature`
- One cherry-pick from `feature` to `main`

### Result

The chosen `add picked feature` commit was copied to `main`. The other feature
commits stayed on the `feature` branch.

### Evidence

![Git cherry-pick output](cherry-pick-practice/git-cherry-pick_24bcs10451.png)
