import pandas as pd

def load_orphadata(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)


    # Building synthetic medical description from given fields
    def build_description(row):
        parts = []
        if "Name" in row and pd.notna(row["Name"]):
            parts.append(str(row["Name"]))
        if "DisorderType" in row and pd.notna(row["DisorderType"]):
            parts.append(f"is a {row['DisorderType']} disorder")
        if "AgeOfOnset" in row and pd.notna(row["AgeOfOnset"]):
            parts.append(f"with onset in {row['AgeOfOnset']}")
        if "TypeOfInheritance" in row and pd.notna(row["TypeOfInheritance"]):
            parts.append(f"inherited as {row['TypeOfInheritance']}")
        return " ".join(parts)

    df["description"] = df.apply(build_description, axis=1)

    # Keep only needed columns
    df = df.rename(columns={"Name": "disease_name"})
    return df[["disease_name", "description"]]