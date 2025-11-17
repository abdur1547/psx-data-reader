from psx import stocks, tickers
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

import datetime

# Configure Plotly to display in browser
pio.renderers.default = "browser"

print("Fetching stock data...")
# tickers = tickers()

data = stocks("EFERT", start=datetime.date(2010, 1, 1), end=datetime.date.today())
print(f"Data fetched successfully! Shape: {data.shape}")
print(f"Columns: {list(data.columns)}")
print(f"Date range: {data.index[0]} to {data.index[-1]}")

# Create subplots with proper configuration
fig = make_subplots(rows=2,
                    cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.1,
                    subplot_titles=('EFERT Stock Price', 'Trading Volume'),
                    row_heights=[0.7, 0.3])

# Add candlestick chart
print("Creating candlestick chart...")
fig.append_trace(
    go.Candlestick(
        x=data.index,
        open=data.Open,
        high=data.High,
        low=data.Low,
        close=data.Close,
        name="EFERT"
    ), row=1, col=1
)

# Add volume bar chart
print("Adding volume chart...")
fig.add_trace(
    go.Bar(x=data.index,
           y=data.Volume,
           marker_color="green",
           name="Volume",
           showlegend=False),
    row=2,
    col=1
)

# Update layout
fig.update_layout(
    title="EFERT Stock Analysis",
    yaxis_title="Price (PKR)",
    width=1400,
    height=700,
    xaxis_rangeslider_visible=False
)

# Update y-axes
fig.update_yaxes(title_text="Price (PKR)", row=1, col=1)
fig.update_yaxes(title_text="Volume", row=2, col=1)

print("Displaying chart...")
print("Chart should open in your default browser...")

# Try multiple display methods
try:
    fig.show()
    print("✅ Chart displayed successfully!")
except Exception as e:
    print(f"❌ Error displaying chart: {e}")
    print("Trying alternative display methods...")
    
    try:
        # Try saving as HTML and opening
        fig.write_html("efert_chart.html")
        print("✅ Chart saved as 'efert_chart.html' - open this file in your browser")
    except Exception as e2:
        print(f"❌ Error saving HTML: {e2}")
        
    try:
        # Try showing without renderer
        fig.show(renderer="browser")
        print("✅ Chart displayed with browser renderer!")
    except Exception as e3:
        print(f"❌ Browser renderer failed: {e3}")

print("Script completed!")

