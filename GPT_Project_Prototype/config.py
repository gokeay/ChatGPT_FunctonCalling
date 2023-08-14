def clear(args):
    # control if function is called or not
    print("===> clear(color) function is called correctly." + "\n")

def pick(args):
    # control if function is called or not
    print("===> pick(color) function is called correctly with argument ...." + "\n") # f-string

def place(args):
    x,y,z = args.get("position")
    # control if function is called or not
    print("===> place(position_x, position_y, position_z) function is called correctly." + "\n")

def put_on(args):
    # control if function is called or not
    print("===> put_on(color_1, color_2) function is called correctly." + "\n")

def push(args):
    # control if function is called or not
    print("===> push(color,direction) function is called correctly." + "\n")

def position(args):
  return 1,5,3


# taken/picked-up
# 
functions = [
          {
          "name": "multi_Func",
          "description": "Call arbitrary number of functions in one call",
          "parameters": {
              "type": "object",
              "properties": {

                  "clear": {
                      "name": "clear",
                      "description": "Before take the any object check if there are any other objects around the block of the desired color that the robot arm will pick up, which could obstruct it.",
                      "parameters": {
                          "type": "object",
                          "properties": {
                              "color": {
                                  "type": "string",
                                  "description": "The color of the object whose surroundings will be checked, e.g. 'blue', 'red', 'green' ",
                              },
                          },
                          "required": ["color"],
                      },
                  },

                  "pick": {
                      "name": "pick",
                      "description": "Pick up the desired color object with the robot arm.",
                      "parameters": {
                          "type": "object",
                          "properties": {
                              "color": {
                                  "type": "string",
                                  "description": "The color of the object to be picked up by the robot arm, e.g. 'blue', 'red', 'green' ",
                              },
                          },
                          "required": ["color"],
                      },
                  },
                  
                  "place": {
                      "name": "place",
                      "description": "Move the desired object to the specified x y z position using the robot arm.",
                      "parameters": {
                          "type": "object",
                          "properties": {
                              "position_x": {
                                  "type": "integer",
                                  "description": "The x value of the target position, e.g. 3, 1, 5 ",
                              },
                              "position_y": {
                                  "type": "integer",
                                  "description": "The y value of the target position, e.g. 3, 1 ,5 ",
                              },
                              "position_z": {
                                  "type": "integer",
                                  "description": "The z value of the target position, e.g. 3, 1, 5 ",
                              },
                          },
                          "required": ["position_x", "position_y", "position_z"],
                      },
                  },

                  "put_on": {
                      "name": "put_on",
                      "description": "Place an object of the desired color onto an object of the specified color using the robot arm.",
                      "parameters": {
                          "type": "object",
                          "properties": {
                              "picked_color": {
                                  "type": "string",
                                  "description": "The color of the object to be picked up by the robot arm, e.g. 'blue', 'red', 'green' ",
                              },
                              "target_color": {
                                  "type": "string",
                                  "description": "The color of target object which taken block will be placed by robot arm, e.g. 'blue', 'red', 'green' ",
                              },
                          },
                          "required": ["picked_color", "target_color"],
                      },
                  },

                  "push": {
                      "name": "push",
                      "description": "Topple the structure made of objects by pushing the block of the desired color and in the desired direction by robot arm.",
                      "parameters": {
                          "type": "object",
                          "properties": {
                              "color": {
                                  "type": "string",
                                  "description": "The color of the object to be pushed with the robot arm, e.g. 'blue', 'red', 'green' ",
                              },
                          },
                          "required": ["color"],
                      },
                  }
              }, "required": ["clear", "pick", "place", "put_on", "push"],
          }
      }
]

available_functions = {
        "clear": clear,
        "pick": pick,
        "place": place,
        "put_on": put_on,
        "push": push,
        # add you other avaliable functions
}

explanations_of_predicates = "obj(x) represent, x is an object. color(x,'red') represent, x object is red. near(x,y) represent, x object is near y object. on(x,y) represent, x object is on the top side of y object. position(x, 0.1, 0.2, 0) represent, x object is in the position x=0.1 y=0.2 z=0."

predicates = {
    "objects": {
        "obj(x)",
        "obj(y)",
        "obj(z)"
    },
    "colors": {
        "color(x,'red')",
        "color(y,'blue')",
        "color(z,'green')"
    },
    "states": {
        "near(y,z)",
        "on(y,x)"
    },
    "positions": {
        "positions(x, 0.1, 0.2, 0))",
        "positions(y, 0.1, 0.5, 0))",
        "positions(z, 0.4, 0.5, 0))"
    }
}