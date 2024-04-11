# dbt-core-workato
### dbt Core 
Dbt core is the free and open source version of dbt by Dbt Labs https://github.com/dbt-labs/dbt-core

### dbt Cloud
**This is not a dbt cloud example.** If you are looking for dbt Cloud connector then check the other examples and dbt Cloud from Community Connectors https://app.workato.com/browse/connectors?q=dbt

This this an example recipe which is part of the tutorial on how to setup Workato + dbt core 

**Instructions**
To run this you will need to:
1. Setup [OnPremise Agent](https://docs.workato.com/on-prem.html) from Workato 
2. Setup Python on your OnPremise Agent virtual machine and make sure it can be executed from [execute script action](https://docs.workato.com/connectors/on-prem-command-line-scripts.html#execute-command-line-script-action) from Workato 
3. Copy your dbt project your want to run "dbt build" or "dbt start" on to a network shared folder or directly to the Virtual machine running OnPremise Agent
4. 

