import sys

if __name__=='__main__':
    f1 = open(sys.argv[1]);
    f2 = open(sys.argv[2]);

    dict_countries = {};
    for line in f1.readlines():
        line = line.lower().strip('\n').split('\t');
        dict_countries[line[0]] = line;
    f1.close();

    for line in f2.readlines():
        line = line.lower().strip('\n');
        if line in dict_countries:
            continue;
        print line;
    f2.close();

