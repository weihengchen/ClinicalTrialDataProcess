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

    ft2r = open(sys.argv[1]);
    region2year2num = {};
    country2region = {};
    miny = 10000;
    maxy = -1;
    region2year2num['ALL'] = {};
    for line in ft2r.readlines():
        line = line.strip('\n').split('\t');
        year = line[1].split(' ')[-1];
        miny = min(miny, int(year));
        maxy = max(maxy, int(year));
        if year in region2year2num['ALL']:
            region2year2num['ALL'][year] += 1;
        else:
            region2year2num['ALL'][year] = 1;
        for i in range(2, len(line)):
            c = line[i];
            if c in region2year2num:
                if year in region2year2num[c]:
                    region2year2num[c][year] += 1;
                else:
                    region2year2num[c][year] = 1;
            else:
                region2year2num[c] = {};
                region2year2num[c][year] = 1;
    content = ['region'];
    for i in range(miny, maxy+1):
        content.append(str(i));
    print '\t'.join(content);

    for c,v in region2year2num.items():
        content = [c];
        num = 0;
        for i in range(miny, maxy+1):
            if str(i) in region2year2num[c]:
                num += region2year2num[c][str(i)];
                content.append(str(num));
            else:
                content.append('0');
        print '\t'.join(content);
    logger.info('Program Finished!');
