# %%
# Setup the Jupyter version of Dash
from jupyter_dash import JupyterDash

# Configure the necessary Python module imports for dashboard components
import dash_leaflet as dl
from dash import dcc
from dash import html
import plotly.express as px
from dash import dash_table
from dash.dependencies import Input, Output, State
import base64

# Configure OS routines
import os

# Configure the plotting routines
import numpy as np
import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

# Enhancement for Milestone Four begins

#Begin Indexing
FUNCTION createIndex(field):
 INDEX = self.database.animals.create_index({field: 1})

 RETURN INDEX 

 END FUNCTION
 
#Aggregation Pipeline for Queries
FUNCTION getAnimalStats():
 PIPELINE = [
    { "$match": { "adopted": False } },
    { "$group": { "_id": "$breed", "count": { "$sum": 1 } } },
    { "$sort": { "count": -1 } }
     ] 
 RESULT = self.database.animals.aggregate(PIPELINE)

RETURN RESULT 

END FUNCTION

#Begin User Authentication 
FUNCTION authenticate(username, password):
USER = self.database.users.find_one({ "username": username, "password": password })
IF USER EXISTS:
 RETURN USER.role

  ELSE:
   THROW AuthenticationException

 END FUNCTION

#Restrict Access to Some Operations
 FUNCTION
updateAnimalRecord(data, newData, role):
 IF role == "admin":
  RESULT = self.database.animals.findOneAndUpdate(data, { "$set": newData })
   RETURN RESULT

    ELSE:
     THROW PermissionException

END FUNCTION


# change animal_shelter and AnimalShelter to match your CRUD Python module file name and class name
from CRUD import AnimalShelter

###########################
# Data Manipulation / Model
###########################
# update with your username and password and CRUD Python module name

username = "aacuser"
password = "passw0rd1"

# Connect to database via CRUD Module
db = AnimalShelter(username, password)

# class read method must support return of list object and accept projection json input
# sending the read method an empty document requests all documents be returned
df = pd.DataFrame.from_records(db.read({}))

# MongoDB v5+ is going to return the '_id' column and that is going to have an 
# invlaid object type of 'ObjectID' - which will cause the data_table to crash - so we remove
# it in the dataframe here. The df.drop command allows us to drop the column. If we do not set
# inplace=True - it will reeturn a new dataframe that does not contain the dropped column(s)
#df.drop(columns=['_id'],inplace=True)

## Debug
# print(len(df.to_dict(orient='records')))
# print(df.columns)


#########################
# Dashboard Layout / View
#########################
app = JupyterDash('SimpleExample')

# Added in Grazioso Salvare’s logo
image_filename = 'Grazioso Salvare Logo.png' 
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


app.layout = html.Div([
    html.Hr(),
    html.Center(html.Img(id='customer-image',src='data:image/png;base64,{}'.format(encoded_image.decode()),alt='customer image')),
    html.Center(html.B(html.H1('Tanya Noyes SNHU CS-340 Dashboard'))),
    html.Div( # Adding Radio Buttons
        dcc.RadioItems(
            id='filter-type',
            options=[
                {'label':'Water Rescue', 'value': 'water'},
                {'label': 'Mountain Rescue', 'value': 'mount'},
                {'label': 'Disaster Rescue and Individual Tracking', 'value': 'disaster'},
                {'label': 'Reset', 'value': 'reset'},
            ],
            value= 'reset'
            
        )
    
    ),
        
    html.Hr(),
    dash_table.DataTable(
                id='datatable-id',
                columns=[
                    {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
                ],
                data=df.to_dict('records'),
                editable=True,
                filter_action="native", 
                sort_action="native", 
                column_selectable=False,
                row_selectable="single",
                selected_columns=[],
                selected_rows=[],
                page_action="native",
                page_current=0,
                page_size=10,
    ),
  
    html.Br(),
    html.Hr(),
#This sets up the dashboard so that your chart and your geolocation chart are side-by-side
    html.Div(className='row',
         style={'display' : 'flex'},
             children=[
        html.Div(
            id='graph-id',
            className='col s12 m6',

            ),
        html.Div(
            id='map-id',
            className='col s12 m6',
            )
        ])
])

#############################################
# Interaction Between Components / Controller
#############################################

    
@app.callback([Output('datatable-id','data'),
               Output('datatable-id', 'columns')],
              [Input('filter-type', 'value')])
    
def update_dashboard(filter_type):
        # Water Rescue Filter
        if filter_type == 'water':
            df = pd.DataFrame.from_records(animals.read({
                "animal_type": "Dog",
                "breed": {"$in": ["Labrador Retriever Mix","Chesapeake Bay Retriever", "Newfoundland"
                                 ]},
                "sex_upon_outcome": "Intact Female",
                "age_upon_outcome_in_weeks": {"$gte":26.0, "$lte":156.0}
            }))
        # Mountain or Wilderness Rescue filter
        elif filter_type == 'mount':
            df = pd.DataFrame.from_records(animals.read({
                "animal_type": "Dog",
                "breed": {"$in": ["German Shepard","Alaskan Malamute","Old English Sheepdog", 
                                  "Siberian Husky", "Rottweiler"
                                 ]},
                "sex_upon_outcome": "Intact Male",
                "age_upon_outcome_in_weeks": {"$gte":26.0, "$lte":156.0}
            }))
               
        # Disaster Rescue or Individual Tracking filter
        elif filter_type == 'disaster':
            df = pd.DataFrame.from_records(animals.read({
                "animal_type": "Dog",
                "breed": {"$in": ["Doberman Pinscher","German Shepard","Golden Retriever", 
                                  "Bloodhound","Rottweiler"
                                 ]},
                "sex_upon_outcome": "Intact Male",
                "age_upon_outcome_in_weeks": {"$gte":20.0, "$lte":300.0}
            }))
               
        # Reset to no filter
        else:
            df = pd.DataFrame.from_records(animals.read({}))
     
            columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns]
            data=df.to_dict('records')
               
            return (data,columns)

# Display the breeds of animal based on how many are represented in the table 
@app.callback(
    Output('graph-id', "children"),
    [Input('datatable-id', "derived_viewport_data"),
     #Input('filter-type', 'value')
    ])
def update_graphs(viewData):
    ###FIX ME ####
    # add code for chart of your choice (e.g. pie chart) #
    dff = pd.DataFrame.from_dict(viewData)
    
    return [
        dcc.Graph(            
#             figure = px.pie(dff, values='breed',  
#                             title='Available Dogs by Breed')
            figure = px.histogram(dff, x='breed')
        )    
    ]
   
#This callback will highlight a cell on the data table when the user selects it
@app.callback(
    Output('datatable-id', 'style_data_conditional'),
    [Input('datatable-id', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]


# This callback will update the geo-location chart for the selected data entry
# derived_virtual_data will be the set of data available from the datatable in the form of 
# a dictionary.
# derived_virtual_selected_rows will be the selected row(s) in the table in the form of
# a list. For this application, we are only permitting single row selection so there is only
# one value in the list.
# The iloc method allows for a row, column notation to pull data from the datatable

@app.callback(
    Output('map-id', "children"),
    [Input('datatable-id', "derived_virtual_data")])
def update_map(viewData):
    dff = pd.DataFrame.from_dict(viewData)
    # Austin TX is at [30.75,-97.48]
    return [
        dl.Map(style={'width': '1000px', 'height': '500px'}, center=[30.75,-97.48], zoom=10, children=[
            dl.TileLayer(id="base-layer-id")] +
            # Marker with tool tip and popup
            [dl.Marker(position=[row['location_lat'],row['location_long']], children=[
                dl.Tooltip(row['breed']),
                dl.Popup([
                     html.H1("Animal Name"),
                     html.P(row['name'])
                ])
            ]) for index, row in dff.iterrows()]
        )
    ]

    


app.run_server(debug=True)


# %%



