from cengal.system import OS_TYPE

from typing import List, Tuple, Dict, Sequence


def ncursorBackward(count: int = 1):
    ...

def ncursorDown(count: int = 1):
    ...


def ncursorForward(count: int = 1):
    ...


def ncursorUp(count: int = 1):
    ...


def neraseLine():
    ...


def neraseScreen():
    ...


def ngetch() -> str:
    ...


def nhideCursor():
    ...


def nisatty() -> bool:
    ...


def nreadPasswordFromStdin(prompt: str = "password: ") -> str:
    ...


def nsetCursorPos(x: int, y: int):
    ...


def nsetCursorXPos(x: int):
    ...


if 'Windows' == OS_TYPE:
  def nsetCursorYPos(y: int):
        ...


def nshowCursor():
    ...


def nterminalHeight() -> int:
    ...


def nterminalHeightIoctl(handles: List[int]) -> int:
    ...


def nterminalSize() -> Tuple[int, int]:
    ...


def nterminalWidth() -> int:
    ...


def nterminalWidthIoctl(handles: List[int]) -> int:
    ...


def nresetAttributes():
    ...


def nstyledWriteOld(args: List[Dict]):
    ...


def nstyledWrite(args: List[Dict]):
    ...


def nstyledWriteFast(args: List[Dict]):
    ...


def nstyledWriteLine(args: List[Dict]):
    ...


def nstyledEcho(args: List[Dict]):
    ...


def nansiStyleCode(style: int) -> str:
    ...


def nwriteStyled(txt: str, style: Sequence[int] = (1,)):
    ...


def nsetForegroundColor(fg: int, bright: bool = False):
  ...


def nsetBackgroundColor(bg: int, bright: bool = False):
  ...


def nansiForegroundColorCode(fg: int, bright: bool = False) -> str:
  ...


def nansiForegroundTrueColorCode(color: int) -> str:
  ...


def nansiBackgroundColorCode(color: int) -> str:
  ...


def nsetForegroundTrueColor(color: int):
  ...


def nsetBackgroundTrueColor(color: int):
  ...


def nisTrueColorSupported() -> bool:
  ...


def nenableTrueColors():
  ...


def ndisableTrueColors():
  ...


def nenterTerm(full_screen: bool = True, mouse: bool = False):
    ...


def nexitTerm():
    ...


def nsaveStdoutState():
    ...


def nrestoreStdoutState():
    ...


def nprepareTryGetch(ms: int = 1000) -> bool:
    ...


def ntryGetch() -> Tuple[int, int]:
    ...


def nwinTryGetch(ms: int = 1000) -> Tuple[bool, int, bool, int]:
    ...
