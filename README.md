# DummyJSON Data Collector Plugin

This plugin is designed to fetch user and post data from the [DummyJSON API](https://dummyjson.com/) . The code is modular and separated by responsibility into `base_client.py`, `client.py`, `data_collector.py`, and `main.py`.

---

## ⚙️ Setup & Usage

1. **Clone the repository**

```bash
git clone https://github.com/yuvalmaliniak/dummyjson-plugin.git
cd dummyjson-plugin
python3 -m venv .venv
source .venv/bin/activate # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```

2. **Create a `.env` file in the root folder with:**

```env
USERNAME=YOUR_USERNAME
PASSWORD=YOUR_PASSWORD
BASE_URL = YOUR_BASE_URL
```
3. **Run the script**

```bash
python main.py
```

## 🧠 Plugin Workflow

### `main.py`

The central execution script. It:

- ✅ Authenticates the user via the `Client`
- 📥 Calls the `DataCollector` to fetch and structure data
- 🖨️ Prints the results:
  - **E1** – Collect the authenticated user details (the user you picked to use).
  - **E2** – Collect a list of 60 posts in the system.
  - **E3** – Collect a list of 60 posts, including each post’s comments.

## 🛠 Files Breakdown & How to Customize

### 🔑 `client.py`

Handles all API interactions.

#### Key Functions:

- `authenticate()` – Logs into DummyJSON and stores the auth token

#### 🔄 What to change (if switching APIs):

- Update .env file with all 3 variables
- Modify `authenticate()` to match the new login endpoint and payload
- Update header structure for token passing (e.g., Bearer token)
- Modify `self.evidences_to_collect` from 3 to the new number of evidences
- Adapt or add new methods to access different endpoints

---

### 🧠 `data_collector.py`

Handles the logic for building structured data, split into three evidence types:

- `collect_e1()` → Fetches authenticated user info  
- `collect_e2()` → Fetches a list of 60 posts  
- `collect_e3()` → Enriches posts with user and comment info  

#### 🔄 What to change

- Redefine the `collect_e1`, `collect_e2`, and `collect_e3` methods based on what your use case requires.  
- If your data source or enrichment logic changes, update the respective `self.client.get(...)` endpoints or processing logic accordingly.  
- For custom evidence types, simply add a new `collect_eX()` method and include it in your workflow.

---

### 🧪 `main.py`

Minimal script that coordinates everything.

#### When to change:

- You want to modify output formatting or printing
- You want to add CLI arguments or logging
- You want to save results to a file or database
