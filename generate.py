# gradle-update
# Copyright (C) 2025 Benjamin Schmitz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import jinja2
import yaml

dataFile = "data.yml"
templateFile = "script.sh.j2"
resultFile = "script.sh"

with open(dataFile) as file:
    exercises = yaml.safe_load(file)["exercises"]

print(exercises)

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template(templateFile)

result = template.render(exercises=exercises, types=["tests", "solution", "exercise"])
print(result)
with open(resultFile, "w") as file:
    file.write(result)
