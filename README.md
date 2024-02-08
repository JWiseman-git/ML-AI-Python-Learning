**Overview**

Trying different projects out to learn AI / ML learning principles 

**Venv**
The variety of projects requires diverse and rare package usages - an virtual environment is therefore used to keep distinct package types contained. 

#### Using the custom environment when running in PyCharm 

Instructions on how to force PyCharm to work in the virtual environment: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html

#### Running a project script in CMD line
Best performed the first time - as alongside this any requirements can be downloaded easily.

```console
rem First cd to project file
rem C:\Users\jorda\Documents\GitHub> cd project_folder_name
rem Activate virtual environment
rem C:\Users\jorda\Documents\GitHub\ML-AI-Python-Learning> myenv\Scripts\activate
rem Inspect requirements package
rem (myenv) C:\Users\jorda\Documents\GitHub\ML-AI-Python-Learning>pip freeze requirements.txt
rem Install all requirements
rem (myenv) C:\Users\jorda\Documents\GitHub\ML-AI-Python-Learning> pip install -r requirements.txt
rem Run any scripts
rem (myenv) C:\Users\jorda\Documents\GitHub\ML-AI-Python-Learning> python HelloGen.py
```
#### Activate from Python 
Should be included at the top of any main scripts used for each project included - easiest way if requirements already downloaded. 
```python
source venv/bin/activate
```
