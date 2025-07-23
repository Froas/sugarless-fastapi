# Sugarless API

A FastAPI project for managing sugarless products with MongoDB Atlas.

---

## 🚀 Overview

This project provides a simple REST API for working with sugarless product data, built on **FastAPI** and **MongoDB Atlas**.
You can add, retrieve, update, and delete sugarless products.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **FastAPI**
* **MongoDB Atlas**
* **pymongo** 
* **Pydantic**
* **Uvicorn**

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/sugarless-api.git
cd sugarless-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file or export the following variables:

```
MONGO_URI=mongodb+srv://<user>:<pass>@<cluster-url>/<dbname>
MONGO_DB=sugar_db
MONGO_COLLECTION=sugar_data
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

---

## 🧩 API Endpoints

| Method | Endpoint         | Description          |
| ------ | ---------------- | -------------------- |
| GET    | `/products`      | Get all products     |
| POST   | `/products`      | Add a new product    |
| GET    | `/products/{id}` | Get product by ID    |
| PUT    | `/products/{id}` | Update product by ID |
| DELETE | `/products/{id}` | Delete product by ID |

---

## 🗂️ Bulk Data Import

To import a large JSON file into MongoDB Atlas, use:

```bash
mongoimport --uri "mongodb+srv://<user>:<pass>@<cluster-url>/sugar_db" --collection sugar_data --type json --file sugarless_1000.json --jsonArray
```

Replace `<user>`, `<pass>`, and `<cluster-url>` with your actual Atlas credentials.

---

## 🌐 Documentation

Interactive Swagger UI available at:

* [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 💡 License

[MIT](https://github.com/Froas/sugarless-fastapi/blob/master/LICENSE)

---

**Made with ❤️ by [Froas](https://github.com/Froas)**

---
