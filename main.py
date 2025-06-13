from src.mongo_json_converter import MongoJsonConverter

if __name__ == "__main__":
    mode = input("Dönüştürme modu seçin:\n1: Shell (Robo 3T) → Compass\n2: Compass → Shell (Robo 3T)\nSeçiminiz: ").strip()

    if mode == "1":
        with open("json_files/input_json/robo3t.json", "r", encoding="utf-8") as f:
            test_data = f.read()
        converted = MongoJsonConverter.convert_robo3t_to_compass(test_data)
        output_file = "json_files/output_json/output_mongo_compass.json"
    elif mode == "2":
        with open("json_files/input_json/mongo_compass.json", "r", encoding="utf-8") as f:
            test_data = f.read()
        converted = MongoJsonConverter.convert_compass_to_robo3t(test_data)
        output_file = "json_files/output_json/output_robo3t_format.json"
    else:
        print("Geçersiz seçim. Çıkılıyor...")
        exit(1)

    print("\nConverted")

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(converted)

    print(f"\nSonuç dosyaya yazıldı: {output_file}")