baseDir=$(cd `dirname "$0"`;pwd)
cd $baseDir
rm -f $baseDir/data/kmeans.clusterdump

mahout clusterdump -d $baseDir/data/dict.txt \
                    -dt text \
                    -dm org.apache.mahout.common.distance.SquaredEuclideanDistanceMeasure \
                    -i $baseDir/data/kmeans-clusters/clusters-*-final \
                    -o $baseDir/data/kmeans.clusterdump \
                    -n 10 \
                    -b 10 \
                    -of JSON \
                    -p $baseDir/data/kmeans-clusters/clusteredPoints 
