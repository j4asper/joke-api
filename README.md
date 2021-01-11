## Simple Joke API
This is a __very__ simple joke api. When a GET request is done with a valid API key, a random joke will be returned.

I would not recommend saving api keys in a json file, it's only to give some context.

You can add jokes on your own in the jokes.json file. Or even try to make the server accept POST requests that can add jokes to a database or a json file.
The test.py file is just to confirm that the API works. It makes a GET request with a working API key.

Only Flask is needed to use this:
```pip install Flask```
