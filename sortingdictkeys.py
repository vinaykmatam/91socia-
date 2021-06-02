import json

dict = {'e' : "hello world",
        'a' : "good morning",
        'd' : "good  afternoon",
        'c' : " good night",
         '1'  : "Hi!"
        }

json_data = json.dumps(dict,sort_keys=True,indent=4)
print(json_data)
    
