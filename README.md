# MapThingy

MapThingy is a simple Python + Javascript application that shows you where IP addresses and hostnames (such as `8.8.4.4` or `virgosvs.com`) are located on a Google Maps page. We are using [ipstack.com](https://ipstack.com/) to find the geographic location of our targets.

The system was built using:

* Python (3+ should work)
* [Tornado](http://www.tornadoweb.org/) as a Web and WebSocket server
* [Bulma](https://bulma.io) for simple CSS
* [Zepto.js](http://zeptojs.com) as a smaller jQuery
* [Lodash](https://lodash.com/) as a small utility box


## Instructions

1. Clone this repository into your own Github account
2. Read the [Running the code](#running-the-code) section and make sure you can get the server working. Reach out to your technical contact at Virgo if you run into any issues
3. Start working on the tasks in the [Assignment](#assignment) section. Every time you complete a task, make a Git commit with your changes. Each commit message should be formatted like `#{TASK_NUMBER} Small description`
4. Once you are done (either because you ran out of time or tasks to complete) make a pull request against our repository with your changes

> ℹ️ **Important!** we don't want you to spend an inordinate amount of time on this challenge. We recommend you take about one hour of your time to work on the tasks. We don't expect you to finish all tasks, *but we do expect you to finish them in the specified order*. If you feel inspired to finish all the tasks - and by all means do it! - we still ask you to make the pull request around one hour after you started working on the code.

### Running the code

### Using `docker compose` (recommended)

If you have a recent version of Docker installed, you should be able to start right away:

To run the server code:
```
$ docker compose up
```

To run the tests:
```
$ docker compose exec mapthingy pytest mapthingy/tests.py
```

Now point your browser to [http://localhost:8888](http://localhost:8888). Do you see a map and a text input below it? Success! 🎉

### Using your local Python installation


> 📝 **Note**: MapThingy requires a version of Python older than 3.10. If you are using [Pyenv](https://github.com/pyenv/pyenv), the directory is configured to request Python 3.9.13. If you aren't but your OS provides a recent version of Python (>= 3.7, < 3.10) then you should be able to run the following commands without issue.


If you are on Linux or macOS, you should be able to bootstrap the environment by running the following commands:
```
$ ./bootstrap.sh
$ source .env/bin/activate
```

To start the server, run the following command:
```
$ python mapthingy/server.py
```

To run tests:
```
$ pytest mapthingy/tests.py
```

Now point your browser to [http://localhost:8888](http://localhost:8888). Do you see a map and a text input below it? Success! 🎉

## Assignment

1. We'd like MapThingy to center the map on San Francisco when the page is first loaded, make that happen.
2. There's a classmethod `APIHandler.is_hostname` on the `server.py` file that needs to be implemented. There's a simple test for it in `tests.py`, we'd like that test to pass.
3. The markers are generated without a title. [Google Maps API](https://developers.google.com/maps/documentation/javascript/markers) specifies a `title` attribute that could be used for adding the domain or IP address the marker belongs to.
4. ipstack.com has a hard limit on how many requests can be made to the backend in a given hour. Implement a simple in-memory cache so that results that already exist don't need to be fetched again. [This StackOverflow question](https://stackoverflow.com/questions/12240285/how-to-share-data-between-requests-in-tornado-web) has a pointer on how to keep state between requests.
5. There's a "Find All" button on the page that currently isn't implemented. Using the existing API, implement it by sending each value in the comma-separated list of values to the API.
6. Extend the API to perform the "Find All" function in single request. The results should be streamed from the backend as they become available.
7. If you implemented item #5 in a synchronous manner (by requesting all of the values in a loop on the server side), take a look at [Tornado's asynchronous HTTP client](http://www.tornadoweb.org/en/stable/httpclient.html) and figure out if there's a way you could speed up the retrieval of values from ipstack.com by making the requests asynchronously.
8. The [Google Maps marker API](https://developers.google.com/maps/documentation/javascript/markers) provides an `icon` attribute that could be used to display an image on the marker. Can you get our service to display the favicon for each data point that is a hostname/domain name?
9. Can you make MapThingy center around the location [reported by the browser the user is using](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)?
10. Can you persist the values in the input box between reloads of the page for a given user? (hint: we don't care if you store it in the backend or the browser)
11. Can you provide a link somewhere in the interface that allows a user to download the list of hostnames/IPs they introduced?