
import sys
import json
import subprocess

from quarto.quarto import find_quarto
from quarto.utils import as_yaml_block

def metadata(input):
  args = ["metadata", input, "--json"]
  metadata_json = subprocess.check_output([find_quarto()] + args)
  return json.loads(metadata_json)

def write_yaml_metadata_block(_list=None, **kwargs):
  """Write YAML metadata block that will be parsed by Quarto."""
  meta = kwargs
  if _list is not None:
    meta = {**_list, **kwargs}
  if len(meta) == 0:
    return
  yaml_block = as_yaml_block(meta)
  print(yaml_block)