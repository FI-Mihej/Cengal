// Package greeter provides a simple greeting function
package greeter

import (
	"cengal/_examples/ex_golang/versions/v_0/compilable/compile_time_py_definitions"
	"fmt"
)

var index = 0

// Greet takes a name and prints a greeting message
func Greet(name string) {
	fmt.Printf("%d> Hello, %s! Welcome to our module.\n", index, name)
	index++
}

// Greet takes a name and prints a greeting message
func Greet2(name string) {
	fmt.Printf("%d> Hello, %s! Welcome to our module.\n%s\n%s\n", index, name, compile_time_py_definitions.ApiEndpointDoc, compile_time_py_definitions.GOD_OS_TYPE)
	index++
}
