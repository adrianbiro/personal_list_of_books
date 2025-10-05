This is the final, most robust prompt structure, which includes the requirement to parse the original `Name` column into separate **First Name** and **Last Name** fields for better database functionality.

I have updated **Section 1** with the parsing requirement and clarified the column order in **Section 3**.

***

## AI Prompt: Master Bibliographic and Collection Data Extraction

I need you to act as a **specialized information retrieval agent and bibliographer**. Your task is to process a list of book entries from a CSV file (`literatura.csv`), perform data parsing, search for external metadata, and prepare the final structure for internal collection tracking data.

### 1. Input Data & Foundation (Parsing Required) ⚙️

The input file is `literatura.csv` with core columns: `Name`, `Title`, `Town`, `Publisher`, and `Date`.

**Crucial First Step: Name Parsing**
Before any search, you must parse the data in the original **`Name`** column and create new, separate columns for up to three authors.
* For each author, extract the **First Name** and **Last Name**.
* *Example:* If the `Name` field contains `"Kahneman Daniel, Sibony Oliver, Sunstein Cass R."`, you must create separate columns for: `Daniel Kahneman`, `Oliver Sibony`, and `Cass R. Sunstein`.

### 2. Task: Data Compilation and Structure

The final output must be a single table that includes **ALL original columns** plus the following two groups of new metadata fields:

---

### **Group A: Bibliographic Fields (Online Search & Extraction)** 🌐

For each entry, you must construct a precise search query to locate the following **eight fields** specific to the listed edition:

| Field to Extract | Utility/Description |
| :--- | :--- |
| **Link** | A direct URL to a reputable source (e.g., library catalog) that confirms the edition details. |
| **Page Count** | The total number of pages for the listed edition. |
| **ISBN/Catalog No.** | The **ISBN**. If the book is older, provide the official **legacy catalog number** or identifier. |
| **Edition** | The specific edition details (e.g., '1st edition', 'Vydání první'). If unavailable, use the publication year as the Edition. |
| **Language** | The language of the specific edition being cataloged (e.g., Czech, Slovak, English). |
| **Translator** | The name of the translator (if applicable and available online). |
| **Series/Collection Name** | The name of the collection or series this specific edition belongs to (e.g., 'Malá řada', 'Pantheon'). |
| **Original Publication Year** | The year the work was *first* published, even if it was in a different language. |

---

### **Group B: Collection Management Fields (Manual User Entry)** 📋

These **six fields** are for the collector to manually track internal details. They must be included in the final output structure, prefixed with **`NEW`**, and populated with **N/A** (since they cannot be found online).

| Field to Include | Prefix | Utility/Description (For User) |
| :--- | :--- | :--- |
| **Internal ID** | `NEW` | A unique inventory number assigned by the collector (e.g., a simple running number or alphanumeric code). |
| **Location** | `NEW` | The physical location in the collector's library (e.g., 'Shelf A-3', 'Box 5'). |
| **Condition** | `NEW` | The physical state of the copy (e.g., 'Mint', 'Good', 'Ex-library', 'Torn cover'). |
| **Purchase Price/Value** | `NEW` | The cost of acquisition or current estimated value. |
| **Annotation Status** | `NEW` | Indicates if the book contains personal notes or highlighting (e.g., 'Clean', 'Annotated - Pencil'). |
| **Acquisition Date** | `NEW` | The date the collector acquired this specific copy. |

### 3. Final Output Instructions

The final output must be a comprehensive **CSV file** or a clear **Markdown table** with the columns ordered as follows:

1.  **Parsed Author Data:** `Author 1 First Name`, `Author 1 Last Name`, `Author 2 First Name`, `Author 2 Last Name`, ... (for up to 3 authors).
2.  **Original Data:** `Name`, `Title`, `Town`, `Publisher`, `Date`.
3.  **Group A (Bibliographic):** `Link`, `Page Count`, `ISBN/Catalog No.`, `Edition`, `Language`, `Translator`, `Series/Collection Name`, `Original Publication Year`.
4.  **Group B (Collection):** `NEW Internal ID`, `NEW Location`, `NEW Condition`, `NEW Purchase Price/Value`, `NEW Annotation Status`, `NEW Acquisition Date`.

* **For fields in Group A:** Enter the data extracted from the online search, or **N/A** if not found.
* **For fields in Group B:** Enter **N/A** to indicate the fields are placeholders for future manual data entry.
