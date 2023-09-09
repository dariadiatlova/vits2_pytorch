from pathlib import Path
import glob


def write_txt(txt_path: Path, data: list) -> None:
    with open(txt_path, "w", encoding="utf-8") as f:
        for m in data:
            f.write(m + "\n")

def run(source_path, target_path, n_val):
    Path(target_path).mkdir(exist_ok=True)
    wavs = glob.glob(f"{source_path}/*.wav")
    test_data = []
    train_data = []

    for i, wav_path in enumerate(wavs):
        with open(Path(wav_path).with_suffix(".txt")) as f:
            raw_text = f.readline().strip("\n")
        res_string = "|".join([wav_path, raw_text])
        if i < n_val:
            manifest_name = Path(target_path) / "test.txt"
            test_data.append(res_string)
        else:
            manifest_name = Path(target_path) / "test.txt"
            train_data.append(res_string)
    print(f"Collected: {len(test_data)} for test files")
    print(f"Collected: {len(train_data)} for train files")

    write_txt(txt_path=Path(target_path) / "test.txt", data=test_data)
    write_txt(txt_path=Path(target_path) / "train.txt", data=train_data)


if __name__ == "__main__":
    source_path = "/app/data/renamed_corpus"
    target_path = "/app/data/vits_manifests"
    n_val = 128
    run(source_path, target_path, n_val)
