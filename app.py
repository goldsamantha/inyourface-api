from flask import Flask, request
import os, inyourface.effect

from inyourface import EffectOrchestrator

app = Flask(__name__)
image_dir = os.environ['IYF_IMAGE_DIR'] if 'IYF_IMAGE_DIR' in os.environ else 'img/'
cache_dir = os.environ['IYF_CACHE_DIR'] if 'IYF_CACHE_DIR' in os.environ else False
if (cache_dir):
    try:
        os.stat(cache_dir)
    except:
        os.mkdir(cache_dir)

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
