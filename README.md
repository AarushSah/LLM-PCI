# LLM-PCI: Project Context Injector for LLMs

LLM-PCI is a Python script that allows you to inject the context of an entire project folder into long-context language models (LLMs) for use as a coding assistant. The script processes a specified folder and its contents, including subfolders and files, and generates a structured text file that preserves the folder hierarchy and file contents.

## Features

- Recursively processes folders and their contents
- Automatically distinguishes between text files and other file types
- Includes the contents of text files in the generated context file
- Represents non-text files with their name, file type, and size
- Prompts the user to include or skip each folder encountered
- Generates a comprehensive text file with folder structure and file contents
- Provides descriptive comments and output for better readability

## Usage

1. Clone this repository to your local machine.

2. Make sure you have Python installed (version 3.6 or above).

3. Open the `llm_pci.py` script in a text editor.

4. Modify the `folder_path` variable to specify the path to the project folder you want to inject.

5. Optionally, you can change the `output_file_name` variable to specify a different name for the generated context file.

6. Run the script using the following command:

   ```
   python llm_pci.py
   ```

7. The script will prompt you for each folder encountered, asking whether to include it or not. Enter 'y' (case-insensitive) to include the folder or any other value to skip it.

8. Once the script finishes executing, it will generate a text file with the specified name (default: `project_context.txt`) in the same directory as the script.

9. The generated context file will contain the folder structure and file contents of the injected project, preserving the hierarchy and providing descriptive information for each file type.

10. You can now use the generated context file as input to a long-context LLM, such as Claude Opus, to provide it with the context of your project for coding assistance.

## File Type Handling

LLM-PCI automatically distinguishes between text files and other file types using the `mimetypes` module in Python. It determines the MIME type of each file based on its extension.

- Text files: If the MIME type starts with "text/", the file is considered a text file. The contents of text files are included in the generated context file, surrounded by triple backticks (```).
- Non-text files: If the MIME type doesn't start with "text/" or is not available, the file is treated as a non-text file. The script includes the file name, file type, and file size in the generated context file.

This approach eliminates the need to manually whitelist specific file extensions and allows for a more flexible and programmatic distinction between text files and other file types.

## Contributing

Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize and enhance the script based on your specific requirements and preferences.

Happy coding with LLM-PCI!