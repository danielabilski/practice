# challenge


Solution:

The idea is to get the fire incident from the source directly via a python script and upload it into a database. 

We will replace the data everytime the script runs just to have the latest data updated in the Socrata webpage (assuming that is updated daily).

I imagine this process being automated in a Jenkins job. 

On the other hand, build a stored procedure with variables to run specific queries by passing the values they need to analyze the data.


Questions:

BI team mentioned is from the customer side?

If so, I need to understand how they are expecting to use the solution: 

Do they need a report with the data filtered? or Do they need to run queries exceuting a stored procedure in their own db by passing custom values? 
What type of queries do they need? How is the logic?

about the three dimensiones mentioned: they would analyze them separately?


