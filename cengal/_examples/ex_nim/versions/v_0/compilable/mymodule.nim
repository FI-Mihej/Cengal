# mymodule.nim - file name should match the module name you're going to import from python
import nimpy
import compile_time_py_definitions
import mystrutils

# Use the exported `toUpper` function
let myString = "Hello, Worldd!"
let upperString = mystrutils.toUpper(myString)

proc greet(name: string): string {.exportpy.} =
  echo upperString  # This will print: "HELLO, WORLDd!"

  when defined(CF_Linux):
    echo "mymodule: CF_Linux"
  else:
    echo "mymodule: not CF_Linux"

  when defined(CF_IS_ARM):
    echo "mymodule: CF_IS_ARM"
  else:
    echo "mymodule: not CF_IS_ARM"

  return "Hello, " & name & "!" & toUpper("me") & CD_OS_TYPE
