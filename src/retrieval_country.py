import sys
import json


if __name__ == '__main__':
    reload(sys);
    sys.setdefaultencoding('utf8');
    dict_country = {};
    fin = open(sys.argv[1]);
    for line in fin.readlines():
        line = json.loads(line);
        # retrieval the countries in 'location_countries.country'
        '''
        if not 'clinical_study' in line:
            continue;
        trial = line['clinical_study'];
        if not 'location_countries' in trial:
            continue;
        countries = trial['location_countries'];
        if not 'country' in countries:
            continue;
        countries = countries['country'];

        if isinstance(countries, list):
            for i in countries:
                dict_country[i] = 1;
        else :
            dict_country[countries] = 1;
        '''
        #retrieval country in 'location.facility.address.country'
        if not 'clinical_study' in line:
            continue;
        trial = line['clinical_study'];
        if not 'location' in trial:
            continue;
        locations = trial['location'];
        if isinstance(locations, list):
            for loc in locations:
                if ('facility' in loc and 'address' in loc['facility'] and
                        'country' in loc['facility']['address']):
                    dict_country[loc['facility']['address']['country']] = 1;
        else :
            loc = locations;
            if ('facility' in loc and 'address' in loc['facility'] and
                    'country' in loc['facility']['address']):
                dict_country[loc['facility']['address']['country']] = 1;


    for k,v in dict_country.items():
        print k;


