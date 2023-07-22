import json

import pandas as pd
import plotly.colors
import plotly.graph_objs as go
import requests

from .AppConfig import api_config
from .Security import Security

from .inference import inf


def get_response(keyword):
    res, ft, sh  = inf.get_inf(keyword)
    # print(res)
    # res_json = json.loads(res)
    return res, ft, sh




def return_figures(keyword):
    """Creates four plotly visualizations using the The Movie DataBase API

    # Example of the The Movie DataBase API endpoint:
    # Fetch relevant movies for a keyword query input
    #

      Args:
          keyword (string): keyword for fetching relevant movies

      Returns:
          list (dict): list containing the four plotly visualizations

    """

    # when the keyword variable is empty, use the default keyword 'hero'
    # if not bool(keyword):
    #     keyword = 'hero'

    # result_df = get_result_df(keyword)

    # first chart gives top five relevant movies wrt popularity
    # print(keyword)
    # print(f"Predictions {get_response(keyword)}")
    prediction, ft, sh  = get_response(keyword)

    df = pd.DataFrame()
    df["features"] = ft
    df["shaps"] = sh
    df = df.sort_values(["shaps"],ascending=False)
    df = df[:10]
    # y_val = ft[:10]
    # x_val = sh[:10]
    graph_one = []
    graph_one.append(
        go.Bar(
            x=df["features"], y=df["shaps"]
        )
    )

    layout_one = dict(title='Features with least contribution to prediction',
                      xaxis=dict(title='Features', automargin=True),
                      yaxis=dict(title='Shap Values'),
                      )
    # # second chart plots Top Five Relevant Movies for the given keyword wrt average vote rating
    # x_val_2 = [1,2,3,4]
    # y_val_2 = [3,6,7,8]

    # graph_two = []
    # graph_two.append(
    #     go.Bar(
    #         x=x_val_2,
    #         y=y_val_2,
    #     )

    # )
    # layout_two = dict(title='Top Five Relevant Movies for the given keyword wrt <br> average vote rating',
    #                   xaxis=dict(title='Movie', automargin=True ),
    #                   yaxis=dict(title='Average Vote Rating'),
    #                   )

    # # third chart plots Top Five Relevant Movies for the given keyword wrt vote count

    # # for_plot_3 = result_df.sort_values(['vote_count'], ascending=False)[:5]
    # x_val_3 = [1,2,3,4]
    # y_val_3 = [3,6,2,9]

    # graph_three = []
    # graph_three.append(
    #     go.Bar(
    #         x=x_val_3,
    #         y=y_val_3,
    #     )

    # )
    # layout_three = dict(title='Top Five Relevant Movies for the given keyword wrt vote count',
    #                     xaxis=dict(title='Movie',automargin=True ),
    #                     yaxis=dict(title='Vote Count'),
    #                     )

   
    

    # append all charts
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    # figures.append(dict(data=graph_two, layout=layout_two))
    # figures.append(dict(data=graph_three, layout=layout_three))
    

    return figures
