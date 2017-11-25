# Welcome to the super simple inyourface API

### To run on port [5000](http://localhost:5000):
```
$ export FLASK_APP=app.py
$ flask run
```

It can be really handy to have debug mode on for this for continuous refresh. If you'd like that then also run the following and restart the app:
```
$ export FLASK_DEBUG=1
```

This should be all you need to do to get up and running with the app. In another window try the following command to curl to the simple api:
```
curl -X POST -H 'Content-type: applicat '{"effects" : ["glitter"], "urls" : ["https://pbs.twimg.com/profile_images/777564057553567749/7P6m2BMF_400x400.jpg"] }' http://localhost:5000/effect
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
