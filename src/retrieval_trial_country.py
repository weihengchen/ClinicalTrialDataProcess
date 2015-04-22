import sys
import json
import logging


if __name__ == '__main__':
    logger = logging.getLogger(__name__);
    logger.setLevel(logging.INFO);
    handler = logging.FileHandler('error.log');
    logger.addHandler(handler);

    reload(sys);
    sys.setdefaultencoding('utf8');
    fin = open(sys.argv[1]);
    for line in fin.readlines():
        line = json.loads(line);
        #retrieval country in 'location.facility.address.country'
        if not 'clinical_study' in line:
            continue;
        trial = line['clinical_study'];
        content = trial['id_info']['nct_id'];
        content = content + '\t' + trial['firstreceived_date'];
        if not 'location' in trial:
            logger.info(content);
            continue;
        locations = trial['location'];
        has_country = {};
        if isinstance(locations, list):
            for loc in locations:
                if ('facility' in loc and 'address' in loc['facility'] and
                        'country' in loc['facility']['address']):
                    if loc['facility']['address']['country'] in has_country:
                        continue;
                    has_country[loc['facility']['address']['country']] = 1;
                    content = content + '\t' + loc['facility']['address']['country'];
        else :
            loc = locations;
            if ('facility' in loc and 'address' in loc['facility'] and
                    'country' in loc['facility']['address']):
                if loc['facility']['address']['country'] in has_country:
                        continue;
                has_country[loc['facility']['address']['country']] = 1;
                content = content + '\t' + loc['facility']['address']['country'];
        print content;
    fin.close();


