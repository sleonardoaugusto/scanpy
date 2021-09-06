# scanpy

An upwork data scrapper.

## How develop?

1. Clone this repo.
2. Create a virtualenv with Python 3.x.
3. Activate virtualenv.
4. Install dependencies.
5. Run tests.

```console
git clone git@github.com:sleonardoaugusto/scanpy.git
cd scanpy
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

# How to use?

## Running
You can interact with the application by commandline.

- Scrapping with secret key
```
python app.py --username=[username] --password=[password] --secret_key=[secret_key]
```

- Scrapping with secret answer
```
python app.py --username=[username] --password=[password] --secret_answer=[secret_answer]
```

## Database
The scrapped data will be stored in a **database.json** file