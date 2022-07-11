<p align="center">
  <img width="300" height="300" src="https://raw.githubusercontent.com/WAFERed/BlueEngine/main/.resources/BLUEENGINE.png">
</p>

# BlueEngine
BlueEngine is the Python CLI package for the WAFER Project. The project serves as the brains of the project. All of the research, implementation, development, packaging and distribuution is done through this project's releases. The package itself is a python virual environment that can be installed or run locally as a command line interface utility

## Getting Started
To get this package, download it through releases or to get souruce code,
```console
git clone https://github.com/WAFERed/BlueEngine.git
```
The dependencies are listed in the [requiremments.txt](https://github.com/WAFERed/BlueEngine/blob/main/requirements.txt) package and can be automatically installed by following the below setup instructions.

<hr/>

## Setup
To enter venv (virtual environment) on Unix-based systems,
```console
source venv/bin/activate
```

To pull package dependencies,
```console
pip install -r requirements.txt
```

To install package,
```console
pip install --editable .
```

To use package,
```console
blue [--OPTIONS] [COMMAND] [ARGUMENTS]
```

To get list of available commands and help,
```console
blue --help
```

## Generating A Release
To generate a .whl release package yourself, run the shell script in the root directory,
```console
sh buildwhl.sh
```

## Contributing
To contribute, fork the project or create a pull request. Alternatively, contact us using any of the below methods,
- Email Address: : <a href = "mailto: email.wafer@gmail.com">email.wafer@gmail.com</a>
- Website: [projectwafer.com](https://www.projectwafer.com) 
