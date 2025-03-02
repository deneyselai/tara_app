# tara_app
Alsat Islemler Icin Giris Cikis Hedef Belirleme

# ÖNEMLI NOT : ANALITIK ILK DENEMEMDIR. CIHAT CICEK VE BORA ÖZKENTI DINLEYIN. YATIRIM TAVSIYESI DEGILDIR; VERI ANALIZ YÖNTEMIDIR

# TO DO : Hisse isimlerini for loop'a alip RSI hesaplanabilir


## Create a Virtual Environment Called Test Environment
python -m venv test_env

## If you receive following error

\test_env\Scripts\Activate.ps1 cannot be 
loaded because running scripts is disabled on this system. For more information, see 
about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ test_env\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

Open  PowerShell and use :
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

## Install Following Packages 
pandas yfinance plotly matplotlib
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pandas
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org yfinance
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org plotly
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org matplotlib