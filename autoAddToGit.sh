#!/bin/bash
lastCount1=`ls -l|awk '{print $9}'|awk -F - '{print $1}'|grep -v "README\|autoAddToGit"|sort|tail -1`
lastFile1=`ls -l|grep "$lastCount1-"|awk '{print $9}'`

git add $lastFile1

read -p "Enter Git Commit message : " gitCommitMessage
git add autoAddToGit.sh
git commit -m "$gitCommitMessage"

git status

git push origin master
