pipeline{
  agent any
  stages{
    stage('Running Latest Python Program'){
      sh '''
      cd /jaydeep/python
      lastCount=`ls -l|awk '{print $9}'|awk -F - '{print $1}'|grep -v "README\|runPythonProgramScriptFromJenkins.sh\|autoAddToGit.sh"|sort -n|tail -1`
      lastFile=`ls -l|grep "$lastCount-"|awk '{print $9}'`
      python2 $lastFile
      '''
    }
  }
}
