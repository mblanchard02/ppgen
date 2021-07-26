# File:      ppgen.py
# Author:    Bruce Belson
# Copyright: See LICENSE in this repository
# Version:   1.1
# Date:      26-Jul-2021

# Notes:
# templates are stored in [exedir]/templates
# templates are generated into [pwdir]/proj_name
# $ symbols in templates must be escaped: $$
# Each file in the template list may be copied or templated
# Template list:
# [ template-file, destination-folder, destonation-file, is_copied ] 

from string import Template
from pathlib import Path
from datetime import date
import getpass
import argparse
from sys import version_info

# Generate a single file from template and dictionary of substitutions
def gen_file(in_path, out_path, dict, is_copied):
  print('gen_file '+str(in_path)+' => '+str(out_path))
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
  picoprobe_templates = [
    ['picoprobe_launch.json', '.vscode', 'launch.json', False]
  ]
  # Append debug material to templates
  if debug_type == 'picoprobe':
    for i in picoprobe_templates: 
      templates.append(i)
  # Generate everything
  gen_project(templates, tpldir, pwdir / proj_name, dict)

# Library list
library_choices = ["pwm", "adc", "uart"]
library_expanded = ["hardware_pwm", "hardware_adc", "hardware_uart"]

def expand_library_list(libs):
  es = []
  flat = [item for sublist in libs for item in sublist]
  for c in flat:
    if c in library_choices:
      es.append(library_expanded[library_choices.index(c)])
  return ' '.join(es)

# Process cmd line switches
pp_version_info = "1.1"
ppgen_desc = f"Pico Project Generator. Version {pp_version_info}." 
parser = argparse.ArgumentParser(description=ppgen_desc)
parser.add_argument("project",help="name of project and of new folder containing project")
# parser.add_argument("-v", "--version", help="show program version", action="store_true")
parser.add_argument("-l", "--library", help="add support library to the make list", 
  choices=library_choices, action="append", nargs='+')
parser.add_argument("-d", "--debugger", help="add debugger support", 
  choices=["picoprobe"])

args = parser.parse_args()

print(args)
print(expand_library_list(args.library))
