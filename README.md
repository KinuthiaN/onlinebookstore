# Installation

~ Install python 3.10.8 from the [official python website](https://www.python.org/downloads/release/python-3108/)

~ Clone the website

```bash
    git clone https://github.com/KinuthiaN/onlinebookstore.git
```

~ Navigate to folder

```bash
    cd onlinebookstore
```

~ Create a virtual environment

```bash
    python -m venv .venv
```

~ Activate the virtual environment

```bash
    source .venv/bin/activate
```

~ Install requirements

```bash
    pip install -r requirements.txt
```

~ Make app migrations

```bash
    python manage.py makemigrations
```

~ Run app migrations

```bash
    python manage.py migrate
```

## Running

~ Run the server

```bash
    source .venv/bin/activate
    pip install -r requirements.txt
    python manage.py runserver
```

~ Access the website at: [127.0.0.1:8000](http://127.0.0.1:8000)
