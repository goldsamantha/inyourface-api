# Welcome to the super simple inyourface API

### To run on port [5000](http://localhost:5000):
For this example your images will live in the `/img` directory. This assumes that you've already gotten [google credentials](https://cloud.google.com/vision/docs/auth) and named the file `google-credentials.json` in the home directory of this project. Feel free to name these folders whatever you like, live your truth.
```
$ mkdir img/cache/
$ export FLASK_APP=app.py IYF_IMAGE_DIR=img/ GOOGLE_APPLICATION_CREDENTIALS=google-credentials.json
$ pip install inyourface
$ flask run
```
This sets up the scaffolding where your images will get stored and tells the application where to look for your google credentials.
Note: the `/` are important as folders are built as strings--e.g. without them, IYF will attempt to load images in the `imgglitter` or `imgthinking` directories instead.

It can be really handy to have debug mode on for this for continuous refresh. If you'd like that then also run the following and restart the app:
```
$ export FLASK_DEBUG=1

```

This should be all you need to do to get up and running with the app. In another window try the following command to curl to the simple api:
```
curl -X POST -H 'Content-type: application/JSON' -d '{"effects" : ["glitter"], "urls" : ["https://pbs.twimg.com/profile_images/777564057553567749/7P6m2BMF_400x400.jpg"] }' http://localhost:5000/effect
```

Check your `./img/glitter` directory for a new image to confirm that it worked

In order for the inyourface library to work you will need credentials for the google vision api and they will need to be stored in the home directory for this project under:
`.google-credentials.json`

### TODO:
- [ ] Proper error handling for
  - no image
  - no effects
- [ ] check file upload size is not too much
- [ ] add a util class with:
  - directory hack update for all inyourface effects
  - sample util functions like `getDirectoryPath()`, `getAngle()`, `getCoefficient()`
