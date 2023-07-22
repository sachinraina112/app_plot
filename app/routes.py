from flask import Flask

app = Flask(__name__)
import os
print(os.getcwd())
import json, plotly
from flask import render_template, request
from scripts.GetDataForPlots import return_figures

import logging
logger = logging.getLogger(__name__)

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

@app.route('/heartbeat', methods=['GET'])
def get_status():
	return "true"


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():


	# Parse the POST request countries list
	if (request.method == 'POST') and request.form:
		keyword_dict = request.form
		logger.info(keyword_dict)
		keyword = keyword_dict.getlist("keywords")[0]
		# # log.info(keyword)
		# keyword = keyword.replace(" ","")
		figures = return_figures(eval(keyword))
	
	# GET request returns all countries for initial page load
	else:
		figures =[request.form]

	# plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('index.html', ids=ids,
		figuresJSON=figuresJSON)



if __name__ == "__main__":
	app.run(host="0.0.0.0", port=2321, debug=True)
	