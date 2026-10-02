
# AI-Powered Demand Forecasting Dashboard Engine

A complete full-stack supply chain planning web application that bridges predictive machine learning with real-time operational dashboard controls. This platform streams public macroeconomic consumer data indices over the web and models predictive trajectories automatically to protect logistics networks from capacity constraints.

Live Interactive Web Application:** [https://streamlit.app](https://streamlit.app)

---

##  System Core Capabilities

*   **Advanced AI Forecasting:** Built with an integrated **Prophet seasonal forecasting engine** capable of identifying underlying macro retail waves and complex annual shopping spikes.
*   **"What-If" Planning Simulation:** Features custom promotional uplift controls that dynamically recalculate backend projections and instantly update the visual interface layout.
*   **Interactive Visualizations:** Includes fluid, responsive multi-series timeline line graphs and categorical sales allocation bar charts powered by **Plotly**.
*   **Enterprise Workflows:** Outfitted with spreadsheet-style editable data grids for manual planning overrides and built-in CSV spreadsheet download/export utility hooks.
*   **Operational Risk Mitigation:** Employs an automated warning engine that evaluates warehouse limits against upcoming peak sales volume and flashes logistics constraint alerts.

---

##  Architecture & Technology Stack

*   **Frontend UI Framework:** Streamlit Core Python Dashboard System
*   **AI Engine Backend:** Prophet Seasonal Forecasting Model (optimized for multi-variable time-series data)
*   **Data Visualization Engine:** Plotly Graphing Objects (Asynchronous Charting)
*   **Data Aggregation Pipeline:** Pandas & NumPy Data Processing Libraries

---

##  Repository File Breakdown

*   `app.py`: The core user interface layer managing widgets, layouts, rendering configurations, metrics, and chart layouts.
*   `model.py`: The machine learning core handling framework instantiation, dataframe formatting, and automated future calculations.
*   `database.py`: The ingestion pipeline responsible for connecting securely to web repositories, pulling transactional metrics, and aggregating timelines.
*   `requirements.txt`: The explicit web server instructions defining cloud installation dependencies.

---

##  Local Installation & Setup Checklist

To run this complete framework locally on your machine, execute these steps inside your terminal:

1. Clone or download this project folder workspace.
2. Initialize a secure Python virtual environment workspace:
   ```bash
   python -m venv venv
   ```
3. Activate the workspace environment:
   *   *Windows:* `venv\Scripts\activate`
   *   *Mac/Linux:* `source venv/bin/activate`
4. Install all engineering dependency packages instantly:
   ```bash
   pip install -r requirements.txt
   ```
5. Fire up your local Streamlit development server:
   ```bash
   streamlit run app.py
   ```

---
*Developed as a full-stack Data Science and Business Intelligence portfolio project.*
