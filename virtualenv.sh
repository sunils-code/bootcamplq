# Note:  On computers running multiple versions of python, use the "python -m pip" command to ensure that modules are installed for the current default version on the system.
# E.g. "python -m pip install numpy pandas faker names"
echo "Virtual environments are often used to create specifc environment configurations for applications."
echo "They are also used to develop apps on machines where root access is not available."
echo "You may also use your personal user environment (--user) to configure resources that require elevated access."
echo "On systems that support multiple versions of python, make sure the default version is 3.X or add an alias that maps python to python3 (e.g. alias python=python3)."
# alias python=python3
pip install --user --upgrade pip
python3 -m pip install --user virtualenv
# verify the location and name of the version of python used with the -p parameter before running this command
virtualenv -p /usr/bin/python3 ~/virtualenv1
cd ~/virtualenv1
source ~/virtualenv1/bin/activate
pip install --upgrade pip
python3 -m pip install --upgrade pandas
python3 -m pip install --upgrade scipy
python3 -m pip install --upgrade matplotlib
python3 -m pip install --upgrade azure
# Examples of user environment configuration of python modules
# python3 -m pip install --user --upgrade pandas
# python3 -m pip install --user --upgrade scipy
# python3 -m pip install --user --upgrade matplotlib
# python3 -m pip install --user --upgrade azure
deactivate


