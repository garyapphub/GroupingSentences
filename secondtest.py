# encoding=utf-8
import datetime
import sys, getopt

from groupingsentences.second import gs_grouping_sentences_to_xmind
from groupingsentences.first import gs_grouping_sentences_to_xls

def main(argv):
    inputfile = ''
    outputfile = ''
    top_words_count = 8
    encoding = 'gb18030'
    max_items = 1000

    try:
        opts, args = getopt.getopt(argv,"hi:o:c:e:t:",["ifile=","ofile=","encoding=","maxcount="])
    except getopt.GetoptError:
        print('second.py -i <inputfile> -o <outputfile> -c <maxcount 1000 default> -e <encoding gb18030 default> -t <topwordscount 8 default>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('second.py -i <inputfile> -o <outputfile> -c <maxcount 1000 default> -e <encoding gb18030 default> -t <topwordscount 8 default>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-t"):
            top_words_count = int(arg)
        elif opt in ("-e", "--encoding"):
            encoding = (arg)
        elif opt in ("-c", "--maxcount"):
            max_items = int(arg)
    if len(inputfile)==0 or len(outputfile)==0:
        print('second.py -i <inputfile> -o <outputfile> -c <maxcount 1000 default> -e <encoding gb18030 default> -t <topwordscount 8 default>')
        sys.exit(2)

    print('Input file is "', inputfile)
    print('Output file is "', outputfile)
    gs_grouping_sentences_to_xmind(inputfile, outputfile, max_items=10000, encoding='gb18030', topwordscount = 8)


if __name__ == "__main__":
    main(sys.argv[1:])
