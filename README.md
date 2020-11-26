# Car-Parking System
  It is a python script that will serve all the desired purposes.
  
## Setup:
  1) No external libraries used in the script. So only Python 3.6+ Needed.
      1.1) If not availabe, use virtualenv.
      Commands for a virtualenv

      Linux:
      ```
      sudo apt-get install python3-pip
      sudo pip3 install virtualenv
      virtualenv -p python3.6 <venv_name>
      ```

      For other machines,
      refer: ```https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/```

  2) Clone the repository, activate the virtualenv by:  ```source <venv_name>/bin/activate```
  3) Go inside the repository and run the script by:
     python parking.py
     
## Assumptions used:

1) Driver's Age Must be > 18.
2) Creation of Car Park must be at the beginning and only once for any particular input file.
3) Duplicate Vehicle Registration numbers cases handled.
4) Input files are processed one by one (1 in each run).
5) All input files must stored in the "Input Files" folder.
6) All input files must be .txt files.
7) To change the input file, put the name of the desired file on line 128 of parking.py file in place of : ```input.txt```.
8) Could have used Classes (OOP Paradigms) to improve the readability and use of variables.
