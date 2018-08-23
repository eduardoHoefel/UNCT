# UnFT - Universal Form Tool

UnFT is a generic form tool, with ease setup, capable of creating forms to do anything. From Software configuration to Network testing, your imagination is the limit.
At least that's the objective. This project is still under development.
The major ideia is already working, but only in a linux-terminal environment.

My dream is to create a generic tool, able to run as a Windows app, Linux shell, web app, and so on.

Over the next days, I'll try to refactor the code to a MVC model, create interfaces and abstract classes to simplify the task of extending this project.
Also, it'll ease the involvement of new developers who wish to contribute.

## How it works

Menus and forms are described in JSON files, and the form submission executes a script passing the submitted values as parameters.

## System Requirements

 - Terminal emulator
 - Python 3.4
 - Ncurses

## TODO

### Version 1.1:

 - Refactor code
 - Provide documentation
 - Specify json patterns

### Version 1.2:

 - Remove recursion from menu files and let it load inside menus from other files
 - Do the same with form files

### Version 1.3:

 - Extend window funcionalities in terminal
 - More input types

### Version 1.4:

 - Create a default form save file
 - Ease the translation from that file to other formats

### Version 2.0:
 - Provide a Form editor
 - Provide a UnFT config tool
 - Port the project to other front-ends

## License

See the [LICENSE](LICENSE) file for license rights and limitations (GPLv3).
