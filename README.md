# Bullet Point Destructor

- [Bullet Point Destructor](#bullet-point-destructor)
  - [How to use this repo](#how-to-use-this-repo)
  - [API](#api)

## How to use this repo

1. Create a virtual environment, you can use the make recipe:

```bash
make venv
```

2. Activate the environment:

```bash
source .venv/bin/activate
```

## API

An api was implemented using FastAPI which at the moment has a GET enpoint to extract the 5 bullet point descriptions, **(what, why, how, who and skills)** given a raw bullet point as a string.

For running the API you can use the make recipe:

```bash
make api
```

or from the root of the repo on the terminal run:

```bash
python -m src.app.main
```

After that click on http://127.0.0.1:3000 and add the **/docs** path at the end to view the swagger UI.