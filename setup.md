# Instructions for how to set up a conda environment to run the lecture notes locally

1. Go to the link below and download the `enviroment.yml` file to your machine.

https://github.com/biavillasboas/SIO221A/edit/master/environment.yml

## How to set-up

### Linux and Mac

Open a terminal and navigate to the directory that you saved the environment.ym file. Then run:

`conda env create -f environment.ym`

Wait until the packages are intalled. 

To use the enviroment, open the terminal and run:

`conda activate SIO221A`

after you activate the environment, you can launch jupyter lab or jupyter notebook from your terminal

`jupter lab`

You can see more about environments [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Windows 

The instructions below should be followed after openning the Anaconda navigator. You can find more detailed instruction [here](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/).


- Importing an environment

Each environment has a YAML-formatted configuration file. If someone has given you an environment file that you want to use, for example my-environment-file.yml, and you have saved it to your computer, you can import it into Navigator.

1. At the bottom of the environments list, click the Import button.

2. In the Import dialog box, type a descriptive name for the new environment (SIO221A in our case).

3. Click the file folder icon to browse to the YAML file, or type the file name, including its path.

4. Click the Import button


- Using an environment

In the environments list, click the environment name (SIO221A). Click the arrow (play) button next to the name. Select the option "Open Terminal". 
In the terminal, run

`jupyter lab`

This will open a Jupyter Lab using the SIO221A environment.
