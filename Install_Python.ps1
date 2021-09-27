### Create Variables
### wmic os get caption ; get-host
Set-StrictMode -Version 2.0
$SubscriptionName = "Azure Subscription"                                                         # Replace with the name of your Azure Subscription
$WorkFolder="C:\Labfiles\"
$NamePrefix = "in" + (Get-Date -Format “HHmmss")                                                 # Replace “in” with your initials
$ResourceGroupName = $NamePrefix + "rg"
$Location = "EASTUS"
$StorageAccountName = $NamePrefix + "sa"
$BlobContainerName = "55247a"

### Install Python 3.6.4
$PythonDownloadFile = $WorkFolder + "python-3.6.4-amd64.exe"
$PythonInstallFolder = "C:\Program Files\Python364"
$PythonURL = "https://www.python.org/ftp/python/3.6.4/python-3.6.4-amd64.exe"
(New-Object System.Net.WebClient).DownloadFile($PythonURL, $PythonDownloadFile) 
&$PythonDownloadFile /Passive InstallAllUsers=1 PrependPath=1 Include_Test=0 TargetDir=$PythonInstallFolder
$env:Path += "; " + $PythonInstallFolder + "\;"

### Install Python modules using pip.  A new console should be opened before running this and the following pip commands.
pip install --upgrade pandas, pandas_datareader, scipy, matplotlib, pyodbc, pycountry, azure

### Install Azure CLI.  Pip may need to be run from a new PowerShell console.
pip install azure-cli

### Login to Azure                          (Not Required for Azure Cloud Shell)
# $AzureUser = 'johnsingleton2@singleton.onmicrosoft.com' ; $AzurePassword = 'Pa$$w0rdPa$$w0rd' | ConvertTo-SecureString -AsPlainText -Force        
# $Credentials = New-Object –TypeName System.Management.Automation.PSCredential –ArgumentList $AzureUser, $AzurePassword
# $Subscription = Add-AzureRMAccount -Credential $Credentials
az login 		                  

### Create a new Resource Group
$RG = az group create -n $ResourceGroupName -l $Location

### Create a Storage Account       (Note:  The "az storage account check-name" command can be used to verify that no one else is using a storage account name.)
$SA = az storage account create -n $StorageAccountName -l $Location -g $ResourceGroupName --sku standard_lrs          

### Get the connection string, Storage Account Key and SAS Token for the new Storage Account:  
$ExpireDate = ((get-date).adddays(60)).ToString("yyyy-MM-dd'T'HH:mm'Z'")
$StorageAccountCS = (az storage account show-connection-string -n $StorageAccountName -g $ResourceGroupName | ConvertFrom-Json).ConnectionString
$StorageAccountKey = (az storage account keys list -n $StorageAccountName -g $ResourceGroupName | ConvertFrom-Json)[0].Value
$StorageAccountToken = az storage account generate-sas --expiry $ExpireDate --services bf --resource-types sco --permissions cdluw --account-name $StorageAccountName
# az storage blob url --container-name $BlobContainerName --name $BlobContainerName --connection-string $StorageAccountCS

### Create a Blob and File Share  
az storage container create -n $BlobContainerName --connection-string $StorageAccountCS
az storage share create --name $BlobContainerName --connection-string $StorageAccountCS

### Upload data to the Blob and File Share
az storage blob upload-batch --source $WorkFolder --pattern "*.zip" --destination $BlobContainerName --connection-string $StorageAccountCS
az storage file upload-batch --source $WorkFolder --pattern "*.ps1" --destination $BlobContainerName --connection-string $StorageAccountCS

# Connect to File Share
$FileShare = "\\" + $StorageAccountName + ".file.core.windows.net\" + $BlobContainerName
Net Use Z: $FileShare /u:AZURE\$StorageAccountName $StorageAccountKey

### Use the Azure Portal to verify the create of the new resource group, storage account, and container.
### Delete the resource group and verify that the storage account and container were also removed:  
# az group delete -n $ResourceGroupName
# pip install --upgrade numpy, pandas, pandas_datareader, scipy, matplotlib, pyodbc, pycountry, azure
