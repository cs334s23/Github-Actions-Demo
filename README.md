# Github-Actions-Demo

*Repository represents an example of what needs to be done to run a Github-Actions workflow using a Makefile*

This repo should be similiar to the process we use in shifting from our old Jenkins CI to a Github-Actions based CI

---
Steps: 

1.  From root of project type 
    
    ```mkdir .github/workflows```
2. Create a file in that directory which represents the yaml file that will be run on a certain trigger in the repo
    
    ```touch <workflow-file-name>.yml```

    * Here is an example of what a workflow.yml file could look like 

        ![Screenshot](example_yaml.png)

3. `make` command along with a corresponding `makefile` can be used to automate complicated testing steps from the command line.
    * Calling `make` from from the yaml file is a good practice because changes would only have to be made in the `makefile` and can be used from GitHub Actions or command line.


