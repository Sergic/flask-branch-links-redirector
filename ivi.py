__author__ = 'Gaiar'
import requests


class IVI(object):
    def __init__(self, app_version=994, session=None):
        self.api_url = 'https://api.ivi.ru/mobileapi'
        self.app_version = app_version

    def get_movie_info(self, movie_id):
        url_endpoint = '{0}/videoinfo/v5/'.format(self.api_url)
        params = {'id': movie_id,
                  'app_version': self.app_version}
        r = requests.get(url_endpoint, params)
        return r.json()

    def get_compilation_id(self, compilation_hru):
        url_endpoint = '{0}/cinema/compilation_id/by/hru/'.format(self.api_url)
        params = {'query': compilation_hru}
        r = requests.get(url_endpoint, params)
        return int(r.json()['id'])

    def get_compilation_info(self, compilation_id):
        if not compilation_id.isdigit():
            compilation_id = self.get_compilation_id(compilation_id)

        url_endpoint = '{0}/compilationinfo/v5/'.format(self.api_url)
        params = {'id': compilation_id,
                  'app_version': self.app_version}
        r = requests.get(url_endpoint, params)
        return r.json()

    def get_collection_info(self, collection_id):
        params = {}

        if not collection_id.isdigit():
            params = {'hru': collection_id}
        else:
            params = {'id': collection_id}
        params.update({'app_version': self.app_version})
        url_endpoint = '{0}/collectioninfo/v5/'.format(self.api_url)

        r = requests.get(url_endpoint, params)
        return r.json()
