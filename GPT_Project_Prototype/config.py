def clear(args):
    # control if function is called or not
    color = list(args.values())[0]
    direction = list(args.values())[1]
    print("===> clear(color) function is called correctly.", color, direction + "\n")

def pickUp(args):
    # control if function is called or not
    color = list(args.values())[0]
    print("===> pickUp(color) function is called correctly with argument ", color + "\n") # f-string

def place(args):
    x = args.get("x")
    y = args.get("y")
    z = args.get("z")
    # control if function is called or not
    print("===> place(position_x, position_y, position_z) function is called correctly.",str(x), str(y), str(z) + "\n")

def putOn(args):
    # control if function is called or not
    print("===> putOn(color_1, color_2) function is called correctly." + "\n")

def push(args):
    # control if function is called or not
    print("===> push(color,direction) function is called correctly." + "\n")

def position(args):
  return 1,5,3

def give(args):
    # control if function is called or not
    print("===> give() function is called correctly." + "\n")


# taken/picked-up

functions = [
          {
          "name": "multi_Func",
          "description": "Call arbitrary number of functions in one call",
          "parameters": {
              "type": "object",
              "properties": {

                #   "clear": {
                #       "name": "clear",
                #       "description": "Before take the any object check if there are any other objects around the block of the desired color.",
                #       "parameters": {
                #           "type": "object",
                #           "properties": {
                #               "color": {
                #                   "type": "string",
                #                   "description": "The color of the object whose surroundings will be checked, e.g. 'blue', 'red', 'green' ",
                #               },
                #           },
                #           "required": ["color"],
                #       },
                #   },

                  "pickUp": {
                      "name": "pickUp",
                      "description": "Pick up the desired color object.",
                      "parameters": {
                          "type": "object",
                          "properties": {
                              "color": {
                                  "type": "string",
                                  "description": "The color of the object to be picked up. It could be only one of these: 'blue', 'red', 'green' ",
                              },
                          },
                          "required": ["color"],
                      },
                  },
                  
                  "place": {
                      "name": "place",
                      "description": "Move the desired color object to the specified x y z position.",
                      "parameters": {
                          "type": "object",
                          "properties": {
                              "position_x": {
                                  "type": "float",
                                  "description": "The x value of the target position in range of (0.6, 0.8), e.g. 0.648.",
                              },
                              "position_y": {
                                  "type": "float",
                                  "description": "The y value of the target position in range of (-0.1, 0.5), e.g. 0.2.",
                              },
                              "position_z": {
                                  "type": "float",
                                  "description": "The z value of the target position in range of (-12, -0.1), e.g. -0.1.",
                              },
                          },
                          "required": ["position_x", "position_y", "position_z"],
                      },
                  },

                  "putOn": {
                      "name": "putOn",
                      "description": "Place the picked object onto an object with specified color.",
                      "parameters": {
                          "type": "object",
                          "properties": {
                            #   "picked_color": {
                            #       "type": "string",
                            #       "description": "The color of the object to be picked up, e.g. 'blue', 'red', 'green' ",
                            #   },
                              "specified_color": {
                                  "type": "string",
                                  "description": "The color of target object which taken block will be placed. It could be only one of these: 'blue', 'red', 'green' ",
                              },
                          },
                          "required": ["specified_color"],
                      },
                  },

                  "push": {
                      "name": "push",
                      "description": "Topple the structure made of objects by pushing the block of the desired color and in the desired direction.",
                      "parameters": {
                          "type": "object",
                          "properties": {
                              "color": {
                                  "type": "string",
                                  "description": "The color of the object to be pushed, e.g. 'blue', 'red', 'green' ",
                              },
                              "direction": {
                                  "type": "string",
                                  "description": " The direction of the push. It could be only one of these: +x, -x, +y, -y",
                              },
                              "distance": {
                                  "type": "float",
                                  "description": "The amount of the displacement in the given direction in centimetre.",
                              },
                          },
                          "required": ["color"],
                      },
                  },

                  "give": {
                    "name": "give",
                    "description": "Take the desired color object then move it to the someone.",
                    "parameters": "null"
                  }

              }, "required": ["clear", "pickUp", "place", "putOn", "push", "give"],
          }
      }
]

available_functions = {
        "pickUp": pickUp,
        "place": place,
        "putOn": putOn,
        "push": push,
        "give": give,
        # add you other avaliable functions
}

explanations_of_predicates = "obj(x) represent, x is an object. color(x,'red') represent, x object is red."
# position(x, 0.1, 0.2, 0) represent, x object is in the position x=0.1 y=0.2 z=0."
predicates = {
    "obj(1)",
    "obj(2)",
    "obj(3)",
    "color(1,'red')",
    "color(2,'blue')",
    "color(3,'green')"
    # "positions(1, 0.75, 0.2, -0.1))",
    # "positions(2, 0.78, 0.1, -0.1))",
    # "positions(3, 0.73, 0.3, -0.1))"
}