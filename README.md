# MongoDbShellConverter

**MongoDbShellConverter** is a lightweight Python utility that converts MongoDB documents between two popular formats:

- **Mongo Shell (Robo 3T)** syntax  
- **MongoDB Compass** extended JSON format

This tool is ideal for developers who frequently switch between GUI-based tools like Robo 3T and Compass, or who need to migrate/export documents in a specific format.

---

## 🔄 Supported Conversions

| From Format           | To Format             | Method                                 |
|-----------------------|------------------------|----------------------------------------|
| Robo 3T Shell Format  | MongoDB Compass Format | `MongoJsonConverter.to_mongo_compass()`<br>`MongoJsonConverter.convert_robo3t_to_compass()` |
| MongoDB Compass Format | Robo 3T Shell Format  | `MongoJsonConverter.from_mongo_compass()`<br>`MongoJsonConverter.convert_compass_to_robo3t()` |

The conversion supports:

- `ObjectId("...")` ⇄ `{"$oid": "..."}`
- `NumberInt(...)` ⇄ `{"$numberInt": "..."}`
- `ISODate("...")` ⇄ `{"$date": "..."}`
- `true`, `false`, `null` values

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/dogukannozturkk/MongoDbShellConverter.git
cd MongoDbShellConverter
```

### 2. Run the Tool

Make sure you have Python 3.7+ installed.

```bash
python main.py
```

You'll be prompted to select a conversion mode:

```
Dönüştürme modu seçin:
1: Shell (Robo 3T) → Compass
2: Compass → Shell (Robo 3T)
Seçiminiz:
```

Depending on your choice, the script will:

- Read from `robo3t.json` or `mongo_compass.json`
- Convert the content
- Write output to `output_mongo_compass.json` or `output_robo3t_format.json`

---

## 📁 Project Structure

```bash
.
├── main.py
└── src/
    └── mongo_json_converter.py
```

---

## 📌 Why Use This?

- 🧩 Simplifies copy-pasting documents between MongoDB tools
- ✅ Validates converted content as real JSON
- 💡 Useful for automation or scripting needs
- 📚 Easy to understand and extend

---

## 🛠️ Future Plans

- Add support for:
  - `NumberLong`
  - `Decimal128`
  - Binary data
- Add CLI flags (e.g. `--input`, `--output`, `--mode`)
- Unit tests

---

## 🙌 Contributing

Pull requests are welcome. If you have suggestions for improvements or encounter issues, feel free to open an issue or PR.

---

## 📄 License

MIT License — [see here](LICENSE)

---

> Developed with ❤️ by [@dogukannozturkk](https://github.com/dogukannozturkk)
