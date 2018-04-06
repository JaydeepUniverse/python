#!/bin/bash
lastCount1=`ll -ltrh|awk '{print $9}'|awk -F - '{print $1}'|grep -v "README\|autoAddToGit"|sort|tail -1`
lastFile1=`ll -ltrh|grep "$lastCount1-"|awk '{print $9}'`

git add $lastFile1

read -p "Enter Git Commit message : " gitCommitMessage
git commit -m "$gitCommitMessage"

git status

git push origin master
