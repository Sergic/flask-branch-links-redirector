__author__ = 'Gaiar'
from urllib import parse


class Gazelle(object):
    def prepare_branch_params(self, content, gutm={}, deepview=True):
        gutm_params = {}
        params = {
            '$og_title': content['title'],
            '$og_description': content['description'],
            '$og_image_url': content['poster_originals'][0]['path'],
            '$always_deeplink': True,
        }

        for key, value in gutm.items():
            gutm_params.update({key: value})
            params.update({key: value})

        # print (content['poster_originals'][0]['path'])

        if deepview:
            params.update({
                '$ios_deepview': 'default_template',
                '$android_deepview': 'default_template'
            })

        deeplink_referrer = '?referrer='+parse.quote_plus(parse.urlencode(gutm_params))

        if content['kind'] > 1:
            params.update({'$deeplink_path': 'compilation/open/' + str(content['id']) + deeplink_referrer,
                           '$desktop_url': 'http://www.ivi.ru/watch/' + str(content['hru']) + '?' + parse.urlencode(
                               gutm_params)})
        else:
            params.update({'$deeplink_path': 'movie/open/' + str(content['id'])+deeplink_referrer,
                           '$desktop_url': 'http://www.ivi.ru/watch/' + str(
                               content['id']) + '/description' + '?' + parse.urlencode(gutm_params)})

        return params
