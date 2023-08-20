# Fashion Recommendation API

This is a Flask-based API for providing fashion recommendations based on user preferences. It uses a combination of user queries, correlation engine, and clustering model to suggest fashion items.

## Getting Started

These instructions will help you set up and run the Flask API on your local machine.

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Installing

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/frg-ai/frg-flask-app.git
   ```

2. Navigate to project directory

   ```bash
   cd frg-flask-app
   ```

3. Create a virtual environment

   ```bash
   python3 -m venv .venv
   ```

4. Source the environment

   ```bash
   source .venv/Scripts/activate
   ```

5. Install the required dependencies

   ```bash
   pip install -r requirements.txt
   ```

### Endpoints

- GET /: Home page of the API. [beta]
- POST /query: Receive user query and return fashion recommendations.
- GET /fashion/<id>: Get fashion item details by ID.

### Usage

- Send a POST request to /query with JSON data containing the query string and the username.
- The API will process the query, merge user preferences, and provide fashion recommendations.
- You can also access fashion item details using the /fashion/<id> endpoint.

### Run the program

```bash
    python ./main.py
```
