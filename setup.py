from cx_Freeze import setup, Executable

setup(
    name = "Slover",
    version = "0.1",
    description = "Slover",
    executables = [Executable("main.py")]
)