import sys
import json
import logging
import os


if __name__ == '__main__':
    current_file = os.path.basename(os.path.splitext(__file__)[0]);
    logger = logging.getLogger(__name__);
    logger.setLevel(logging.INFO);
    handler = logging.FileHandler(current_file+'.log');
    logger.addHandler(handler);
    logger.info('Program Start!');

    reload(sys);
    sys.setdefaultencoding('utf8');

    fc2r = open(sys.argv[1]);
    country2region = {};
    for line in fc2r.readlines():
        if (line[0] == '#'):
            continue;
        line = line.lower().strip('\n').split('\t');
        country2region[line[0]] = line[1];
    fc2r.close();

    fin = open(sys.argv[2]);
    for line in fin.readlines():
        line = line.lower().strip('\n').split('\t');
        content = [line[0], line[1]];
        has_region = {};
        for i in range(2, len(line)):
            if line[i] in country2region:
                if country2region[line[i]] in has_region:
                    continue;
                has_region[country2region[line[i]]] = 1;
                content.append(country2region[line[i]]);
            else:
                logger.info(line[0]+'\t'+line[i]);
        print '\t'.join(content);

    logger.info('Program Finished!');
