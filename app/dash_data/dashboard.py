from dash import Dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd

class Dashboard(Dash):
    def __init__(self, server, url_base_pathname, path):
        super().__init__(server=server, url_base_pathname=url_base_pathname)
        self.layout = self.create_layout(path)

    @staticmethod
    def create_layout(path):

        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
        
        return html.Div([ 
                dash_table.DataTable(df.to_dict('records'), page_size=10) 
            ])
    

    @staticmethod
    def get(server, url_base_pathname):
        dash_app = Dashboard(server=server, url_base_pathname=url_base_pathname, path=1)
        return dash_app