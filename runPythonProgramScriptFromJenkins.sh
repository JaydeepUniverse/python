#!/bin/bash
lastCount=`ll -ltrh /jaydeep/python|awk '{print $9}'|awk -F - '{print $1}'|grep -v "README"|sort|tail -1`
lastFile=`ll -ltrh /jaydeep/python|grep "$lastCount-"|awk '{print $9}'`
python2 /jaydeep/python/$lastFile
