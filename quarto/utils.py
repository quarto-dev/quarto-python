import yaml

def as_yaml(x):
  return yaml.dump(
    x,
    default_flow_style=False,
    allow_unicode=True,
    sort_keys=False
  )


def as_yaml_block(x):
  yaml_content = as_yaml(x)
  return f"---\n{yaml_content}---\n"


