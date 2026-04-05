# Agricultural Fertilizer Recommendation Agent

This AI agent helps farmers and gardeners recommend the best fertilizer combinations based on soil chemical composition and desired crop type.

## Setup

1. Clone or download this repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Download the local LLM model:
   ```
   python scripts/download_model.py
   ```
   Note: This requires ~5GB of disk space and may take time depending on your internet connection.

## Usage

Run the agent interactively:

```
python main.py
```

The agent will prompt you for:

- Soil pH level
- Nitrogen level (low/medium/high)
- Phosphorus level (low/medium/high)
- Potassium level (low/medium/high)
- Crop type (e.g., corn, wheat)

Alternatively, for command-line arguments (non-interactive):

```
python main.py --ph 6.5 --n low --p medium --k high --crop corn
```

Parameters:

- `--ph`: Soil pH level (float, e.g., 6.5)
- `--n`: Nitrogen level (low/medium/high)
- `--p`: Phosphorus level (low/medium/high)
- `--k`: Potassium level (low/medium/high)
- `--crop`: Crop type (e.g., corn, wheat)

## Example Output

The agent will output fertilizer recommendations like:

- Apply 167 lbs/acre of 15-15-15 as starter fertilizer in the band.
- Sidedress with 55 lbs N/acre of urea if PSNT indicates need.

## Troubleshooting

- If the model download fails, ensure you have `huggingface_hub` installed and a Hugging Face account (optional for public models).
- For GPU acceleration, ensure CUDA is installed and `torch` is compiled with CUDA support.
- If responses are slow, consider using a smaller model or quantized version.

## Data Sources

Recommendations are based on Cornell University Whole Farm Nutrient Management tutorials and general agricultural guidelines.
