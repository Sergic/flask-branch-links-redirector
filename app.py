__author__ = 'Gaiar'

from branch import BranchClient
from ivi import IVI
import simplejson
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

        branch_link = branch.create_branch_link(True, None, 0,
                                                gz.prepare_branch_params(response['result'], data, False),
                                                ['ivi', 'movie'], 'facebook', 'hell', 'mail', 'launch')
        return redirect(branch_link['url'], 302)

@app.route('/collections/<collection_hru>')
def get_branch_collection_link(collection_hru):



@app.route('/')
def get_branch_link():
    data = {'g_source': 'ivi',
            'g_campaign': 'gaiar'
            }
    response = ivi.get_movie_info(97812)
    branch_link = branch.create_branch_link(True, None, 0, gz.prepare_branch_params(response['result'], data, False),
                                            ['ivi', 'movie'], 'facebook', 'hell', 'mail', 'launch')
    return redirect(branch_link['url'], 302)


if __name__ == '__main__':
    app.run()
