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

  combined_content = explanations_of_predicates + "\n" + "\n".join(predicates["objects"]) + "\n" + "\n".join(predicates["colors"]) + "\n" + "\n".join(predicates["states"]) + "\n" + "\n".join(predicates["positions"]) + "\n" + user_request
  messages = [{"role": "system", "content": "You are an assistant that always replies with multiple function calls in straight JSON format ready to parsed. Respond to user request based on predicates."},
              {"role": "user", "content": combined_content}]
  
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
      function_to_call = avaliable_functions[function_name]
      print("function_name: " + function_name)
      print("args: ", args)
      function_to_call(args)

user_request_1 = "Could you pick the blue block and then put onto red block?"
user_request_2 = "could you take down the tower of blocks with the blue block in left direction ?"
user_request_3 = "Take the blue block."

run_conversation(user_request = user_request_3)
# print("\n\nFinal GPT output:\n" + a)