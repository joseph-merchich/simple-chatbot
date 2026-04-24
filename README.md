How to install the Ollamma model:

Navigate to your system's terminal.

Command: `ollama pull lamma2`.



Code line-by-line:

LINE 1: Imports requests for URL.

LINE 2: Imports `json` for conversation file.

LINE 3: Imports `system` for interaction with PC.

LINE 4: Imports time for `slowSpacePrint()`.

LINE 5: Defines the `Ollama` model.

LINE 6: Defines the outfile.

LINE 7: Defines the URL.

LINE 8: Ask the user if they want responses read to them.

LINE 9: If the user input equals "y":

LINE 10: Left blank for readability.

LINE 11: Starts a `try` command.

LINE 12: Attempts to import `pyttsx3`.

LINE 13-15: Excepts `importError` if importation fails, prints that the `pyttsx3` module needs to be installed, and exits the program.

LINE 16: Left blank for readability.

LINE 17-18: Still within the `try` statement, attempts to intialize the `pyttsx3` module under the name `tts`. Declares `voice_on = True`.

LINE 19: Left blank for readability.

LINE 20-25: Defines the `slowSpacePrint` function, which makes the output print out in a more stylized manner.

LINE 26: Left blank for readability.

LINE 27-29: Defines the `speak` function with the parameter `text`. The function uses `pyttsx3` to say the text.


LINE 30: Left blank for readability.

LINE 30-33: Starts the input sequence.

LINE 34-37: Specifies the `Ollama` models' role.

LINE 38: Left blank for readability.

LINE 39: Starts the `while` loop. 

LINE 40-41: While prompt is not empty, print 'Thinking...'. Print a new line.

LINE 42-46: Creates the `msg` dictionary.

LINE 47: Declares `resp`. `resp` posts the `msg` dict to the `Ollama` model.

LINE 48-49: If the`Ollama` servers' satus is unsatisfactory, raise an error.

LINE 51-57: Loads the response from the `Ollama` model, `slowSpacePrint` the answer, and, `if voice_on == True`, speaks the answer as well.

LINE 58-61: Appends and updates messages.

LINE 62: Left blank for readability.

LINE 63-69: Asks for input again.

LINE 70: Left blank for readability.

LINE 71-74: Writes and saves interaction to file. The program can reference this in future conversations.

I hope this explained my code! 
