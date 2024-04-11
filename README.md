### dbt Cloud
**!This is not a dbt cloud example.** If you are looking for dbt Cloud connector then check the dbt Cloud from Community Connector https://app.workato.com/browse/connectors?q=dbt

### dbt Core how to
Dbt core is the free and open source version of dbt by Dbt Labs https://github.com/dbt-labs/dbt-core

**Instructions**
To run this you will need to:
1. Setup [OnPremise Agent](https://docs.workato.com/on-prem.html) from Workato 
2. Setup Python in global folder and not your local AppData user folder, it should be under:
`C:\Program Files\Python312`
You can do this by picking install for all users on Windows setup screen
3. Make sure Agent can run Python from action block in Workato [execute script action](https://docs.workato.com/connectors/on-prem-command-line-scripts.html#execute-command-line-script-action). You can test a simple command
`Python --version`
3. Install dbt using `pip `and make sure it is installed under global folder `C:\Program Files\Python312\Lib\site-packages` and NOT c:\users\myuser\AppData\Local\Programs\Python. On Windows can do this by opening cmd using right click &gt; Administrator and running 
`pip install dbt-postgres --force-reinstall` to force it install inside the global folder for all  users
4. Copy your dbt project (or do git checkout) on the machine running the OPA for example on 
`C:/Workato/dbt-project`
5. Download the [dbt-runner.py](https://github.com/maxknu/dbt-core-workato) script which helps to run the commands from Workato script action
6. Place the script on your virtual machine with OPA for example in
`C:/Workato/Scripts`
7. Test your dbt project on the OPA machine, make sure the database connections are properly configured and dbt run / build commands are working. 
8. Find the .dbt configuration folder with the yaml files 
`C:\Users\youruser\.dbt`
9. Copy the .dbt folder to 
`C:/Workato/.dbt. `
10. Make sure the OPA service user (default user on windows is 'Local Service') can read / write / execute on the  C:/Workato folder. Right click on folder  &gt; Properties &gt; Security and add Local Service or another user which is running your Workato OnPremise Agent 
11. Add and Execute script command to your recipe and connect, provide the script details. Check screenshot on [github to get some configuration](https://github.com/maxknu/dbt-core-workato/blob/main/workato-recipe-connector_config.png) examples 
12. input 3 parameters, your dbt project, dbt command line "dbt run" and dbt profile directory. [Screenshot example here](https://github.com/maxknu/dbt-core-workato/blob/main/workato-recipe-example_action_config.png) 
