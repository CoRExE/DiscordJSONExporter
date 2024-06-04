
# Discord JSON Exporter

## Overview

Discord JSON Exporter is a tool designed to read and report JSON data from Discord exports. The tool includes Python scripts for data processing and an HTML template for rendering the report, which lists every message from an author.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Read_Data.py](#readdatapy)
  - [Report_JSON.py](#reportjsonpy)
  - [index.html](#indexhtml)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/CoRExE/DiscordJSONExporter.git
    ```

2. Navigate to the project directory:

    ```sh
    cd DiscordJSONExporter
    ```

3. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Read_Data.py

`Read_Data.py` is a script for reading JSON data from a Discord export and processing it.

#### Usage

1. Place your JSON data file in the same directory as \`Read_Data.py\`.

2. Run the script:

    ```sh
    python Read_Data.py <path_to_json_file>
    ```

This script will extract and organize the data, preparing it for reporting.

#### Example

```sh
python Read_Data.py data/discord_export.json
```

### Report_JSON.py

`Report_JSON.py` is a script for generating a report from the processed JSON data. It creates an HTML file listing every message from each author in the JSON data.

#### Usage

1. Ensure you have the processed data file ready (e.g., from running \`Read_Data.py\`).

2. Run the script:

    ```sh
    python Report_JSON.py <path_to_processed_data>
    ```

This script will generate an HTML report using the \`index.html\` template.

#### Example

```sh
python Report_JSON.py data/processed_data.json
```

### index.html

`index.html` is an HTML template for rendering the JSON data report.

#### Usage

1. Ensure the `index.html` file is in the correct directory.

2. Open `index.html` in a web browser to view the report. The report will list every message from each author included in the JSON export.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out with any questions or issues you encounter while using the Discord JSON Exporter. Happy reporting!
