import win32api
import win32print

win32api.ShellExecute(0, "print", "test.txt", f'/d:"{win32print.GetDefaultPrinter()}"', ".", 0)