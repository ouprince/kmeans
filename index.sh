#! /bin/bash 
baseDir=$(cd `dirname "$0"`;pwd)

JAR=jar/text-indexer-1.0-SNAPSHOT-jar-with-dependencies.jar
#[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return

cd $baseDir
if [ ! -f $JAR ]; then
    echo "first run $baseDir/package.sh to build jar."
    exit 1
fi
rm -rf $baseDir/index/*

java -cp $JAR lucene.text.FileIndexing $baseDir/test $baseDir/index
