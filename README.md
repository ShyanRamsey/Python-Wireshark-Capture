This is a Netmiko script that will gather network device configuration.
=========================================================================

_Install requirements.txt_
Windows/Linux: pip install -r requirements.txt
Sometimes pip install gives a error: externally-managed-environment error. Try:
   1. Creating a venv and activating it
   2. pip install -r requirements.txt
   3. python3 -c "import netmiko; print(netmiko.__version__)" to verify

_For secure credentials_
Create a .env file. This loads your credentals as environment variables.
A .env file also helps keep your code reusable.

I will finish this at a later date with more info :)

