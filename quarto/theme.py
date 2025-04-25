import yaml
import plotly.graph_objects as go
from functools import partial

def plotly_theme_colors(bg, fg):
  return go.layout.Template({'layout': {
    'paper_bgcolor': bg,
    'plot_bgcolor': bg,
    'font_color': fg,
  }})

def plotly_theme_brand(brand_yml):
  brand = yaml.safe_load(open(brand_yml).read())
  return plotly_theme_colors(brand["color"]["background"], brand["color"]["foreground"])
