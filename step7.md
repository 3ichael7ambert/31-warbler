# **Step Seven: Research and Understand Login Strategy**

Look over the code in ***app.py*** related to authentication.

- How is the logged in user being kept track of?

the do_logic function puts the user into session. Also it is retreived from the database using the add_user_to_g function to make sure the user is CURR_USER_KEY

- What is Flask’s ***g*** object?
"application context global"
It is a global variable and a way to share data between different parts of the application within the same request.

- What is the purpose of ***add_user_to_g ?***
  
```py
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None
```

We are adding the user object to the g global session, it is tracked during every request.

- What does ***@app.before_request*** mean?
  @app.before_request decorator registers the add_user_to_g function as a "before request" handler. The function is called before the request, allowing the currently logged-in user to the g object, making it available throughout the request.