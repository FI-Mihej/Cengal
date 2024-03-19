# mystrutils.nim

# Import necessary modules from Nim's standard library
import compile_time_py_definitions
import strutils


const apiEndpointDoc {.strdefine: package.apiEndpointDoc}: string = "https://api.example.com"
const apiEndpointDoc2 {.strdefine: package.apiEndpointDoc2}: string = "https://api.example.com"


# This is our module's exported function
proc toUpper*(inputString: string): string =
  when defined(CF_Linux):
    echo "mystrutils: CF_Linux"
  else:
    echo "mystrutils: not CF_Linux"

  when defined(CF_IS_ARM):
    echo "mystrutils: CF_IS_ARM"
  else:
    echo "mystrutils: not CF_IS_ARM"

  echo "API Endpoint: ", apiEndpointDoc
  echo "API Endpoint: URL: https://api.production.com; Path: \\usr\\bin"
  echo "API Endpoint: ", "URL: https://api.production.com; Path: \\usr\\bin"

  echo "API Endpoint2: ", apiEndpointDoc2
  echo "API Endpoint2: https://api.example.com"
  echo "API Endpoint2: ", "https://api.example.com"

  # Convert and return the input string to uppercase 
  return inputString.toUpperAscii() & "=="
