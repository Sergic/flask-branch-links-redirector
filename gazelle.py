__author__ = 'Gaiar'
import urllib



class Gazelle(object):
    LINK_TYPES = {
        'index': {
            'desktop_url': 'http://www.ivi.ru/',
            'deeplink': 'index/'
        },
        'movie': {
            'desktop_url': 'http://www.ivi.ru/watch/',
            'deeplink': 'movie/open/'
        },
        'series': {
            'desktop_url': 'http://www.ivi.ru/watch/',
            'deeplink': 'compilation/open/'
        },
        'collection': {
            'desktop_url': 'http://www.ivi.ru/collections/',
            'deeplink': 'collection/open/'
        }
    }

    def prepare_branch_params(self, content, gutm={}, deepview=True, link_type='index'):
        gutm_params = {}
        """:type: dict """
        params = {
            '$always_deeplink': True
        }
        """:type: dict """
        for key, value in gutm.items():
            gutm_params.update({key: value})
            params.update({key: value})

        if deepview:
            params.update({
                '$ios_deepview': 'default_template',
                '$android_deepview': 'default_template'
            })
        referrer = urllib.urlencode(gutm_params)
        deeplink_referrer = '?referrer=' + urllib.quote_plus(referrer)

        if link_type == 'index':
            params.update(
                {
                    '$og_title': '',
                    '$og_description': '',
                    '$og_image_url': '',
                    '$desktop_url': self.LINK_TYPES['index']['desktop_url'] + '?' + referrer,
                    '$deeplink_path': self.LINK_TYPES['index']['deeplink'] + '?' + deeplink_referrer
                })
        elif link_type == 'movie':
            params.update(
                {
                    '$og_title': content['title'],
                    '$og_description': content['synopsis'] if len(content['synopsis']) > 1 else content['description'],
                    '$og_image_url': content['poster_originals'][0]['path']
                }
            )
            if content['kind'] == 1:
                params.update({
                    '$desktop_url': self.LINK_TYPES['movie']['desktop_url'] + str(
                        content['id']) + '/description' + '?' + referrer,
                    '$deeplink_path': self.LINK_TYPES['movie']['deeplink'] + str(content['id']) + deeplink_referrer
                })
            else:
                params.update({
                    '$desktop_url': self.LINK_TYPES['series']['desktop_url'] + str(content['hru']) + '?' + referrer,
                    '$deeplink_path': self.LINK_TYPES['series']['deeplink'] + str(content['id']) + deeplink_referrer
                })


        elif link_type == 'collection':
            params.update(
                {
                    '$og_title': content['title'],
                    '$og_description': content['synopsis'] if len(content['synopsis']) > 1 else content['description'],
                    '$og_image_url': '',
                    '$desktop_url': self.LINK_TYPES['collection']['desktop_url'] + str(content['hru']) + '?' + referrer,
                    '$deeplink_path': self.LINK_TYPES['collection']['deeplink'] + str(content['id']) + deeplink_referrer
                }
            )
        return params