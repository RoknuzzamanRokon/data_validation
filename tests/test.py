import panel as pn
import hvplot.pandas as hvplot
import pandas as pd
from sqlalchemy import create_engine

# Connect to your database
engine = create_engine('sqlite:///your_database.db')

# Query the database
query = "SELECT * FROM your_table"
df = pd.read_sql(query, engine)

# Create a simple panel dashboard
pn.extension()
dashboard = pn.Column(
    pn.Row(
        pn.panel(df.hvplot())
    )
)

# Display the dashboard
dashboard.servable()
