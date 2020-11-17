# encoding=utf-8
import datetime
import sys, getopt

from groupingsentences.second import gs_grouping_sentences_to_xmind
from groupingsentences.first import gs_grouping_sentences_to_xls

def main(argv):
    inputfile = ''
    outputfile = ''
    type_of_func = 0
    threshold = 0.55
    encoding = 'gb18030'
    max_items = 1000

    try:
        opts, args = getopt.getopt(argv,"hi:o:c:e:f:t:",["ifile=","ofile=","encoding=","maxcount="])
    except getopt.GetoptError:
        print('first.py -i <inputfile> -o <outputfile> -c <maxcount 1000 default> -e <encoding gb18030 default> -f <typeofcomparefunction 0 default> -t <threshold 0.55 default>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('first.py -i <inputfile> -o <outputfile> -c <maxcount 1000 default> -e <encoding gb18030 default> -f <typeofcomparefunction 0 default> -t <threshold 0.55 default>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-f"):
            type_of_func = int(arg)
        elif opt in ("-t"):
            threshold = float(arg)
        elif opt in ("-e", "--encoding"):
            encoding = (arg)
        elif opt in ("-c", "--maxcount"):
            max_items = int(arg)
    if len(inputfile)==0 or len(outputfile)==0:
        print('first.py -i <inputfile> -o <outputfile> -c <maxcount 1000 default> -e <encoding gb18030 default> -f <typeofcomparefunction 0 default> -t <threshold 0.55 default>')
        sys.exit(2)

    print('Input file is "', inputfile)
    print('Output file is "', outputfile)
    gs_grouping_sentences_to_xls(inputfile, outputfile, max_items, encoding, type_of_func , threshold)
   

if __name__ == "__main__":
    main(sys.argv[1:])
