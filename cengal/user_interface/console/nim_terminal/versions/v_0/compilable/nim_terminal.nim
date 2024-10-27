# mymodule.nim - file name should match the module name you're going to import from python
import nimpy
import compile_time_py_definitions
import std/terminal
import std/winlean
import std/colors
from async_getch import prepareTryGetch, tryGetch, illwillInit, illwillDeinit, winTryGetch
# import illwill


proc ncursorBackward(count: int = 1){.exportpy.} =
  cursorBackward(stdout, count)

proc ncursorDown(count: int = 1){.exportpy.} =
  cursorDown(stdout, count)

proc ncursorForward(count: int = 1){.exportpy.} =
  cursorForward(stdout, count)

proc ncursorUp(count: int = 1){.exportpy.} =
  cursorUp(stdout, count)

proc neraseLine() {.exportpy.} =
  eraseLine(stdout)

proc neraseScreen() {.exportpy.} =
  eraseScreen(stdout)

proc ngetch(): char {.exportpy.} =
  return getch()

proc nhideCursor() {.exportpy.} =
  hideCursor(stdout)

proc nisatty(): bool {.exportpy.} =
  return isatty(stdout)

proc nreadPasswordFromStdin(prompt: string = "password: "): string {.exportpy.} =
  return readPasswordFromStdin(prompt)

proc nsetCursorPos(x, y: int) {.exportpy.} =
  setCursorPos(stdout, x, y)

proc nsetCursorXPos(x: int) {.exportpy.} =
  setCursorXPos(stdout, x)

when defined(windows):
  proc nsetCursorYPos(y: int) {.exportpy.} =
    setCursorYPos(stdout, y)

proc nshowCursor() {.exportpy.} =
  showCursor(stdout)

proc nterminalHeight(): int {.exportpy.} =
  return terminalHeight()

proc nterminalHeightIoctl(handles: openArray[Handle]): int {.exportpy.} =
  return terminalHeightIoctl(handles)

proc nterminalSize(): tuple[w, h: int] {.exportpy.} =
  return terminalSize()

proc nterminalWidth(): int {.exportpy.} =
  return terminalWidth()

proc nterminalWidthIoctl(handles: openArray[Handle]): int {.exportpy.} =
  return terminalWidthIoctl(handles)

proc nresetAttributes() {.exportpy.} =
  resetAttributes()

# Define the types for the arguments
type
  Arg* = object
    bg_style_type*: uint8
    bg_color_type*: uint8
    fg_color_type*: uint8
    style_type*: seq[uint8]
    str_type*: string
    has_reset_style*: bool
    has_foreground_true_color*: bool
    foreground_true_color*: int
    has_background_true_color*: bool
    background_true_color*: int

type
  BackgroundStyle* = enum ## Background style.
    bgStyleDefault = 0,      ## default
    bgStyleBright,           ## bright
    bgStyleDim,              ## dim

proc nstyledWriteOld(args: seq[Arg]) {.exportpy.} =
  for i in countup(0, args.len - 1):
    let arg = args[i]
    var default_bg_style: bool = bgStyleDefault == BackgroundStyle(arg.bg_style_type)
    var bg_style_bright: bool = bgStyleBright == BackgroundStyle(arg.bg_style_type)
    var style_type: set[Style] = {}
    for style_int in arg.style_type:
      style_type.incl(Style(style_int))
    
    if default_bg_style and (not arg.has_foreground_true_color) and (not arg.has_background_true_color):
      stdout.styledWrite(BackgroundColor(arg.bg_color_type), ForegroundColor(arg.fg_color_type), style_type, arg.str_type)
    elif default_bg_style and (not arg.has_foreground_true_color) and arg.has_background_true_color:
      stdout.styledWrite(BackgroundColor(arg.bg_color_type), ForegroundColor(arg.fg_color_type), bgColor, Color(arg.background_true_color), style_type, arg.str_type)
    elif default_bg_style and arg.has_foreground_true_color and (not arg.has_background_true_color):
      stdout.styledWrite(BackgroundColor(arg.bg_color_type), ForegroundColor(arg.fg_color_type), fgColor, Color(arg.foreground_true_color), style_type, arg.str_type)
    elif default_bg_style and arg.has_foreground_true_color and arg.has_background_true_color:
      stdout.styledWrite(BackgroundColor(arg.bg_color_type), ForegroundColor(arg.fg_color_type), fgColor, Color(arg.foreground_true_color), bgColor, Color(arg.background_true_color), style_type, arg.str_type)
    elif (not default_bg_style) and (not arg.has_foreground_true_color) and (not arg.has_background_true_color):
      stdout.setBackgroundColor(BackgroundColor(arg.bg_color_type), bg_style_bright)
      stdout.styledWrite(ForegroundColor(arg.fg_color_type), style_type, arg.str_type)
    elif (not default_bg_style) and (not arg.has_foreground_true_color) and arg.has_background_true_color:
      stdout.setBackgroundColor(BackgroundColor(arg.bg_color_type), bg_style_bright)
      stdout.styledWrite(ForegroundColor(arg.fg_color_type), bgColor, Color(arg.background_true_color), style_type, arg.str_type)
    elif (not default_bg_style) and arg.has_foreground_true_color and (not arg.has_background_true_color):
      stdout.setBackgroundColor(BackgroundColor(arg.bg_color_type), bg_style_bright)
      stdout.styledWrite(ForegroundColor(arg.fg_color_type), fgColor, Color(arg.foreground_true_color), style_type, arg.str_type)
    elif (not default_bg_style) and arg.has_foreground_true_color and arg.has_background_true_color:
      stdout.setBackgroundColor(BackgroundColor(arg.bg_color_type), bg_style_bright)
      stdout.styledWrite(ForegroundColor(arg.fg_color_type), fgColor, Color(arg.foreground_true_color), bgColor, Color(arg.background_true_color), style_type, arg.str_type)

proc nstyledWrite(args: seq[Arg]) {.exportpy.} =
  for i in countup(0, args.len - 1):
    let arg = args[i]
    var default_bg_style: bool = bgStyleDefault == BackgroundStyle(arg.bg_style_type)
    var bg_style_bright: bool = bgStyleBright == BackgroundStyle(arg.bg_style_type)
    var all_font_styles: set[Style] = {Style.styleItalic .. Style.styleStrikethrough}
    var style_type: set[Style] = {}
    for style_int in arg.style_type:
      style_type.incl(Style(style_int))
    
    var default_fg_style: bool = (styleBright notin style_type) and (styleDim notin style_type)
    var fg_style_bright: bool = styleBright notin style_type

    # background style
    if default_bg_style:
      stdout.setBackgroundColor(BackgroundColor(arg.bg_color_type))
    else:
      stdout.setBackgroundColor(BackgroundColor(arg.bg_color_type), bg_style_bright)

    if arg.has_background_true_color:
      stdout.setBackgroundColor(Color(arg.background_true_color))

    # foreground style
    if default_fg_style:
      stdout.setForegroundColor(ForegroundColor(arg.fg_color_type))
    else:
      stdout.setForegroundColor(ForegroundColor(arg.fg_color_type), fg_style_bright)

    if arg.has_background_true_color:
      stdout.setForegroundColor(Color(arg.foreground_true_color))
    
    # font style
    var font_styles: set[Style] = all_font_styles * style_type
    if len(font_styles) > 0:
      stdout.setStyle(style_type)
    
    # write the string
    stdout.write(arg.str_type)
  
  stdout.resetAttributes()

proc nstyledWriteFast(args: seq[Arg]) {.exportpy.} =
  var needToResetAttributes: bool = false
  for i in countup(0, args.len - 1):
    let arg = args[i]
    var default_bg_style: bool = bgStyleDefault == BackgroundStyle(arg.bg_style_type)
    var bg_style_bright: bool = bgStyleBright == BackgroundStyle(arg.bg_style_type)
    var all_font_styles: set[Style] = {Style.styleItalic .. Style.styleStrikethrough}
    var style_type: set[Style] = {}
    for style_int in arg.style_type:
      style_type.incl(Style(style_int))
    
    var default_fg_style: bool = (styleBright notin style_type) and (styleDim notin style_type)
    var fg_style_bright: bool = styleBright notin style_type

    # background style
    if bgDefault != BackgroundColor(arg.bg_color_type):
      needToResetAttributes = true
      if default_bg_style:
        stdout.setBackgroundColor(BackgroundColor(arg.bg_color_type))
      else:
        stdout.setBackgroundColor(BackgroundColor(arg.bg_color_type), bg_style_bright)

    if arg.has_background_true_color:
      needToResetAttributes = true
      stdout.setBackgroundColor(Color(arg.background_true_color))

    # foreground style
    if fgDefault != ForegroundColor(arg.fg_color_type):
      needToResetAttributes = true
      if default_fg_style:
        stdout.setForegroundColor(ForegroundColor(arg.fg_color_type))
      else:
        stdout.setForegroundColor(ForegroundColor(arg.fg_color_type), fg_style_bright)

    if arg.has_background_true_color:
      needToResetAttributes = true
      stdout.setForegroundColor(Color(arg.foreground_true_color))
    
    # font style
    var font_styles: set[Style] = all_font_styles * style_type
    if len(font_styles) > 0:
      needToResetAttributes = true
      stdout.setStyle(font_styles)
    
    # write the string
    stdout.write(arg.str_type)
  
  if needToResetAttributes:
    stdout.resetAttributes()

proc nstyledWriteLine(args: seq[Arg]) {.exportpy.} =
  # nstyledWriteOld(args)
  # nstyledWrite(args)
  nstyledWriteFast(args)
  stdout.write("\n")
  # stdout.flushFile()  # Ensure all output is flushed

proc nstyledEcho(args: seq[Arg]) {.exportpy.} =
  nstyledWriteLine(args)

proc nansiStyleCode*(style: int): string {.exportpy.} =
  return ansiStyleCode(style)

proc nwriteStyled*(txt: string, style: seq[int] = @[1]) {.exportpy.} =
  var style_type: set[Style] = {}
  for style_int in style:
    style_type.incl(Style(style_int))

  writeStyled(txt, style_type)

proc nsetForegroundColor*(fg: int, bright: bool = false) {.exportpy.} =
  stdout.setForegroundColor(ForegroundColor(fg), bright)

proc nsetBackgroundColor*(bg: int, bright: bool = false) {.exportpy.} =
  stdout.setBackgroundColor(BackgroundColor(bg), bright)

proc nansiForegroundColorCode*(fg: int, bright: bool = false): string {.exportpy.} =
  return ansiForegroundColorCode(ForegroundColor(fg), bright)

proc nansiForegroundTrueColorCode*(color: int): string {.exportpy.} =
  return ansiForegroundColorCode(Color(color))

proc nansiBackgroundColorCode*(color: int): string {.exportpy.} =
  return ansiBackgroundColorCode(Color(color))

proc nsetForegroundTrueColor*(color: int) {.exportpy.} =
  stdout.setForegroundColor(Color(color))

proc nsetBackgroundTrueColor*(color: int) {.exportpy.} =
  stdout.setBackgroundColor(Color(color))

proc nisTrueColorSupported*(): bool {.exportpy.} =
  return isTrueColorSupported()

proc nenableTrueColors*() {.exportpy.} =
  enableTrueColors()

proc ndisableTrueColors*() {.exportpy.} =
  disableTrueColors()

proc nenterTerm*(fullScreen: bool=true, mouse: bool=false) {.exportpy.} =
  illwillInit(fullScreen, mouse)

proc nexitTerm*() {.exportpy.} =
  illwillDeinit()

when defined(windows):

  proc nsaveStdoutState*() {.exportpy.} =
    discard

  proc nrestoreStdoutState*() {.exportpy.} =
    discard

else:
  import termios

  var oldStdoutMode: Termios
  var oldStdoutModeRestored: bool = true

  proc nsaveStdoutState*() {.exportpy.} =
    ## Reads a single character from the terminal, blocking until it is entered.
    ## The character is not printed to the terminal.
    when not defined(windows):
      oldStdoutModeRestored = false
      let fd = getFileHandle(stdin)
      discard fd.tcGetAttr(addr oldStdoutMode)

  proc nrestoreStdoutState*() {.exportpy.} =
    ## Reads a single character from the terminal, blocking until it is entered.
    ## The character is not printed to the terminal.
    when not defined(windows):
      if not oldStdoutModeRestored:
        let fd = getFileHandle(stdin)
        discard fd.tcSetAttr(TCSADRAIN, addr oldStdoutMode)
        oldStdoutModeRestored = true

proc nprepareTryGetch*(ms: int32 = 1000): bool {.exportpy.} =
  return prepareTryGetch(ms)

proc ntryGetch*(): tuple[num: int, ch: int] {.exportpy.} =
  return tryGetch()

proc nwinTryGetch*(ms: int32 = 1000): tuple[has_ch: bool, ch: int, has_vsc: bool, vsc: int] {.exportpy.} =
  return winTryGetch(ms)
