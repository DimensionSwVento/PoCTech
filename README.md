# PoCTech
<img width="987" height="796" alt="image" src="https://github.com/user-attachments/assets/01520c28-90ca-4985-80b1-1e7f417278be" />

<h1>🌍 GIS Proof of Concept: ArcGIS + Python + Matplotlib</h1>

<h2>1. Overview</h2>
<p>
This project is a <strong>proof of concept (PoC)</strong> demonstrating how 
<strong>Python</strong> can be used to integrate <strong>ArcGIS Online public services</strong> 
with scientific visualization libraries such as <strong>Matplotlib</strong>.
The objective is to retrieve geospatial data from external ArcGIS Feature Services,
process it programmatically, and visualize spatial patterns using basic plotting techniques.
</p>

<p>
The example focuses on accessing <strong>publicly available geospatial datasets</strong>
(no authentication required) and generating simple spatial visualizations as a first step
toward more advanced GIS-based decision support systems.
</p>

<hr>

<h2>2. Objectives</h2>
<ul>
  <li>Demonstrate how to connect to ArcGIS Online public services using Python.</li>
  <li>Retrieve and process vector geospatial data (Feature Layers).</li>
  <li>Extract geometry information from GIS features.</li>
  <li>Visualize spatial data using Matplotlib.</li>
  <li>Provide a reproducible workflow that can be extended to multicriteria or energy-related analyses.</li>
</ul>

<hr>

<h2>3. Technologies Used</h2>
<table>
  <thead>
    <tr>
      <th>Technology</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Python 3.x</td>
      <td>Core programming language</td>
    </tr>
    <tr>
      <td>ArcGIS API for Python</td>
      <td>Access to ArcGIS Online GIS services</td>
    </tr>
    <tr>
      <td>Matplotlib</td>
      <td>Scientific plotting and visualization</td>
    </tr>
    <tr>
      <td>Virtual Environment (venv)</td>
      <td>Dependency isolation</td>
    </tr>
    <tr>
      <td>Public ArcGIS Feature Services</td>
      <td>External geospatial data sources</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>4. Project Structure</h2>
<pre>
EjemploGIS/
│
├── .venv/                  # Python virtual environment
├── analisis_geo.py         # Main Python script
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
</pre>

<hr>

<h2>5. Installation and Setup</h2>

<h3>5.1 Create and activate a virtual environment</h3>

<pre>
python -m venv .venv
</pre>

<p>Activate the environment:</p>

<p><strong>Windows (CMD):</strong></p>
<pre>
.venv\Scripts\activate
</pre>

<p><strong>Windows (PowerShell):</strong></p>
<pre>
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
</pre>

<hr>

<h3>5.2 Install dependencies</h3>

<pre>
pip install arcgis matplotlib
</pre>

<p>Alternatively, using <code>requirements.txt</code>:</p>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>6. Data Source</h2>
<p>
This proof of concept uses <strong>public ArcGIS Online Feature Services</strong>,
which can be accessed without authentication.
</p>

<p><strong>Example dataset:</strong></p>
<ul>
  <li><em>USA Current Wildfires (Feature Service)</em></li>
</ul>

<p>
Source: ArcGIS Living Atlas (Public)
</p>

<hr>




