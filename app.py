from flask import Flask, request, jsonify
import os, sys, click, pprint

app = Flask(__name__)

# necessary directories for images
image_dir           = os.getcwd() + "/img/"
cache_dir           = os.getcwd() + "/img/cache"
google_credentials  = os.getcwd() + "/google-credentials.json"

# inyourface submodule
lib_dir_path        = os.getcwd() + "/lib/inyourface"
sys.path.append(lib_dir_path)
import inyourface.effect
from inyourface import EffectOrchestrator

# set up some globals for google credz, image directory, and cache dir
# set up a "help" prompt

"""
This is a basic request for an inyourface effect which will return a gif with
the requested effects
request should have:
{
  urls: string [] // list of images, gifs
  effects: string [] // list of effects
}
"""
@app.route('/effect', methods=['POST'])
def effect():
    global image_dir, cache_dir, google_credentials
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = google_credentials
    data = request.get_json()
    urls = data.get("urls")
    # TODO: error handling for no image_url
    effects = data.get("effects")
    effects = list(filter((lambda x: is_effect(x)), effects))

    if (len(effects) == 0):
        return "You must specify some effects!"
    elif (len(effects) == 1):
        effect_module = getattr(inyourface.effect, effects[0][0].upper() + effects[0][1:])
        gif = effect_module.EffectAnimator(urls, image_dir, cache_dir)
        name = gif.gif()
        return name
    else:
        gif = EffectOrchestrator(urls, image_dir, cache_dir, effects)
        name = gif.gif()
        return name


def is_effect(e):
    try:
        effect_module = getattr(inyourface.effect, e[0].upper() + e[1:])
        return True
    except Exception as ex:
        return False
