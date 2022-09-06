# Sentiment Analysis API

An API to provide sentiment analysis rating on text data.
Sentiment Analysis powered by Vader.

A RESTful API built with Python 3.8.10 and Flask-Restful

Currently a work in progress ...

To run the API locally, you must first enter the python virtual environment using the command:

source my-venv/bin/activate

You can then access the API and submit a POST request with key "text" and string value to the URL:

http://[your port here]/api/v1/

The API will return a JSON object containing the values associated with the sentiment analysis of the request
