# Frequently Asked Questions

**1. I have already created the SIO221A environment. How do I add the environment to the list of available kernels?**

- Linux/Mac 
Open the terminal and run 

`conda activate SIO221A`

then run:

`ipython kernel install --user --name=SIO221A`

That is it. Now, when you launch JupyterLab or Jupyter Notebook, the SIO221A kernel will be available. 

- Windows

Open the Anaconda navigator. On the left menu, go to the Environments tab. CLick on the play button on the SIO221A environment tab and click "Open Terminal".

In the terminal, run:

`ipython kernel install --user --name=SIO221A`

Close the terminal and that is it. You can now launch JupyterLab or Jupyter Notebook and the SIO221A kernel will be available
