
import requests
import pandas as pd
url = "https://remoteok.com/api"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

if response.status_code == 200:
    data = response.json()

    jobs = data[1:]

    job_list = []
    for job in jobs:
        company = job.get("company", "").strip()
        role = job.get("position", "").strip()
        location = job.get("location", "").strip()
        tags = ", ".join(job.get("tags", []))

        job_list.append({
            "Company Name": company,
            "Job Role": role,
            "Location": location,
            "Tags/Features": tags
        })

    df = pd.DataFrame(job_list)

    df.to_csv("remoteok_jobs.csv", index=False, encoding="utf-8")
    print(" RemoteOK jobs saved in 'remoteok_jobs.csv' with clean columns!")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


