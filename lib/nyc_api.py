
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "https://data.cityofchicago.org/resource/f7f2-ggz5.json"

    response = requests.get(URL)
    return response.content
  def program_school(self):
    #we use the JSON library to parse the API response into nicely formatted JSON
    program_list=[]
    programs =json.loads(self.get_programs())
    for program in programs:
      program_list.append(program["station_name"])
    return program_list

# programs = GetPrograms().get_programs()
# print(programs)
programs = GetPrograms()
programs_schools = programs.program_school()
for school in set(programs_schools):
  print(school)