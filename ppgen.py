# File:      ppgen.py
# Author:    Bruce Belson
# Copyright: TODO
# Version:   1.1
# Date:      26-Jul-2021

# Notes:
# templates are stored in [exedir]/templates
# templates are generated into [pwdir]/proj_name
# $ symbols in templates must be escaped: $$
# Each file in the template list may be copied or templated
# Template list:
# [ template-file, destination-folder, destonation-file, is_copied ] 

# import os
from string import Template
from pathlib import Path
from datetime import date
import getpass

# Generate a single file from template and dictionary of substitutions
def gen_file(in_path, out_path, dict, is_copied):
  src = in_path.read_text()
  if is_copied:
    result = src
  else:
    src = Template(src)
    result = src.substitute(dict)
  out_path.write_text(result)

# Generate all output files into a new sub-folder, using template list 
def gen_project(templates, in_root, out_root, dict):
  # Create output folder
  Path(out_root).mkdir(parents=True, exist_ok=True)
  # Process each template
  for template in templates:
    Path(out_root / template[1]).mkdir(parents=True, exist_ok=True)
    gen_file(Path(in_root) / template[0], Path(out_root) / template[1] / template[2], dict, template[3])

# Run the main function
def main(proj_name, libraries, debug_type):
  exedir = Path(__file__).parent
  pwdir = Path.cwd()
  tpldir = exedir / 'templates'

  dict = {
    'project': proj_name, 
    'dt': date.today().strftime("%d-%b-%Y"),
    'user': getpass.getuser(),
    'libs': libraries
    }
  templates = [
    ['main.c', '.', 'main.c', False],
    ['CMakeLists.txt', '.', 'CMakeLists.txt', False],
    ['pico_sdk_import.cmake', '.', 'pico_sdk_import.cmake', True] 
  ]
  # TODO - append debug stuff
  gen_project(templates, tpldir, pwdir / proj_name, dict)

# TODO - add cmd line switches

main('Lab7', 'hardware_pwm hardware_pio', 'picoprobe')
