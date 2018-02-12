baseDir=$(cd `dirname "$0"`;pwd)
cd $baseDir
textname=$1
ksum=$2
./yuchuli.sh $1
sh index.sh
sh vector.sh
./kmeans.sh $2
sh clusterdump.sh
python jieguo.py $1
vi $baseDir/result/${textname}-result
