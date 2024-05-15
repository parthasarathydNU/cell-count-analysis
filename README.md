# Cell Count Analysis

## Project Overview
This project involves analyzing immune cell count data from various samples to determine relative frequencies of different cell populations and to explore differences between responders and non-responders to a specific treatment (tr1) in melanoma patients. The analysis is performed using Python with libraries like Pandas, Matplotlib, and Seaborn.

### Tasks 
- For **detailed insights and analysis** check out the following notebook `notebooks/treatment_analysis.ipynb`. 
- For an executive summary check out `Insights.md`
- For the task related to database design refer file `DatabaseSchemaDesign.md`

## Getting Started

### Prerequisites
- Docker (optional)
- Docker Compose (optional)
- Git (optional, for cloning the repository)

### Installation
1. **Clone the repository (optional):**
   ```bash
   git clone https://github.com/parthasarathydNU/cell-count-analysis.git
   cd cell-count-analysis
   ```

2. **Install packages and access notebook:**
   - Set up virtual environment and activate it
   - Install the packages listed in the `requirements.txt` file
   - Run the following command to start jupyter lab in the working directory of this application
      ```bash
      jupyter lab
      ```
   - Check url printed in the console and follow the link in your browser to access the notebook
   - Navigate to `notebooks` and double click on the `treatment_analysis.ipynb` file to open and view the notebook in your browser


3. **Running as docker container**
   - Run the following command in the working directory of this project
   - To build and run the containers for the first time run the command `docker compose up --build`
   - To re run the containers after editing any of the scripts run the command `docker compose up`
   - Logs will be displayed in the terminal. Check out `sample_logs.md` for sample logs


### File Structure
- `scripts/`: Contains Python scripts for data analysis.
  - `analyze.py`: Script to calculate relative frequencies of cell counts.
  - `statistics_analysis.py`: Script to analyze differences in cell populations.
- `results/`: Contains outputs from the scripts, including CSV files and plots.
- `Dockerfile`: Defines the Docker container setup.
- `docker-compose.yml`: Configures services, networks, and volumes for Docker.
- `requirements.txt`: Lists Python package dependencies.


## Contributing
Feel free to fork the repository and submit pull requests. You can also open an issue if you find any bugs or have suggestions for further improvements.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Authors
- Dhruv Parthasarathy

## Acknowledgments
- Thanks to everyone who has contributed to the open-source packages used in this project.
