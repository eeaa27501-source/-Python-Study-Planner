# Python Study Planner — Web App

A browser-based study planner built with Python and Streamlit.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Run: `pip install -r requirements.txt`
4. Run: `streamlit run app.py`

## Deploy
Push this folder's contents to the GitHub repository. On Streamlit Community Cloud, create a new app, select this repository and branch `main`, and set the main file path to `app.py`.

## Note
This demo stores tasks in Streamlit session state, so tasks are temporary and may reset when the session ends or the app restarts. It is not a permanent database.
