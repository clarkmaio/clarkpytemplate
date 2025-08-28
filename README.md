
# Cookiecutter templates
Here you will find some cookie cutter templates I've created for python programs.



## Description
* `application`: program that is supposed to be a "final" product. A program that deliver an output (a.e. a program that produce forecast or train models)
* `package`: python aux package that are supposed to be dependencies of bigger programs or `application`. The template is structured to be a `pip` installable package.


## How to

**There is no need to clone this repository!**
Just find the template you are interested in and use the following command from your terminal:

Example with template `application`
```
pip install cookiecutter
cookiecutter https://github.com/clarkmaio/clarkpytemplate.git --directory=application
```


