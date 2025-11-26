# Localrag v. 0

*Tuesday, Novemebr 25, 2025*

Localrag is a command line tool that allows you to use an LLM to ask questions about the codebase in which you have initialized the localrag project. 

## Commands

Commands for this CLI have been copied from git, so they should be fairly intuitive for anyone who has operated with git.

### Initializing the project
```bash
localrag init
```

This initializes the `.rag` directory. This directory is curcial for naking localrag work as all of the files are kept here. Please do not modify the `.rag` directory unless you know what you are doing.

### Adding files to the staging area

```bash
localrag add path\to\file
```

Adds a file to the staging area. For now, this can only happen with one file at a time. In future versions, batch adding will be supported. This copies the file to the staging directory in the `.rag` directory. It will take a little time.

### Committing

```bash
localrag commit
```

This will vectorize each file you added to the staging area. It will then add the vectorized file to a milvus database in the `.rag` directory. You must execute this command before being able to interact with the LLM.

### Status

```bash
localrag status
```

This will give you a status of what files are currently staged. 

### Removing file from staging area

```bash
localrag rm path\to\file
```

This will remove the file from the staging area.

### Prompting the LLM

```bash
localrag ask
```

This will open up chatting service that will allow you to query the LLM about your project. The LLM does not stream its response back so it will take some time before you see a response.

Currently, only Gemini is supported as the LLM. You will need to create a `.env` file with your Gemini API key in the folder for this package. Future versions will try to support more enterprise models as well as locally run models. 


## Notes about the package


