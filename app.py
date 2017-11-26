from flask import Flask, request, jsonify
import os, sys, click, pprint
import config

app = Flask(__name__)

# inyourface submodule
lib_dir_path        = os.getcwd() + "/lib/inyourface"
sys.path.append(lib_dir_path)
import inyourface.effect
from inyourface import EffectOrchestrator

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
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config.google_credentials
    data = request.get_json()
    urls = data.get("urls")
    # TODO: error handling for no image_url
    effects = data.get("effects")
    effects = list(filter((lambda x: is_effect(x)), effects))

    if (len(effects) == 0):
        return "You must specify some effects!"
    elif (len(effects) == 1):
        effect_module = getattr(inyourface.effect, effects[0][0].upper() + effects[0][1:])
        gif = effect_module.EffectAnimator(urls, config.image_dir, config.cache_dir)
        name = gif.gif()
        return name
    else:
        gif = EffectOrchestrator(urls, config.image_dir, config.cache_dir, effects)
        name = gif.gif()
        return name


def is_effect(e):
    try:
        effect_module = getattr(inyourface.effect, e[0].upper() + e[1:])
        return True
    except Exception as ex:
        return False
