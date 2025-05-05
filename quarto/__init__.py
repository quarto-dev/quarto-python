# __init__.py

# Version of the quarto package
__version__ = "0.1.0"

from quarto.quarto import path
from quarto.render import render
from quarto.metadata import metadata
from quarto.theme import theme_colors_altair, theme_brand_altair, \
    theme_colors_bokeh, theme_brand_bokeh, \
    theme_colors_great_tables, theme_brand_great_tables, \
    theme_colors_matplotlib, theme_brand_matplotlib, \
    theme_colors_plotnine, theme_brand_plotnine, \
    theme_colors_plotly, theme_brand_plotly, \
    theme_colors_pygal, theme_brand_pygal, \
    theme_colors_seaborn, theme_brand_seaborn
