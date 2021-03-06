## HW 1
## SI 364 F18
## 1000 points

#################################


## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".
# I worked with Sam Lu
# I used code from Challenges.py from discussion 


## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

#from flask import Flask
import requests 
import json 

from flask import Flask, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
	return 'Welcome to SI 364!'



## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' 
#you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }

@app.route('/movie/<moviename>')
def get_movie(moviename):
	base_url = "https://itunes.apple.com/search"
	params_diction = {}
	params_diction['term'] = moviename
	resp = requests.get(base_url, params = params_diction)
	text = resp.text
	python_obj = json.loads(text)
	return str(python_obj)


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

@app.route('/form')
def question():
	html_form = '''
	<html>
	<body>
	<form method ="GET" action ="/result"> 
		Enter your favorite number : 
		<input type='text' name="number"></input>
		<input type = 'submit' name = 'submit'></input>
	</form>
	</body>
	</html>
	'''
	return html_form

@app.route('/result', methods = ['GET', 'POST'])
def result_doubled():
	if request.method == 'GET':
		number = str(request.args.get("number"))
	int_number = int(number)
	doubled = int_number*2
	response_string = "Double your favorite number is " + str(doubled)
	return response_string




## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, 
#you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is 
#<number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". 
#Careful about types in your Python code!
## You can assume a user will always enter a number only.


## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, 
#and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

@app.route('/problem4form', methods = ['GET', 'POST'])
def get_synopsis():
	html_form2 = '''
	<html>
	<body>
	<form method ="POST" action ="/problem4form"> 
		<label>Enter a movie title:</label><br>
		<input type='text' name="title"></input>
		<br>Do you want the IMBD or Rotten Tomatoes rating? </br>
		<input type='radio' name="Ratingsystem" value="IMDB">IMDB</input><br>
		<input type='radio' name="Ratingsystem" value="RottenTomatoes">Rotten Tomatoes</input><br>
		<input type = 'submit' name = 'submit'></input>
	</form>
	</body>
	</html>
	'''
	
	APIKEY = "3fb83d44"
	if request.method == 'POST':             
		rating = request.form.get('Ratingsystem')
		title = request.form.get("title")
		baseurl = "http://www.omdbapi.com/"
		response = requests.get(baseurl, params={'apikey' : APIKEY, 't': title})
		omdb_data = json.loads(response.text)
		
		if rating == "IMDB":
			return "The IMDB rating of " + title + " is " + (omdb_data['Ratings'][0]['Value'])
		if rating == 'RottenTomatoes':
			return "The Rotten Tomatoes rating of " + title + " is " + (omdb_data['Ratings'][1]['Value'])


	return html_form2

if __name__ == '__main__':
	app.run()

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the 
#submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). 
#The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing 
#out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors 
#or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for 
#a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume 
#they will do that.)

# Points will be assigned for each specification in the problem.
