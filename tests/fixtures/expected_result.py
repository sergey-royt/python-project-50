PLAIN_1_2 = '''{
  - follow : False
    host : hexlet.io
  - proxy : 123.234.53.22
  - timeout : 50
  + timeout : 20
  + verbose : True
}'''

PLAIN_2_1 = '''{
  + follow : False
    host : hexlet.io
  + proxy : 123.234.53.22
  - timeout : 20
  + timeout : 50
  - verbose : True
}'''