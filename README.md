***********************HOW TO RUN THE DJngo BLOG APP**************************

PART (A)

a) Assuming you have read the entire Licence governing this source code.
   You can procede with instructions below:

                      <!>CAUTION/IMPORTANT!!!
b) These Instructions are strictly for software developers using linux OS. 
   This system was developed from Linux OS Ubuntu 18.04 

c) Clone or Download This Project Zip Folder and Extract it.

e) Right click on the extracted folder and open it with Visual Studio Text Editor

If you don't have Visual studio Text Editor
in your linux OS based machine, follow Instructions
from this link: https://www.tecmint.com/install-visual-studio-code-on-linux/

d) Open Terminal in Visual Studio Text Editor and Execute Following Commands:

*******************************************************************************

PART (B)

<!> CAUTION | IMPORTANT |

==> Before proceding to any of steps provided below IN PART (C), 
please setup the postgres database  using the postgre.txt file provided 
in the project folder. If you skip this step, the project will not execute.

*********************************************************************************

PART (C)

<!> START 
** Assuming you have read all the instructions in PART (B)
** Assuming you already have pip or pipenv Installed on your Machine.
** Assuming you are familiar with migration(s) procedures in Django Frame Work.

1. Setup the virtual Environment via terminal.
   $  pipenv --python <version>

2. Activate the Environment
   $  pipenv shell

3. In the activated environment, install the requirements for the project
   $  pip install -r requirements.txt

4. Apply all the migrations
   $  python manage.py migrate

6. Create a superuser
   $  python manage.py createsuperuser

7. In your terminal 1, run your project
   $  python manage.py runserver
   Now enter following URL in Your Browser Installed On Your Pc
   http://127.0.0.1:8000/

<!> STOP

-----------------------------------------------------------------------------

DEVELOPER ONLINE PORTFOLIOS



1. SEAN KAMUGASA   : https://seankamugasa.github.io/
2. WASSWA HERBERT  : https://wasswaherbert.github.io/

------------------------------------------------------------------------------
