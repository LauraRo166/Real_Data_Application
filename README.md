# Real Data Application

This project provides tools for parsing, analyzing, and visualizing real-world health data, focusing on non-communicable disease mortality statistics.

## Project Structure

- `src/`
  - `parser.py`: Functions to parse and load data.
  - `analyzer.py`: Data analysis utilities.
  - `visualizer.py`: Visualization tools.
  - `run_visualizer.py`: Example script to run visualizations.
- `notebooks/`
  - Jupyter notebooks for data exploration and prototyping.
- `data/`
  - Contains the main dataset (`data.csv`).
- `tests/`
  - Unit tests for each module.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

- Run analysis or visualization scripts from the `src/` directory.
- Explore and prototype in the `notebooks/` directory.

## Testing

Run all tests with:
```
pytest
```

## Requirements

- Python 3.8+
- See `requirements.txt` for dependencies.

## License

MIT License.

Data repository from World Health Organization (WHO):
[Global Health Observatory data repository](https://apps.who.int/gho/data/?theme=main)

