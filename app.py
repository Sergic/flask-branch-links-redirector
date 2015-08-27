__author__ = 'Gaiar'

from branch import BranchClient
from ivi import IVI
from gazelle import Gazelle
from flask import Flask, redirect, url_for

gz = Gazelle()
branch = BranchClient('key_test_iceRbypBYEOFfsnpGBLVKhnczFpaZo1j')
ivi = IVI()

app = Flask(__name__)


@app.route('/watch/<content_id>')
@app.route('/watch/<content_id>/<serie_id')

def get_branch_movie_link(content_id, serie_id, collection_hru):
    data = {'g_source': 'ivi',
            'g_campaign': 'gaiar'
            }
    if content_id:
        if content_id.isdigit():
            response = ivi.get_movie_info(int(content_id))
        else:
            response = ivi.get_compilation_info(str(content_id))

        branch_params = gz.prepare_branch_params(response['result'], data, False, 'movie')

        branch_link = branch.create_branch_short_link(True, None, 0, branch_params,
                                                      ['ivi', 'movie'], 'facebook', 'hell', 'mail', 'launch')
        print('Branch long link: ' + branch.create_branch_redirect_link(True, None, 0, branch_params,
                                                 ['ivi', 'movie'], 'facebook', 'hell', 'mail', 'launch'))
        print('Branch short link: ' + branch_link['url'])
        return redirect(branch_link['url'], 302)

@app.route('/collections/<collection_id>')
def get_branch_collection_link(collection_id):
    data = {'g_source': 'ivi',
            'g_campaign': 'gaiar'
            }
    if collection_id:
        response = ivi.get_collection_info(collection_id)

        branch_link = branch.create_branch_short_link(True, None, 0,
                                                      gz.prepare_branch_params(response['result'], data, True,
                                                                               'collection'),
                                                      ['ivi', 'movie'], 'facebook', 'hell', 'mail', 'launch')
        print('Branch link: ' + branch_link['url'])
        return redirect(branch_link['url'], 302)

@app.route('/')
def get_branch_link():
    data = {'g_source': 'ivi',
            'g_campaign': 'gaiar'
            }
    branch_link = branch.create_branch_short_link(True, None, 0, gz.prepare_branch_params({}, data, True, 'index'),
                                                  ['ivi', 'movie'], 'facebook', 'hell', 'mail', 'launch')
    print('Branch link: ' + branch_link['url'])
    return redirect(branch_link['url'], 302)


if __name__ == '__main__':
    app.run(debug=True)
