# WooWoo

This extension brings the WooWoo Language Server to VSCode. In addition to that it provides basic client-side syntax highlighting.

## Installation guide

Please follow these steps to setup the extension:

1. **System compatibility**
    - Unless you are running the extension on one of the following systems, you need to have a C++ compiler installed.
    - Supported systems (no need for compiler):
        - Windows x64
        - Linux x64
        - *more coming soon*
        
2. Install the `tree-sitter` Python package. You can install it into Python virtual environment, system Python or any other Python interpreter you have.
3. Install the extension from the marketplace 
4. Open the **command menu** and search for `Python: Select interpreter` command
    - To open the menu, press `Ctrl + Shift + P` or `Cmd + Shift + P` on Mac
5. Select the Python interpreter you used in Step 2.
6. You are all set up!
    - If the language server isn't working, open the command menu and run the `WooWoo VSCode: Restart Server` command.

## Language Server Features

Please visit [the official WooWoo Language Server repository](https://gitlab.fit.cvut.cz/woowoo/lsp/woowoo-language-server) to see the full list of features.


## Theme Choice and Semantic Highlighting

The choice of theme in VSCode plays a pivotal role in the semantic highlighting experience provided by the WooWoo LS. Some themes might use the same color for various token types, which could lead to suboptimal highlighting when working with WooWoo documents.

