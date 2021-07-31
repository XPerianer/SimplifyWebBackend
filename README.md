# SimplifyWebBackend
This is the python backend for the SimplifyWeb Browser Plugin developed for the 2021 NLP course at HPI

# Installation
Example for installing in a virtual environment:

Activating the virtual environment:
```
python3 -m venv .venv
. .venv/bin/activate
```

Installing dependencies:
```
pip install -r requirements.txt
```

You also need to download some special nltk library data one time.
This can be done using
```
python3
	import nltk
	nltk.download('punkt')
```

# Run
```
python3 -m app
```
The server now waits for connection from the plugin.
