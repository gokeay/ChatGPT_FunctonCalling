import openai
import json
import apiKeys
import os
import sys
import config

functions = config.functions
avaliable_functions = config.available_functions
explanations_of_predicates = config.explanations_of_predicates
predicates = config.predicates
openai.api_key = apiKeys.OPENAI_API_KEY

# Variable to clear the order in which the function is called
seq_of_func = 1


# main function which is called by user
def run_conversation(user_request):

  combined_content = explanations_of_predicates + "\n" + "\n".join(predicates) + "\n" + user_request
  messages = [{"role": "system", "content": "You are the assistant that always reply with multiple function calls with only arguments of functions (If a function doesn't take input, definitely don't return an argument.) in string format instead of dictionary. For example; instead of {'color': 'blue', 'direction': '+x'} return blue +x. Only reply with given function parameters."},
              #  + explanations_of_predicates + "Use predicaters to vizualize the environment to take action."},
              #  You are an assistant that always replies with multiple function calls in straight JSON format ready to parsed. 
              {"role": "user", "content": user_request}]
  
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0613",
      messages=messages,
      functions=functions,
      function_call="auto",
      temperature=0.0,
  )
  print("\n" + "Respone: " + str(response) + "\n" + "\n" + "\n")
  
  baxter_message = "pauseInterpreter;"
  
  response_message = response["choices"][0]["message"]
  # print("Respone_message: "  + str(response_message) + "\n" + "\n" + "\n")
  print("Respone_message: " + str(response_message) + "\n\n\n")
  

  if response_message.get("function_call"):
    function_args_str = response_message["function_call"]["arguments"]
    function_args = json.loads(function_args_str)

    for function_name, args in function_args.items():
      # function_to_call = avaliable_functions[function_name]
      baxter_message += function_name
      baxter_message += " "
      baxter_message += str(args)
      baxter_message += ";"
      print("function_name: " + function_name)
      print("args: ", args)


      # function_to_call(args)
  baxter_message +="homePosition;pauseInterpreter"
  print("baxter_message: " + baxter_message)
  
user_request_1 = "There are red and blue boxes on the table. Pick the blue box and then put onto red box."
user_request_2 = "There are red and blue boxes on the table. Take down the tower of blocks with the blue block in +x direction."
user_request_3 = "There are red and blue boxes on the table. Take the blue block."
user_request_4 = "Move the blue block to the x=4, y=3, z=0."
user_request_5 = "There are red and blue boxes on the table. Give the blue box to me."

run_conversation(user_request = user_request_1)
# print("\n\nFinal GPT output:\n" + a)