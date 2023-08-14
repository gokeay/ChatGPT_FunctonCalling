import openai
import json
import apiKeys
# import yaml
import os
import sys

# with open('config.yaml', 'r') as yaml_file:
#     data = yaml.load(yaml_file, Loader=yaml.FullLoader)

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")
with open(config_path, "r") as config_file:
    json_data = config_file.read()

data = json.loads(json_data)
functions = data['functions']
available_functions = data['available_functions']
print(str(functions)+ "\n" + "\n" + "\n")
print(str(available_functions))


openai.api_key = apiKeys.OPENAI_API_KEY
# Variable to clear the order in which the function is called
seq_of_func = 1

prep = "blocks: x=1; y=2; z=3; 1,2,3='object'; colors: color(1,'red'); color(2,'blue'); color(3,'green'); states: near(2,3); on(2,1); positions: position(1, -0.1, -0.3, 0); position(2, -0.1, 0,2, 0); position(3, 0.3, 0.2, 0);"
prep_json = {
    "blocks": {
        "x": 1,
        "y": 2,
        "z": 3,
        "1,2,3": "object"
    },
    "colors": {
        "1":'red',
        "2":'blue',
        "3":'green'
    },
    "states": {
        "near(2,3)",
        "on(2,1)"
    },
    "positions": {
        "1": "-0.1, -0.3, 0",
        "2": "-0.1, 0.2, 0.2, 0",
        "3": "0.3, 0.2, 0"
    }
}

# def position(args):
#   return 1,5,3

def clear(args):
    global seq_of_func
    # control if function is called or not
    print("{}-   clear(color) function is called correctly.".format(seq_of_func) + "\n")
    seq_of_func += 1

def pick(args):
    global seq_of_func
    # control if function is called or not
    print("{}-   pick(color) function is called correctly with argument {}.".format(seq_of_func,args.get("color")) + "\n")
    seq_of_func += 1

def place(args):
    global seq_of_func
    block,x,y,z = args.get("position")
    # control if function is called or not
    print("{}-   place(position_x, position_y, position_z) function is called correctly.".format(seq_of_func) + "\n")
    seq_of_func += 1

def put_on(args):
    global seq_of_func
    # control if function is called or not
    print("{}-   put_on(color_1, color_2) function is called correctly.".format(seq_of_func) + "\n")
    seq_of_func += 1

def push(args):
    global seq_of_func
    # control if function is called or not
    print("{}-   push(color,direction) function is called correctly.".format(seq_of_func) + "\n")
    seq_of_func += 1

# main function which is called by user
def run_conversation(user_request):

  messages = [{"role": "system", "content": "You are an assistant that always replies with multiple function calls in straight JSON format ready to parsed. Respond to user request based on prep content."},
              {"role": "user", "content": prep + user_request}]
  
  response = openai.ChatCompletion.create( 
      model="gpt-3.5-turbo-0613",
      messages=messages,
      functions=functions,
      function_call="auto",
  )
  print("\n" + "Respone: " + str(response) + "\n" + "\n" + "\n")
  
  response_message = response["choices"][0]["message"]
  print("Respone_message: " + str(response_message) + "\n" + "\n" + "\n")

  if response_message.get("function_call"):
    function_args_str = response_message["function_call"]["arguments"]
    function_args = json.loads(function_args_str)

    for function_name, args in function_args.items():
      function_to_call = available_functions[function_name]
      print("function_name: " + function_name)
      print("args: " + str(args))

      function_to_call(args)

user_request_1 = "Could you pick the blue block and then put onto red block?"
user_request_2 = "could you take down the tower of blocks with the blue block in left direction ?"

run_conversation(user_request = user_request_1)
# print("\n\nFinal GPT output:\n" + a)