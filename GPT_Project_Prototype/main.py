import openai
import json
import apiKeys
# import yaml
import os
import configgg

# with open('config.yaml', 'r') as yaml_file:
#     data = yaml.load(yaml_file, Loader=yaml.FullLoader)
with open("configgg.json", "r") as config_file:
    json_data = config_file.read()

data = json.loads(json_data)
functions = data['functions']
print(functions)

# openai.api_key = apiKeys.OPENAI_API_KEY
# # Variable to clear the order in which the function is called
# seq_of_func = 1

# prep = "blocks: x=1; y=2; z=3; 1,2,3='object'; colors: color(1,'red'); color(2,'blue'); color(3,'green'); states: near(2,3); on(2,1); positions: position(1, -0.1, -0.3, 0); position(2, -0.1, 0,2, 0); position(3, 0.3, 0.2, 0);"
# prep_json = """{	
#     "blocks": {
#         "x": 1,
#         "y": 2,
#         "z": 3,
#         "1,2,3": "object"
#     },
#     "colors": {
#         "color(1,'red')": null,
#         "color(2,'blue')": null,
#         "color(3,'green')": null
#     },
#     "states": {
#         "near(2,3)": null,
#         "on(2,1)": null
#     },
#     "positions": {
#         "position(1, -0.1, -0.3, 0)": null,
#         "position(2, -0.1, 0.2, 0.2, 0)": null,
#         "position(3, 0.3, 0.2, 0)": null
#     }
# }"""	 

# # functions which robot can do
# def position(args):
#   return 1,5,3

# def clear(args):
#     global seq_of_func
#     # control if function is called or not
#     print("{}-   clear(color) function is called correctly.".format(seq_of_func) + "\n")
#     seq_of_func += 1

# def pick(args):
#     global seq_of_func
#     # control if function is called or not
#     print("{}-   pick(color) function is called correctly with argument {}.".format(seq_of_func,args.get("color")) + "\n")
#     seq_of_func += 1

# def place(args):
#     global seq_of_func
#     x,y,z = args.get("position")
#     # control if function is called or not
#     print("{}-   place(position_x, position_y, position_z) function is called correctly.".format(seq_of_func) + "\n")
#     seq_of_func += 1

# def put_on(args):
#     global seq_of_func
#     # control if function is called or not
#     print("{}-   put_on(color_1, color_2) function is called correctly.".format(seq_of_func) + "\n")
#     seq_of_func += 1

# def push(args):
#     global seq_of_func
#     # control if function is called or not
#     print("{}-   push(color,direction) function is called correctly.".format(seq_of_func) + "\n")
#     seq_of_func += 1

# # main function which is called by user
# def run_conversation(user_request):

#   available_functions = {
#           "clear": clear,
#           "pick": pick,
#           "place": place,
#           "put_on": put_on,
#           "push": push,
#           # add you other avaliable functions
#   }
#   messages = [{"role": "system", "content": "You are an assistant that always replies with multiple function calls in straight JSON format ready to parsed. Respond to user request based on prep content."},
#               {"role": "user", "content": prep + user_request}]
#   functions = [
#           {
#           "name": "multi_Func",
#           "description": "Call two functions in one call",
#           "parameters": {
#               "type": "object",
#               "properties": {

#                   "clear": {
#                       "name": "clear",
#                       "description": "Must take color value. Before picking up the block in the selected color, must be clearing if there is an object around the block that could prevent the robot arm from picking up the selected color block.",
#                       "parameters": {
#                           "type": "object",
#                           "properties": {
#                               "color": {
#                                   "type": "string",
#                                   "description": "The color of selected block which will be clear, e.g. blue, red, green, yellow, orange, purple, pink, brown, black, white",
#                               },
#                           },
#                           "required": ["color"],
#                       },
#                   },

#                   "pick": {
#                       "name": "pick",
#                       "description": "If a block needs to be taken, this function works and the block is taken.",
#                       "parameters": {
#                           "type": "object",
#                           "properties": {
#                               "color": {
#                                   "type": "string",
#                                   "description": "The color of block which will be take, e.g. 'blue', 'red', 'green', 'yellow', ...",
#                               },
#                           },
#                           "required": ["color"],
#                       },
#                   },
                  
#                   "place": {
#                       "name": "place",
#                       "description": "If user gives the x, y, z position values for the target position, this function works with given x, y, z position.",
#                       "parameters": {
#                           "type": "object",
#                           "properties": {
#                               "position_x": {
#                                   "type": "integer",
#                                   "description": "The x value of the target position, e.g. 0.1",
#                               },
#                               "position_y": {
#                                   "type": "integer",
#                                   "description": "The y value of the target position, e.g. -0,5",
#                               },
#                               "position_z": {
#                                   "type": "integer",
#                                   "description": "The z value of the target position, e.g. 0.3",
#                               },
#                           },
#                           "required": ["position_x", "position_y", "position_z"],
#                       },
#                   },

#                   "put_on": {
#                       "name": "put_on",
#                       "description": "Must take 2 color value. If the block with the specified color has been successfully picked up and the block of the intended color to be placed is brought over it, the picked-up block is placed onto the target block.",
#                       "parameters": {
#                           "type": "object",
#                           "properties": {
#                               "picked_color": {
#                                   "type": "string",
#                                   "description": "The color of block which picked, e.g. blue, red, green, yellow, orange, purple, pink, brown, black, white",
#                               },
#                               "target_color": {
#                                   "type": "string",
#                                   "description": "The color of target block which received block will be placed, e.g. blue, red, green, yellow, orange, purple, pink, brown, black, white",
#                               },
#                           },
#                           "required": ["picked_color", "target_color"],
#                       },
#                   },

#                   "push": {
#                       "name": "push",
#                       "description": "Robotic arm, by touching the tower made of arranged colored cube blocks with the specified color block, knocks down the tower in the desired direction",
#                       "parameters": {
#                           "type": "object",
#                           "properties": {
#                               "color": {
#                                   "type": "string",
#                                   "description": "The color of block, e.g. blue, red, green, yellow, orange, purple, pink, brown, black, white",
#                               },
#                           },
#                           "required": ["color"],
#                       },
#                   }
#               }, "required": ["clear", "pick", "place", "put_on", "push"],
#           }
#       }
#   ]

#   response = openai.ChatCompletion.create( 
#       model="gpt-3.5-turbo-0613",
#       messages=messages,
#       functions=functions,
#       function_call="auto",
#   )
#   print("\n" + "Respone: " + str(response) + "\n" + "\n" + "\n")
  
#   response_message = response["choices"][0]["message"]
#   print("Respone_message: " + str(response_message) + "\n" + "\n" + "\n")

#   if response_message.get("function_call"):
#     function_args_str = response_message["function_call"]["arguments"]
#     function_args = json.loads(function_args_str)

#     for function_name, args in function_args.items():
#       function_to_call = available_functions[function_name]
#       print("function_name: " + function_name)
#       print("args: " + str(args))

#       function_to_call(args)

#       # if(str(function_name)=="clear"):
#       #   function_to_call(color=args.get("color"))
#       # elif(str(function_name)=="pick"):
#       #   function_to_call(color=args.get("color"))
#       # elif(str(function_name)=="place"):
#       #   function_to_call(color=args.get("color"))
#       # elif(str(function_name)=="put_on"):
#       #   function_to_call(block_color=args.get("block_color"), target_color=args.get("target_color"))
#       # elif(str(function_name)=="push"):
#       #   function_to_call(color=args.get("color"), direction=args.get("direction"))

# user_request_1 = "Could you pick the blue block and then put onto red block?"
# user_request_2 = "could you take down the tower of blocks with the blue block in left direction ?"

# run_conversation(user_request = user_request_1)
# # print("\n\nFinal GPT output:\n" + a)