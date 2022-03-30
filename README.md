# Permutation Cipher Python's FastApi Implementation
Backend to Full Stack Permutation Cipher Test in React

## Getting Started

First, Create a virtual environment to isolate our package dependencies locally:

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

Then Install reqiured packages

```bash
pip install -r requirements.txt 
```

Now run the server, suffix with --reload to make the server watch for changes

```bash
uvicorn main:app --reload 
```

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

Open [http://localhost:8000/encode](http://localhost:8000/encode) with your browser to encrypt password.

Open [http://localhost:8000/docs](http://localhost:8000/docs) to previeew the documentation
