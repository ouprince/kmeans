baseDir=$(cd `dirname "$0"`;pwd)
cd $baseDir
rm -rf $baseDir/data/kmeans-clusters/*
ksum=$1
mahout kmeans \
        -i data/vector.txt \
        -c data/centroids \
        -cl \
        -cd 1.0 \
        -o data/kmeans-clusters \
        -k $ksum \
        -ow \
        -x 2000 \
        -dm org.apache.mahout.common.distance.ChebyshevDistanceMeasure 
