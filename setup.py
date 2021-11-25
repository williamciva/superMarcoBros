import cx_Freeze
executables = [cx_Freeze.Executable(
    script="startGame.py", icon="assets/superMarcosBrosIcoPng.ico")]

cx_Freeze.setup(
    name="Super Marcos Bros",
    options={"build_exe": {"packages": ["pygame", "art", "os", "pyautogui"],
                           "include_files": ["assets", "libsGame"]
                           }},
    executables=executables
)
