# Git Cheatsheet
``` bash
# change default editor from vim to nano
git config —global core.editor "nano"
# use git to track the directory
git init
# add file to staging area
git add
# add all file to staging area
git add —all
# add file to local repo with comments
git commit -m “”
# commit file directly without staging, limited to existing files
git commit -a -m
# show commit log message
git log
# remove file and add to staging
git rm 
# make file untracked
git rm <file> —cached
# rename file and add to staging
git mv <file> <new file name>
# edit the last commit comments
git commit —amend -m “”
# ignore file settings
.gitignore
# clean ignored files
git clean -fX
# show commit change of a file
git log <file name>
# show detailed commit change of a file
git log -p <file name>
# show change log of a file
git blame <file>
git annotate
# 
git checkout 
# reset master to previous commit version
git reset master^
git reset HEAD^
# reset master to certain commit version
git reset <commit index>
# git reset common argument
git reset --mixed
git reset --soft
git reset --hard 
```
模式|mixed模式(預設)|soft模式|hard模式
---|---|---|---
Commit 拆出來的檔案|丟回工作目錄|丟回暫存區|直接丟掉
``` bash
# show head change log
git reflog
git log -g
# reset reset
git reset <commit index> —hard
# show all branch
git branch
# switch to another branch
git checkout <branch_name>
# staging a part of file(use UI would be easier)
git add -p 
e
# add new branch
git branch <branch_name>
# switch to other branch
git checkout <branch_name>
# rename branch
git branch -m <ori_name> <new_name>
# delete branch 
git branch -d <branch_name>
# force delete branch
git branch -D <branch_name>
# switch to other branch, if not exists, create one.
git checkout -b <branch_name> 
# merge branch into current branch
git merge <branch_name> 
# assign certain commit a branch
git branch <branch_name> <commit index>
# base current branch(changes) on another branch
git rebase <branch_name>
# reset 
git reset ORIG_HEAD —hard
or
git reset <commit index> —hard
# resolve merge conflict
edit file 
git commit -m ""
# resolve rebase conflict
edit file 
git rebase —continue
# resolve conflicted non-text file using current branch’s file
git checkout —ours <file name> 
# resolve conflicted non-text file using merging branch’s file
git checkout —theirs <file name> 
# switch to specific commit
git checkout <commit index>
# switch to specific commit and create a new branch
git checkout -b <branch name> <commit index>
# assign new branch on specific commit
git branch <branch name> <commit index>
# enter interactive mode to modify previous commit history
git rebase -i <commit index>
pick: remain
reword: edit message
squash: merge commit
edit:
drop
# submit a new commit to cancel the last commit 
git revert HEAD —no-edit
```

- comparison of three modification command
指令|改變歷史紀錄|說明
---|:--------:|---
Reset|是|把目前的狀態設定成某個指定的 Commit 的狀態，通常適用於尚未推出去的 Commit。
Rebase|是|不管是新增、修改、刪除 Commit 都相當方便，用來整理、編輯還沒有推出去的 Commit 相當方便，但通常也只適用於尚未推出去的 Commit。
Revert|否|新增一個 Commit 來反轉（或說取消）另一個 Commit 的內容，原本的 Commit 依舊還是會保留在歷史紀錄中。雖然會因此而增加 Commit 數，但通常比較適用於已經推出去的 Commit，或是不允許使用 Reset 或 Rebase 之修改歷史紀錄的指令的場合。
``` bash
# add lightweight tag to specific commit
git tag <tag name> <commit index>
# add annotated tag to specific commit
git tag <tag name> <commit index> -a -m “”
# show tag info
git show <tag name>
# delete tag
git tag -d <tag name>
# comparison between tag and branch
branch will follow the commit, while tag remain in the same commit where it was attached
# save working dir state (not applicable to untracked files)
git stash
# show stash WIP(work in progress)
git stash list
# fetch stash, apply it into current branch and drop stash record
git stash pop <stash index>
# drop/discard stash
git stash drop <stash index>
# fetch stash, apply it into current branch and keep the record in stash list
git stash apply <stash index>
# switch to each commit and execute command by specific filter
git filter-branch --tree-filter <command>
# switch to each commit and remove file
git filter-branch --tree-filter "rm -f <file name>"
# reset filter-branch
git reset refs/original/refs/heads/<branch name> --hard
# copy specific commit and merge into current branch
git cherry-pick <commit index> [<commit index> <commit index>]
# copy specific commit and put it into current branch’s staging area
git cherry-pick <commit index> —no-commit
# switch to each commit and remove file and overwrite backup info
git filter-branch -f --tree-filter "rm -f <file name>"
# clear reflog message(reflog default keep 30 days record)
git reflog expire --all --expire=now
# show unreachable objects
git fsck --unreachable
# activate garbage collection
git gc --prune=now
# set remote repo endpoint
git remote add origin <endpoint path or ssh syntax>
                     (nickname)
# push local repo on remote repo
git push -u origin <branch name>
# fetch remote repo to local repo
git fetch
# pull(fetch and merge) remote repo to local repo
git pull
# pull(fetch and merge) remote repo to local repo without generating another commit for merging
git pull —rebase
# clone remote repo to local 
git clone <endpoint path or ssh syntax> [local dir name]
# show remote repo info
git remote -v
# delete branch remotely
git push origin :cat
# forcefully push commit, danger!!!!
git push -f 
# pull requests on Github

```

