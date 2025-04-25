import yaml
from functools import partial

def theme_colors_altair(bg, fg):
  return {
    'config': {
      'view': {'stroke': 'transparent'},
      'axis': {
        'domainColor': fg,
        'labelColor': fg,
        'titleColor': fg,
      },
      'legend': {
        'labelColor': fg,
        'titleColor': fg,
      },
      'background': bg,  # Background color
    }
  }

def theme_brand_altair(brand_yml):
    brand = yaml.safe_load(open(brand_yml).read())
    bg = brand["color"]["background"]
    fg = brand["color"]["foreground"]
    return partial(theme_colors_altair, bg, fg)

# background fill is incomplete
def theme_colors_bokeh(bg, fg):
  from bokeh.io import curdoc
  from bokeh.themes import Theme
  curdoc().theme = Theme(json={'attrs': {
    'figure': {
      'background_fill_color': bg, # just plot area
    },
    'Title': {
      'background_fill_color': bg,
      'text_color': fg,
    },
    'Axis': {
      'background_fill_color': bg,
      'axis_label_text_color': fg,
      'major_label_text_color': fg,
    },
  }})

def theme_brand_bokeh(brand_yml):
  brand = yaml.safe_load(open(brand_yml).read())
  fg = brand["color"]["foreground"]
  bg = brand["color"]["background"]
  return partial(theme_colors_bokeh, bg, fg)


def theme_colors_great_tables(bg, fg):
  return {
    'table_background_color': bg,
    'table_font_color': fg
  }
def theme_brand_great_tables(brand_yml):
  brand = yaml.safe_load(open(brand_yml).read())
  fg = brand["color"]["foreground"]
  bg = brand["color"]["background"]
  return theme_colors_great_tables(bg, fg)


def theme_colors_matplotlib(bg, fg, primary):
  import matplotlib as mpl
  from cycler import cycler
  mpl.rcParams["axes.facecolor"] = bg
  mpl.rcParams["axes.edgecolor"] = fg
  mpl.rcParams["axes.labelcolor"] = fg
  mpl.rcParams["axes.titlecolor"] = fg
  mpl.rcParams["figure.facecolor"] = bg
  mpl.rcParams["figure.edgecolor"] = fg
  mpl.rcParams["text.color"] = fg
  mpl.rcParams["xtick.color"] = fg
  mpl.rcParams["ytick.color"] = fg
  if primary:
    mpl.rcParams["axes.prop_cycle"] = cycler('color', [primary])


def theme_brand_matplotlib(brand_yml):
  brand = yaml.safe_load(open(brand_yml).read())
  return partial(
    theme_colors_matplotlib,
    brand["color"]["background"],
    brand["color"]["foreground"],
    brand["color"]["primary"],
  )


def theme_colors_plotnine(bg, fg):
  from plotnine import theme, element_rect, element_text
  return theme(
    plot_background=element_rect(fill=bg, size=0),
    text=element_text(color=fg)
  )

def theme_brand_plotnine(brand_yml):
  brand = yaml.safe_load(open(brand_yml).read())
  return theme_colors_plotnine(brand["color"]["background"], brand["color"]["foreground"])


def theme_colors_plotly(bg, fg):
  import plotly.graph_objects as go
  return go.layout.Template({'layout': {
    'paper_bgcolor': bg,
    'plot_bgcolor': bg,
    'font_color': fg,
  }})

def theme_brand_plotly(brand_yml):
  brand = yaml.safe_load(open(brand_yml).read())
  return theme_colors_plotly(brand["color"]["background"], brand["color"]["foreground"])


def theme_colors_pygal(_bg, fg, primary, secondary):
  from pygal.style import Style
  return Style(
    background='transparent',
    plot_background='transparent',
    foreground=fg,
    foreground_strong=primary,
    foreground_subtle=secondary or '#630C0D',
    opacity='.6',
    opacity_hover='.9',
    transition='400ms ease-in',
    colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))

def theme_brand_pygal(brand_yml):
  brand = yaml.safe_load(open(brand_yml).read())
  return theme_colors_pygal(
    brand["color"]["background"],
    brand["color"]["foreground"],
    brand["color"]["primary"],
    brand["color"].get("secondary"),
  )


def theme_colors_seaborn(bg, fg):
  # seaborn accepts matplotlib rcparams
  return {
      "axes.facecolor": bg,
      "axes.edgecolor": fg,
      "axes.labelcolor": fg,
      "axes.titlecolor": fg,
      "figure.facecolor": bg,
      "figure.edgecolor": fg,
      "text.color": fg,
      "xtick.color": fg,
      "ytick.color": fg,
      "grid.color": fg,
  }

def theme_brand_seaborn(brand_yml):
    brand = yaml.safe_load(open(brand_yml).read())
    return theme_colors_seaborn(brand["color"]["background"], brand["color"]["foreground"])
