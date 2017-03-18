from cx_Freeze import setup, Executable

setup(
    name = "Alien Invasion",
    version = "0.1",
    description = "Alien Invasion",
    executables = [Executable("alien_invasion.py")]
)