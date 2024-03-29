__author__ = 'Gaiar'

import requests

import urllib


class BranchClient(object):
    def __init__(self, branch_key, branch_secret='', branch_domain=None):
        self.branch_key = branch_key
        self.branch_secret = branch_secret
        self.api_url = 'https://api.branch.io'
        if branch_domain:
            self.branch_domain = branch_domain
        else:
            self.branch_domain = 'https://bnc.lt'

    def create_branch_short_link(self, has_app=False, duration=None, type=0, data={}, tags=[], campaign=None,
                                 feature=None,
                                 channel=None, stage=None):
        url_endpoint = '{0}/v1/url'.format(self.api_url)
        params = {'branch_key': self.branch_key}

        params.update({'has_app': 'yes'}) if has_app else params.update({'has_app': 'no'})

        if duration:
            params.update({'duration': duration})

        if type in [0, 1]:
            params.update({'type': type})
        if data:
            params.update({'data': data})
        if len(tags) > 0:
            params.update({'tags': tags})
        if campaign:
            params.update({'campaign': campaign})
        if feature:
            params.update({'feature': feature})
        if channel:
            params.update({'channel': channel})
        if stage:
            params.update({'stage': stage})
        r = requests.post(url_endpoint, json=params)

        return r.json()

    def create_branch_redirect_link(self, has_app=False, duration=None, type=0, data={}, tags=[], campaign=None,
                                    feature=None,
                                    channel=None, stage=None):
        redirect_link = '{0}/a/{1}/?'.format(self.branch_domain, self.branch_key)

        # redirect_link = self.branch_domain + '/a/' + self.branch_key + '/?'

        params = {}

        params.update({'has_app': 'yes'}) if has_app else params.update({'has_app': 'no'})
        if duration:
            params.update({'duration': duration})

        if type in [0, 1]:
            params.update({'type': type})

        for name, value in data.items():
            params.update({name: value})

        if len(tags) > 0:
            params.update({'tags': tags})
        if campaign:
            params.update({'campaign': campaign})
        if feature:
            params.update({'feature': feature})
        if channel:
            params.update({'channel': channel})
        if stage:
            params.update({'stage': stage})

        redirect_link += urllib.urlencode(params)
        return redirect_link

    def get_credits_count(self, identity):

        url_endpoint = '{0}/v1/credits'.format(self.api_url)
        params = {'branch_key': self.branch_key,
                  'identity': str(identity)}
        r = requests.get(url_endpoint, params)
        return r.json

    def add_credits(self, identity, credits_amount, bucket=''):

        url_endpoint = '{0}/v1/credits'.format(self.api_url)
        params = {'branch_key': self.branch_key,
                  'branch_secret': self.branch_secret,
                  'identity': identity,
                  'amount': credits_amount
                  }
        if bucket:
            params.update({
                'bucket': bucket
            })
        r = requests.post(url_endpoint, json=params)

        return r.json()

    def get_credits_history(self,identity):

        url_endpoint='{0}/v1/credithistory'.format(self.api_url)
        params={
            'branch_key':self.branch_key,
            'identity':identity
        }

        r = requests.get(url_endpoint,params)
        return r.json()
    