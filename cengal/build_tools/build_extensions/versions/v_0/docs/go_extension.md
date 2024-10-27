## Prepare

* Install Golang. You may use this instruction as an example: https://www.digitalocean.com/community/tutorials/how-to-install-go-on-ubuntu-20-04
* Install Gopy. Use an official instruction: https://github.com/go-python/gopy. Also you do not need to adjust `LD_LIBRARY_PATH` manually: we are adjusting `LD_LIBRARY_PATH` exclusively for the running session of gopy process automatically.
* Windows:
    * Create 'GO_BIN_DIR_PATH' env var with a path to Go bin dir (for example 'C:/Program Files/go/bin'). Build system will try to use 'GOPATH' if 'GO_BIN_DIR_PATH' is absent.
    * MSVC toolchain is not supported by Go at all
    * You need to use Mingw instead:
        * Suggested solution for UWP apps for Microsoft Store (from the https://github.com/golang/go/issues/20982 discussion by this comment: https://github.com/golang/go/issues/20982#issuecomment-729541323): https://github.com/status-im/mingw-windows10-uwp/blob/master/README.md
        * Prepare MinGW:
            * Create 'MINGW_BIN_DIR_PATH' env var with a path to mingw bin dir (for example 'C:/Program Files/LLVM/mingw-w64/bin'). It will be used by a build system. 
            * Alternatively add it to the path manually, but permanent PATH env var change will add bunch of unneeded unitilities to your path and even might break some of your apps.
