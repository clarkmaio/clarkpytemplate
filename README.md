# Cookiecutter template

Clone this templates without git cloning it.



Create first an environment with cookicutter installed (this env is just to copy the template, `cookiecutter` package is not needed for the package it self)
```
conda create --name cookicutter 
pip install cookiecutter
```

Clone template with the terminal command:
```
# Example clone template "application"
cookiecutter http://gitrepo:7990/scm/uq/fp_cookiecutter.git --directory=application
```
