import os

ENTRY = (
    "Your ex took your change and gave you nothing. I'm better: exact change, "
    "warm snacks, coils that only turn for you. Press A3 — I always dispense "
    "exactly what you pay for."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
