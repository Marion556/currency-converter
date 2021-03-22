### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
    .Python does not declare variables like const or let
    .Python use _ to name variables while JS uses ThisVar
    .Python is used for backend developement and is mainly object oriented
    .Python relies on indentation
    .Python uses # to write comments, JS uses //
    .Logical operators are different (and, or not vs &&, ||, !)
    .Python uses print, JS uses console.log

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
    .dict.get('c', 'Is missing")
    .dict.setdefault('c', 'Is missing')

- What is a unit test?
    .It is the testing of a single component.

- What is an integration test?
    .Test that components work together

- What is the role of web application framework, like Flask?
    .It is to make the server-side scripting easier for the developper.
    .Flask provides tools and libraries like Jinja.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
    .Query param are best to sort data collected with an API
    .path param is good to identify specific ressources

- How do you collect data from a URL placeholder parameter using Flask?
    .flask.request.args.get()

- How do you collect data from the query string using Flask?
    .flask.request.args.get()

- How do you collect data from the body of the request using Flask?
    .request.form.get()

- What is a cookie and what kinds of things are they commonly used for?
    .Cookies store information. Mainly used to store login info as key value pair.
    .A session cookie gets erased when we close the browser.
    .A stored cookie is stored on the hard drive until it expires or until deleted.

- What is the session object in Flask?
    .It is used to track the session data which is a dictionary object that contains key value pairs
    for session variables and associated values. It is stored in the browser.

- What does Flask's `jsonify()` do?
    .It is a helper method that returns data in JSON format.
    .JSON is JavaScript Object Notation, used for transmitting data in web application.
