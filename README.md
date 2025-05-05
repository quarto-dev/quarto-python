# quarto-python

Python interface to the Quarto CLI (https://quarto-dev/quarto-cli). 



## theme helpers

`quarto-python` contains theme helpers to do basic background/foreground theming of plots and tables

The `theme_colors_*` functions take background and foreground colors:

| parameter | description |
| --------- | ----------- |
| `bg` | background color |
| `fg` | foreground color |

The `theme_brand_*` functions take a [brand.yml](https://posit-dev.github.io/brand-yml/) file:

| parameter | description |
| --------- | ----------- |
| `brand_yml` | path to **brand.yml** file |

Available theme helpers:

| colors | brand |
| --------- | ----------- |
| `theme_colors_altair` | `theme_brand_altair` |
| `theme_colors_bokeh` | `theme_brand_bokeh` |
| `theme_colors_great_tables` | `theme_brand_great_tables` |
| `theme_colors_matplotlib` | `theme_brand_matplotlib` |
| `theme_colors_plotnine` | `theme_brand_plotnine` |
| `theme_colors_plotly` | `theme_brand_plotly` |
| `theme_colors_pygal` | `theme_brand_pygal` |
| `theme_colors_seaborn` | `theme_brand_seaborn` |

The usage of the returned object or function depends on the package. See this repo for usage examples:

https://github.com/quarto-dev/quarto-examples/tree/main/renderings