
import os
import sys
import yaml
import tempfile
import subprocess

from quarto.quarto import find_quarto

def render_to_path(input,
           output_format = None,
           output_file = None,
           execute = True,
           execute_params = None,
           execute_dir = None,
           cache = None,
           cache_refresh = False,
           kernel_keepalive = None,
           kernel_restart = False,
           debug = False,
           quiet = False,
           pandoc_args = None,
           output_dir_path=None):

  render(input=input,
           output_format=output_format,
           output_file=output_file,
           execute=execute,
           execute_params=execute_params,
           execute_dir=execute_dir,
           cache=cache,
           cache_refresh=cache_refresh,
           kernel_keepalive=kernel_keepalive,
           kernel_restart=kernel_restart,
           debug=debug,
           quiet=quiet,
           pandoc_args=pandoc_args)

  if output_dir_path is not None:
    output_file_path = os.path.join(output_folder, output_file)
    if output_file is None:
      output_file = os.path.basename(input)
    os.makedirs(output_dir_path, exist_ok=True)
    os.rename(output_file, output_file_path)

  return output_file_path

def render(input,
           output_format = None,
           output_file = None,
           execute = True,
           execute_params = None,
           execute_dir = None,
           cache = None,
           cache_refresh = False,
           kernel_keepalive = None,
           kernel_restart = False,
           debug = False,
           quiet = False,
           pandoc_args = None):

  # params file to remove after render
  params_file = None

  # build args
  args = ["render", input]
  
  if output_format is not None:
    args.extend(["--to", output_format])
  
  if output_file is not None:
    args.extend(["--output", output_file])
  
  if execute is not None:
    if execute is True:
      args.append("--execute")
    elif execute is False:
      args.append("--no-execute")
  
  if execute_params is not None:
    params_file = tempfile.NamedTemporaryFile(mode = 'w',
                                              prefix="quarto-params", 
                                              suffix=".yml",
                                              delete=False)
    yaml.dump(execute_params, params_file)
    params_file.close()
    args.extend(["--execute-params", params_file.name])                                          

  if execute_dir is not None:
    args.extend(["--execute-dir", execute_dir])

  if cache is not None:
    if cache is True:
      args.append("--cache")
    elif cache is False:
      args.append("--no-cache")
  
  if cache_refresh is True:
    args.append("--cache-refresh")

  if kernel_keepalive is not None:
    args.extend(["--kernel-keepalive", str(kernel_keepalive)])
 
  if kernel_restart is True:
    args.append("--kernel-restart")

  if debug is True:
    args.append("--debug")
   
  if quiet is True:
    args.append("--quiet")
 
  # run process
  try:
    process = subprocess.Popen([find_quarto()] + args)
    process.wait()
  finally:
    if params_file is not None:
      os.remove(params_file.name)

