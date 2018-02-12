baseDir=$(cd `dirname "$0"`;pwd)

textname=$1

cd $baseDir
rm -rf $baseDir/test/*

python read.py $baseDir/$textname  $baseDir/test/$textname
