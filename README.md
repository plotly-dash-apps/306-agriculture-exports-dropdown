# Getting Started with Plotly Dash

#### Description
Dash is a Python framework for building analytical web applications. Dash ties modern UI elements like dropdowns, sliders, and graphs to your Python code. In this class, participants will learn how to build a simple Dash application and deploy it online.

# How to deploy a simple Plotly Dash app on Heroku
* Take a moment to read this [Medium post about how to deploying this app](https://austinlasseter.medium.com/deploy-a-plotly-dash-app-on-heroku-4d2c3224230)


### Notes
* The `assets` folder is designed to hold all of your static images. Then you can call them using the `get_asset_url` method, as follows:
```
html.Img(src=app.get_asset_url(some_image.jpg)),
```
* There's a file called `favicon.ico` -- you can find and download customized favicons [here](https://www.favicon.cc/). Just replace the current favicon with a new one.
* The `requirements.txt` includes the basic libraries you'll need to run a simple Dash app, but for more complicated projects you may need to add additional libraries such as `dash-daq` or `scikit-learn`.
* Be sure to include the files `runtime.txt` and `Procfile`
* You should only have one app per repository, and you should name it `app.py` for deployment on Heroku. This name is referenced in `Procfile` and also inside of `app.py` itself.


### Additional Reading
* Plotly’s [Dash deployment guide](https://dash.plotly.com/deployment)
* Heroku’s [deployment guide](https://devcenter.heroku.com/articles/getting-started-with-python)
* Fantastic [blog post](https://towardsdatascience.com/deploying-your-dash-app-to-heroku-the-magical-guide-39bd6a0c586c) that dives deep
* Excellent [YouTube tutorial](https://www.youtube.com/watch?v=b-M2KQ6_bM4&feature=youtu.be)

## Simple dash apps to fork and imitate
This page presents a collection of very simple dash apps, designed for learning purposes. Each has an embedded link to its source code on github. Students can fork the code on github, modify the `app.py` file, and deploy their own version on Heroku.
* [Here's a Medium post](https://austinlasseter.medium.com/deploy-a-plotly-dash-app-on-heroku-4d2c3224230) describing how to do that.

## Simple (no callbacks, no pandas)
* https://zoo-animals-dash.herokuapp.com/
* https://flying-dog.herokuapp.com/
* https://example-donut-chart.herokuapp.com/
* https://dash-linechart-example.herokuapp.com/
* https://back2good-dc-metro.herokuapp.com/

## Dash apps with simple callbacks
* https://dash-simple-callback.herokuapp.com
* https://chuck-norris-execution.herokuapp.com/
* https://dash-radio-callback.herokuapp.com/

## More advanced callbacks
* https://lightsaber-chooser.herokuapp.com/
* https://dash-multitab-example.herokuapp.com/
* https://dash-daq-state.herokuapp.com/

## Dash apps with Pandas
* https://virginia-2016-vote-totals.herokuapp.com/
* https://scatterplot-dc-housing.herokuapp.com
* https://data-table-beer-example.herokuapp.com/
* https://my-test-pandas-app-123.herokuapp.com/

## Dash apps with maps
* https://dc-properties-map.herokuapp.com/
* https://virginia-census-data.herokuapp.com/
* https://dash-density-heatmap-dc.herokuapp.com/
* https://agriculture-exports-map.herokuapp.com/
* https://va-opioid-dashboard.herokuapp.com/
* https://dash-density-heatmap.herokuapp.com/

## Dash apps for machine learning models
* https://knn-iris-classifier.herokuapp.com/
* https://tmdb-rf-genres.herokuapp.com/
* https://ames-housing-linear-reg.herokuapp.com/
* https://loan-approval-classifier.herokuapp.com/

#### Official Resources from Plotly:  
[Introducing Plotly Dash](https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503)  
[Youtube: Dash in 5 minutes](https://www.youtube.com/watch?v=e4ti2fCpXMI)  
[Dash User Guide](https://dash.plot.ly/)  
[Dash Workshop, Washington DC Edition - June 9-10, 2018](https://dash-workshop.plot.ly/)  
[Chris Parmer's github repo for Dash](https://github.com/plotly/dash-docs)  
[Dash Community Forum - like StackOverflow for Dash](https://community.plot.ly/c/dash)  
[Gallery of Dash apps](https://dash.plot.ly/gallery)  

#### Additional resources for learning Dash  
[Dash Workbook by Jose Portilla](https://docs.google.com/document/d/1DjWL2DxLiRaBrlD3ELyQlCBRu7UQuuWfgjv9LncNp_M/edit)  
[Github Repo by Jose Portilla](https://github.com/Pierian-Data/Plotly-Dashboards-with-Dash)   
[Using Dash to build public sector dashboards](https://medium.com/a-r-g-o/using-plotlys-dash-to-deliver-public-sector-decision-support-dashboards-ac863fa829fb)  
