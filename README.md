

<img src="assets/export-bot-nz.png" alt="Export Bot NZ Banner" width="700"/>


# export-bot-nz
Autonomous NZ Data Harvester – an export-focused agent that scrapes, formats, and packages public datasets (e.g. tenders, geospatial, infrastructure) for manual auditing, resale, or insight generation. Offline-first, agentic architecture. Built for resilience and clarity.

# 🛰️ export-bot-nz

**Autonomous NZ Data Harvester** — an export-focused, offline-first agent that scrapes, formats, and packages public datasets (e.g., tenders, geospatial, infrastructure) for manual auditing, resale, or insight generation.  
Built with resilience, clarity, and sovereignty in mind.

> 🧠 Designed for use by civic agents, SMEs, researchers, and independent contractors who require signal over noise in a cluttered data ecosystem.

---

## 📦 Features

- 🔗 **Multi-source ingestion** (web, RSS, GitHub, APIs, TSV, PDF, CSV)
- 🧰 **Multi-format packaging** (Markdown, JSONL, SQLite, PDF)
- 🗃️ **Auto-tagging + folderized export vaults**
- ⛔ **Offline-first mode** (no cloud dependencies)
- 🔍 **Manual verification-ready output**
- 🔁 Modular agent scaffolding for multiple NZ/Global datasets

---

<details>
<summary><strong>🗺️ Local NZ Sources</strong> (Click to expand)</summary>

- [GeoNet](https://www.geonet.org.nz/) – Seismic, volcanic, tsunami data
- [LINZ](https://data.linz.govt.nz/) – Geospatial & cadastral datasets
- [MBIE DataHub](https://www.mbie.govt.nz/) – Economic and regulatory data
- [GETS](https://www.gets.govt.nz/) – Government tenders and contracts
- [Stats NZ](https://www.stats.govt.nz/) – Demographics, trade, census
- [LAWA](https://www.lawa.org.nz/) – Water quality/environmental metrics
- [NZ Parliament API](https://www.parliament.nz/en/pb/bills-and-laws/data-api/) – Legislation + bill tracking
- [Creative NZ](https://www.creativenz.govt.nz/) – Grants, cultural funding

</details>

<details>
<summary><strong>🌐 Global Sources</strong> (Click to expand)</summary>

- [arXiv](https://arxiv.org/) – Research metadata (via OAI-PMH)
- [WTO](https://data.wto.org/) – Trade & tariff data
- [WEF](https://www.weforum.org/) – Insight reports and datasets
- [UN OCHA](https://data.humdata.org/) – Humanitarian data
- [GitHub](https://github.com/topics/nz) – NZ-tagged open repos
- [Hugging Face Datasets](https://huggingface.co/datasets) – For training downstream agents
- [OECD](https://data.oecd.org/) – Country benchmarks
- [IMF](https://data.imf.org/) – Financial flows
- [World Bank](https://data.worldbank.org/) – Global development indicators

</details>

---

## 🧑‍💻 Local Setup (WSL2 or Native Linux)

```bash
git clone https://github.com/MYTHIK-blip/export-bot-nz.git
cd export-bot-nz
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/export_bot.py
⚙️ Works natively in WSL2 with Ollama + Gemini CLI

🧬 Optional: Plug in mistral:instruct, phi, or any LLM supported via Ollama.

🧱 Architecture
sql
Copy
Edit
+------------------------+
|     Scheduler/CLI      |
+------------------------+
          ↓
+------------------------+
|   Source Parsers (TSV, |
|    RSS, PDF, CSV)      |
+------------------------+
          ↓
+------------------------+
|   Data Cleaning & Tagging  |
+------------------------+
          ↓
+------------------------+
| Export Formats (MD, PDF,  |
| JSONL, SQLite)            |
+------------------------+
          ↓
+------------------------+
| Local Vaults / Manual UI |
+------------------------+
🧭 Use Cases
Sector	Use Case	Output
Civic Agents	Export tenders from GETS	Audit packages (PDF)
SMEs	Pull geospatial boundaries	CSV+JSONL bundles
Journalists	Summarize OIA and MBIE data	Markdown digests
Researchers	Harvest StatsNZ + LINZ for models	SQLite datasets
Contractors	Identify relevant RFPs across sectors	Tagged listings

🔒 Philosophy
🧱 Built for local autonomy. Every export is a signal refinement against digital overwhelm.

❌ No mandatory cloud or telemetry

✅ Designed for local-first ownership and repackaging

📦 Works without an internet connection once preloaded

🧠 Placeholder: future LEAN4 verification layer

📄 License
MIT – use, adapt, and fork freely.

🚧 Roadmap (MVP Completion Path)
 Initialize repo and README

 Scaffold folder structure (3 agent types: GETS, GeoNet, LINZ)

 Add local config + logging

 Exporter classes for all file types

 Test run with GETS tender listings

 Tagging + metadata schema

 SQLite + markdown dual write

 (Optional) Add local REPL or CLI HUD

📬 Contact
Built by MYTHIK-blip
For clarity, sovereignty, and data-driven economic enablement.