# WooWoo

This extension brings the WooWoo Language Server to VSCode. In addition to that it provides basic client-side syntax highlighting.

## Installation guide

Please follow these steps to setup the extension:

1. Ensure that you have C compiler installed on your system.
    - The extension uses [tree-sitter](https://github.com/tree-sitter/tree-sitter) for parsing, which requires the compiler. It will try to look for the compiler in the standard places for each platform.
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

To get the best highlighting experience, we recommend experimenting with different themes. 
You can change your theme by selecting the `Preferences: Color theme` command from the **command menu**. 
Here are a few that we've found to work particularly well with WooWoo LS:
- Monokai Dimmed
- [More recommendations coming soon]
