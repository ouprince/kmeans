baseDir=$(cd `dirname "$0"`;pwd)
LUCENE_DIR=$baseDir/index
OUTPUT_DIR=$baseDir/data/vector.txt
DICT_DIR=$baseDir/data/dict.txt
SEQ_DICT_DIR=$baseDir/data/dict.seq.txt

rm -rf $baseDir/data/*

# main 
#[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
echo "apache mahout home:" $MAHOUT_HOME

mahout lucene.vector \
       --dir $LUCENE_DIR \
       --idField id \
       --output $OUTPUT_DIR \
       --field post \
       --dictOut $DICT_DIR \
       --seqDictOut $SEQ_DICT_DIR \
       --weight TFIDF \
       --minDF 1 \
       --norm 2 \
       --maxPercentErrorDocs 1 
