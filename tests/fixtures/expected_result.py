PLAIN_JSON_1_2 = '''{
  - follow : False
    host : hexlet.io
  - proxy : 123.234.53.22
  - timeout : 50
  + timeout : 20
  + verbose : True
}'''

PLAIN_JSON_2_1 = '''{
  + follow : False
    host : hexlet.io
  + proxy : 123.234.53.22
  - timeout : 20
  + timeout : 50
  - verbose : True
}'''

PLAIN_YAML_1_2 = '''{
  - age : 30
  + age : 25
    city : New York
  - country : USA
  + country : United States
    is_student : True
    name : John Doe
  - street : 123 Main St
}'''

PLAIN_YAML_2_1 = '''{
  - age : 25
  + age : 30
    city : New York
  - country : United States
  + country : USA
    is_student : True
    name : John Doe
  + street : 123 Main St
}'''